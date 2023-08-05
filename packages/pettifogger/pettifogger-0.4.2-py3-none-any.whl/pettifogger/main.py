#!/usr/bin/env python3
import os
import sys
import time
import threading
from argparse import ArgumentParser

from ruamel.yaml.parser import ParserError
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pettifogger.utils.configuration import GlobalConfiguration, set_global_configuration
from pettifogger.utils.stateful_logger import StatefulLogger
from pettifogger.workflow.structure.root import Workflow
from pettifogger.utils.yaml import yaml

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../VERSION")) as version_file:
    version = version_file.read()

__version__ = version


class WorkflowWatcher(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.watched = []
        self._lock = threading.Lock()

    def __release_lock_after_grace_period(self, grace):
        time.sleep(grace)
        self._lock.release()

    def add_to_watched(self, path):
        self.watched.append(path)

    def on_modified(self, event):
        super().on_modified(event)
        if event.src_path.endswith("~") or event.src_path not in self.watched or self._lock.locked():
            return
        self._lock.acquire()
        release = threading.Thread(target=self.__release_lock_after_grace_period, args=(2,))
        release.start()

        if event.is_directory:
            files = os.listdir(event.src_path)
        else:
            files = [event.src_path]
        files = list(map(lambda x: os.path.join(event.src_path, x), files))
        filtered_files = list(filter(lambda x: os.path.exists(x) and not x.endswith("~"), files))
        results = validate_files(filtered_files)

        if not all(results):
            print(f"\n\nWorkflow validation failed, please check the logs", file=sys.stderr)

        print("\n-----------------------------------------------------------------------------------\n")

def validate_files(files):
    results = []
    loggers = {}

    for file in files:
        logger = StatefulLogger(indent=4)
        try:
            with open(file) as workflow_file:
                data = yaml.load(workflow_file)
            wf = Workflow(data)
            result = wf.validate(logger)
            results.append(result)
        except ParserError as e:
            logger.error(str(e), source_id="YAML load")
            results.append(False)
        except Exception as e:
            logger.error(str(e), source_id="YAML load")

        loggers[file] = logger


    for f, l in loggers.items():
        l.summary(filename=f)
        l.reset_state()

    return results

def main():
    parser = ArgumentParser()
    parser.add_argument("--version", action="store_true", help="Print pettifogger's version")
    parser.add_argument("--workflow", help="Path to a workflow file to validate")
    parser.add_argument("--suppress-suspicions", action="store_true", help="Suppresses the suspicion output")
    parser.add_argument("--fail-on-suspicions", action="store_true", help="Suspicions fail the validation")
    parser.add_argument("--no-fail-on-error", action="store_true", help="Errors will not fail the validation")
    parser.add_argument("--watch", action="store_true", help="Watch the file or workflow subdirectories detected automatically")
    args = parser.parse_args()

    if args.version:
        print(f"pettifogger {__version__}")
        exit(0)

    configuration = GlobalConfiguration()
    configuration.suppress_suspicions = args.suppress_suspicions
    configuration.fail_on_suspicions = args.fail_on_suspicions
    configuration.no_fail_on_error = args.no_fail_on_error
    set_global_configuration(configuration)

    watch_paths = set()

    if args.workflow is not None:
        files = [args.workflow]
        if args.watch:
            watch_paths.add(args.workflow)
    else:
        paths_with_files = []
        for path, _, files in os.walk(os.getcwd()):
            paths_with_files.append((path, files))
        filtered = list(filter(lambda x: os.path.join(".github", "workflows") in x[0], paths_with_files))
        if args.watch:
            watch_paths = [item[0] for item in filtered]
        files = [os.path.join(item[0], file) for item in filtered for file in item[1]]

    results = validate_files(files)

    if not args.watch:
        if not all(results):
            print(f"\n\nWorkflow validation failed, please check the logs", file=sys.stderr)
            if args.no_fail_on_error:
                exit(0)
            exit(1)
    else:
        event_handler = WorkflowWatcher()
        observer = Observer()

        for p in watch_paths:
            event_handler.add_to_watched(p)
            observer.schedule(event_handler, p)
        observer.start()

        try:
            while True:
                time.sleep(2)
        except KeyboardInterrupt:
            observer.unschedule_all()
            observer.stop()
        observer.join()

if __name__ == '__main__':
    main()
