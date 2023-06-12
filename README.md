# web-testing

A basic set of web tests.

## Requirements

- python 3.10.x
- pip

## Setup

```sh
pip install -r requirements.txt
```

If you are using python virtual environments:

```sh
# Tested using 3.10.x
pyversion=3.10.11
pyenv install -s $pyversion
pyenv virtualenv $pyversion webtesting
pyenv local webtesting
pip install -U pip
pip install -r requirements.txt
```

## Usage

Note: `setup.cfg` implies `pytest --verbose --no-header --capture=no --tb=short`.

Run the entire suite of tests:

```sh
pytest
```

Only run tests marked with `dns`:

```sh
pytest -m dns
```

For testing DNS, use a specific name server to resolve records (this can be useful when migrating DNS):

```sh
pytest -m dns --ns 8.8.8.8
```
