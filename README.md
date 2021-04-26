### Brief:

- Multiple item types available
- Can accept different coins e.g. 50p and two 20p's for a value of 90p
- The machine must be capable of handling change

### Git branches:

- **`master`: latest tested & approved code ready to be deployed**
- `staging`: container branch to test multiple feature/ticket/etc... branches together before merging into master
- `dev`: wip branch


### Usage

**Python 3.8**

start env:

```
$ pipenv shell
```

install dependencies:

```
# dev
$ pipenv install --dev

# live
$ pipenv install
```

test:
```
# in the project root dir:
$ python -m pytest

# if the project root is added to the PYTHONPATH:
$ pytest
```

### make targets:

*makefile targets assume the project virtualenv is active.*

- test: run all tests
