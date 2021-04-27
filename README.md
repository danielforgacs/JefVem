[![Python Pytest testing template](https://github.com/danielforgacs/JefVem/actions/workflows/workflow.yml/badge.svg)](https://github.com/danielforgacs/JefVem/actions/workflows/workflow.yml)


### Brief:

- Multiple item types available
- Can accept different coins e.g. 50p and two 20p's for a value of 90p
- The machine must be capable of handling change

### Notes:

- I left a few unused standard files, like docker compose files, .env, ... in the repo. Those come from my automated git repo initialiser bash func. (See my [.dotfiles repo](https://github.com/danielforgacs/.dotfiles))
- The actual vending machine logic is tiny. I focused on a framework design that other programmers can use in their tools.
- the tests use some hardcoded values. A configuarion update will break them. I wouldn't do that with actual code base.
- optional future directions:
    - items coming from a centralized DB with the vending machine
        tracking inventory across the company.
    - coins also stored in a DB.
    - `singleton` object, so it woulnd't matter where a developer instantiates the class.

### Git branches:

- **`master`: latest tested & approved code ready to be deployed**
- `staging`/`release.dddd`: container branch to test multiple feature/ticket/etc... branches together before merging into master
- `dev`: wip branch


### Setup

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

### docs:

*The **`functional tests`** cover most use cases with examples.*

```python
# import the module:
import VendingMachine.vendmach as vendmach

# get an instance of the vending machine
# with the requested item and the budget:
machine = vendmach.VendingMachine(
    itemrequest='nuke license',
    coins=[20, 50],
)

# As part of a module it can make sense and it's possible
# to instantiate a machine without arguments and set those
# attrs when they became available:
machine = vendmach.VendingMachine()
machine.coins = [20, 10, 50, 50]
machine.itemrequest = 'nuke license'

# If the coins are enough the requested item
# is in the item attr:
print('requested item:', machine.item)

# The actual price of the item is in the cost attr:
print('requested item cost:', machine.cost)

# if the budget was enough, change is in the change attr:
print('change:', machine.change)
```

### make targets:

*makefile targets assume the project virtualenv is active.*

- test: run all tests
