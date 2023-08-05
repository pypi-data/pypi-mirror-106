# pettifogger


**pettifogger (noun)**

pet·​ti·​fog·​ger | \ ˈpe-tē-ˌfȯ-gər, -ˌfä- \

**Definition of pettifogger**

1 : a lawyer whose methods are petty, underhanded, or disreputable : shyster

2 : one given to quibbling over trifles

(source: https://www.merriam-webster.com/dictionary/pettifogger)

## Description

Pettifogger is a github actions workflow validator, that will sniff out things like forgotten checkouts and suspicious capital letter words. The intention is to provide some level of additional insight to the workflow files before they go to master/main.

The project is still under initial development and is mainly intended for internal testing but other interested may try it out as well if their sanity can stand it.

## Installation

`pip install pettifogger` or `pip install --upgrade pettifogger`

## Usage

Pettifogger can be run with or without `--workflow` argument. When the argument is defined, then only that workflow is being validated and if used together with `--watch`, then only that file is watched. When used without `--workflow` the tool will search paths matching `.github/workflows` in all subdirectories and will validate those. When the workflows are searched automatically `--watch` will watch all those directories for changes.

```
usage: pettifogger [-h] [--version] [--workflow WORKFLOW] [--suppress-suspicions] [--fail-on-suspicions] [--no-fail-on-error] [--watch]

optional arguments:
  -h, --help            show this help message and exit
  --version             Print pettifogger's version
  --workflow WORKFLOW   Path to a workflow file to validate
  --suppress-suspicions
                        Suppresses the suspicion output
  --fail-on-suspicions  Suspicions fail the validation
  --no-fail-on-error    Errors will not fail the validation
  --watch               Watch the file or workflow subdirectories detected automatically
```

## Known limitations

* Tool has not been tested in Windows or in MacOS. It might work or then not. Please report any issues related to this using the Gitlab issues.
* Shell scripts only support *nix shell dialects (developed using bash). Windows powershell etc. are not supported at the moment.
* If the environment variables are not found from the workflow file, they are considered to be missing. This is something that is currently being looked into.

## License

This project is licensed under MIT license.

