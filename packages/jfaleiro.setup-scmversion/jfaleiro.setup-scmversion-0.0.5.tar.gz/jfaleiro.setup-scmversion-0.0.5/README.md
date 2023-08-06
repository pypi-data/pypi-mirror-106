# setup_scmversion

<!-- badges
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![license](https://img.shields.io/pypi/l/jfaleiro.setup-scmversion/0.0.5)](https://pypi.org/project/jfaleiro.setup-scmversion/0.0.5)
[![python version](https://img.shields.io/pypi/pyversions/jfaleiro.setup-scmversion/0.0.5)](https://pypi.org/project/jfaleiro.setup-scmversion/0.0.5)
[![implementation](https://img.shields.io/pypi/implementation/jfaleiro.setup-scmversion/0.0.5)](https://pypi.org/project/jfaleiro.setup-scmversion/0.0.5)
[![format](https://img.shields.io/pypi/format/jfaleiro.setup-scmversion/0.0.5)](https://pypi.org/project/jfaleiro.setup-scmversion/0.0.5)
[![status](https://img.shields.io/pypi/status/jfaleiro.setup-scmversion/0.0.5)](https://pypi.org/project/jfaleiro.setup-scmversion0.0.5/)
[![downloads](https://img.shields.io/pypi/dd/jfaleiro.setup-scmversion)](https://pypi.org/project/jfaleiro.setup-scmversion/)
[![pipeline status](https://img.shields.io/gitlab/pipeline/jfaleiro.open/setup_scmversion/0.0.5)](https://gitlab.com/jfaleiro.open/setup-scmversion/pipelines)
[![coverage](https://img.shields.io/gitlab/coverage/jfaleiro.open/setup_scmversion/0.0.5)](https://gitlab.com/jfaleiro.open/setup_scmversion)

![png tester2](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHoAAABkCAYAAABJhSQPAAAACXBIWXMAAAsTAAALEwEAmpwYAAADf0lEQVR42u3dW2vTYBzH8eeUPDm0adN2adeddNMpo2ObXoypsDvFd+WbEfRSUUHvxIFOEXG7UEFR5xybulO3tU3XpF4JIiJ43Pw/v+8LKP3nQ54nIaTlC2fOXGKIfAKHANAI0AjQCNAI0AjQCNAI0AjQgEaARoBGgEaARoBGgEaARoBGgAY0AjQCNAI0AjQCNAI0AjQCNKARoBGgEaARoNE/T+EQHL4SwXhsCbnrKWvHU3bdV3rHV3rPlXrPkbqppY5tYXUkVx3JZSo4Z4wxkXa7KukmKul2dDvdd+Mk9ltJ7DeTGNAHXFML+Slnu6slnVkpOfm1og5bttC/8lmp4LwtuGhbzGo40t1kFs7ogyjljNV9ZS9V3OB11Su97XUrWLqJFFtcLEdu9vmRTPSq3+vDHk2oli3k66qXWzie7V8r6AIuxogty+/KbvbxydzActmJcNVNrIYW6uloED0ay4/i9opg64GlH4yHgwe57wL6L/YhtN17k4Xh95HT8z99b0D/xBl891Rx5DDuv4D+AzW1kHMThaFnRzOD//McgP5BT0aD6N5UYYzCLID+Th/ztnPzXFSr+ypDZSZAf3MvPF/LVw/7rRKgf6NtX9nXZsvjW1krS3E+QDPGXgz64e2ZngnKMxoPfXeqMPh0NBimPqex0G3FxfXZythKSZdMmNdI6B1XWlcu9J1uauGYMrNx0OuBpS9f7JsxbW6joD+EtnvlfHXaxFVMABnQpJZrk5GNgN51pDJxTzYKuiM5v3q+epoh2tA3zkUn91zpgpkw9P3xfHWp4pZBTBj6bcXNUnwCBeivatlCXpstY1+mDn1nuucYWIlDv+z3cm+qbi9YCUO3FRe3zkZTICUOPV8L+8BJHLruKevJiWAEnMSh5ybDI6AkDr2VUfbLAR/LNnXo+Vo4AEbi0E0t5IshH9DUoRdHggiEBkA/rOWPg5A49GpBeynHD+KRh148lsUjSOrQKWfs2dHMEPiIQ28ElgM6A6Df9Ho50BkA/arfw20VdeiUM7ZW1EXQEYduaIl3uk2A3sjhQswI6PWc7YHNAOjNwAK0CdBbGUAbAb3r4RUbI6BbWtpgMwC6rbgFNgOgv/z1DyIOLdJuF2wGQNud7j7YDIB24qQNNgOgM42kCTYDoPO7+w2wGQAd1gFtBHRxuw1oE6AL2/stsBkA7cVJB2w/32c7r8DNq/e3jAAAAABJRU5ErkJggg==)

-->

Builds a semantic version number based on information available on your scm (tag, branch, and number of commits).

See [LICENSE](LICENSE) for important licensing information.


## Instalation

```bash
pip install jfaleiro.setup-scmversion
```

Or as a `dev` dependency in [`poetry`](https://python-poetry.org/):

```bash
poetry add jfaleiro.setup-scmversion --dev
poetry update
```

Currently only `git` is supported.

## Use

A semantic version number is created from standard data available in your *scm*, i.e. tag, branch name, and number of commits from a tag or master. It supports a simple workflow:

* Versions follow a simplified [semantic versioning](https://semver.org/) scheme.
* Non-production releases are produced from release branches named `release/<version>`.
* Non-production releases are produced from feature-releases named `feature/<version>`.
* Production releases and releases candidates are generated from a `tag` in `master` after a release branch is merged to master. The version will match the tag.


### Simplest Use

Should apply to most projects. Tag the current version before build or deploy using a command line:

```bash
$ scmversion version
0.0.1.dev1
```

```bash
V=`scmversion version`
echo 
0.0.1.dev1
```

or the type of version:

```bash
$ scmversion version-type
RELEASE_BRANCH
```

The type of version can be one of `RELEASE`, `RELEASE_BRANCH`, `FEATURE_BRANCH`, or `OTHER`.

### Pre-commit

For use as a [`pre-commit` hook](https://pre-commit.com/) add this to your `.pre-commit-config.yaml`

```yaml
  - repo: https://gitlab.com/jfaleiro.open/setup_scmversion
    rev: 0.0.5
    hooks:
      - id: tag-version
```


## Versioning Schema

* Release branches `release/<version>` with `nnn` differences from master will produce a `RELEASE_BRANCH` with a version `<version>-dev<nnn>`
* Feature branches `feature/<version>` with `nnn` differences from master will produce a `FEATURE_BRANCH` with a version `<version>-feature<nnn>`
* A well-formed tagged version `<tag>` on master will produce a `RELEASE` version `<tag>`.
* Everything else will produce `0.0.0+master...` for master or `0.0.0+other...` for any other branch.
