# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pettifogger',
 'pettifogger.checks',
 'pettifogger.utils',
 'pettifogger.workflow',
 'pettifogger.workflow.structure',
 'pettifogger.workflow.structure.jobs']

package_data = \
{'': ['*'],
 'pettifogger': ['testdata/.github/workflows/*'],
 'pettifogger.checks': ['testdata/jobs/*', 'testdata/schema/*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'jsonschema>=3.2.0,<4.0.0',
 'networkx>=2.5.1,<3.0.0',
 'ruamel.yaml>=0.17.4,<0.18.0',
 'watchdog==2.1.0']

entry_points = \
{'console_scripts': ['pettifogger = pettifogger.main:main']}

setup_kwargs = {
    'name': 'pettifogger',
    'version': '0.5.0',
    'description': 'Github actions workflow validator',
    'long_description': "# pettifogger\n\n\n**pettifogger (noun)**\n\npet·\u200bti·\u200bfog·\u200bger | \\ ˈpe-tē-ˌfȯ-gər, -ˌfä- \\\n\n**Definition of pettifogger**\n\n1 : a lawyer whose methods are petty, underhanded, or disreputable : shyster\n\n2 : one given to quibbling over trifles\n\n(source: https://www.merriam-webster.com/dictionary/pettifogger)\n\n## Description\n\nPettifogger is a github actions workflow validator, that will sniff out things like forgotten checkouts and suspicious capital letter words. The intention is to provide some level of additional insight to the workflow files before they go to master/main.\n\nThe project is still under initial development and is mainly intended for internal testing but other interested may try it out as well if their sanity can stand it.\n\n## Installation\n\n`pip install pettifogger` or `pip install --upgrade pettifogger`\n\n## Usage\n\nPettifogger can be run with or without `--workflow` argument. When the argument is defined, then only that workflow is being validated and if used together with `--watch`, then only that file is watched. When used without `--workflow` the tool will search paths matching `.github/workflows` in all subdirectories and will validate those. When the workflows are searched automatically `--watch` will watch all those directories for changes.\n\n```\nusage: pettifogger [-h] [--version] [--workflow WORKFLOW] [--suppress-suspicions] [--fail-on-suspicions] [--no-fail-on-error] [--watch]\n\noptional arguments:\n  -h, --help            show this help message and exit\n  --version             Print pettifogger's version\n  --workflow WORKFLOW   Path to a workflow file to validate\n  --suppress-suspicions\n                        Suppresses the suspicion output\n  --fail-on-suspicions  Suspicions fail the validation\n  --no-fail-on-error    Errors will not fail the validation\n  --watch               Watch the file or workflow subdirectories detected automatically\n```\n\n## Known limitations\n\n* Tool has not been tested in Windows or in MacOS. It might work or then not. Please report any issues related to this using the Gitlab issues.\n* Shell scripts only support *nix shell dialects (developed using bash). Windows powershell etc. are not supported at the moment.\n* If the environment variables are not found from the workflow file, they are considered to be missing. This is something that is currently being looked into.\n\n## License\n\nThis project is licensed under MIT license.\n\n",
    'author': 'Aki Mäkinen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/blissfulreboot/python/pettifogger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
