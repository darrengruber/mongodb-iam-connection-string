# mongodb-iam-connection-string

[![Release](https://img.shields.io/github/v/release/darrengruber/mongodb-iam-connection-string)](https://img.shields.io/github/v/release/darrengruber/mongodb-iam-connection-string)
[![Build status](https://img.shields.io/github/actions/workflow/status/darrengruber/mongodb-iam-connection-string/main.yml?branch=main)](https://github.com/darrengruber/mongodb-iam-connection-string/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/darrengruber/mongodb-iam-connection-string/branch/main/graph/badge.svg)](https://codecov.io/gh/darrengruber/mongodb-iam-connection-string)
[![Commit activity](https://img.shields.io/github/commit-activity/m/darrengruber/mongodb-iam-connection-string)](https://img.shields.io/github/commit-activity/m/darrengruber/mongodb-iam-connection-string)
[![License](https://img.shields.io/github/license/darrengruber/mongodb-iam-connection-string)](https://img.shields.io/github/license/darrengruber/mongodb-iam-connection-string)

A python CLI and Library for generating MongoDB client connection strings using boto3's credential resolution.

- **Github repository**: <https://github.com/darrengruber/mongodb-iam-connection-string/>
- **Documentation** <https://darrengruber.github.io/mongodb-iam-connection-string/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

``` bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:darrengruber/mongodb-iam-connection-string.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see
[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting
[this page](https://github.com/darrengruber/mongodb-iam-connection-string/settings/secrets/actions/new).
- Create a [new release](https://github.com/darrengruber/mongodb-iam-connection-string/releases/new) on Github.
Create a new tag in the form ``*.*.*``.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
