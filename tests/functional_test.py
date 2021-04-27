import pytest
import VendingMachine.vendmach as vendmach



def test_functionality_example():
    # The item's name we want
    itemname = 'renderfarm time'
    # The budget
    budget = []
    machine = vendmach.VendingMachine(
        itemrequest=itemname,
        coins=budget,
    )

    assert machine.item is None
    # budget is not enough
    assert not machine.is_paid

    budget += [-1]

    # The budget contains coins not configured
    # for the vending machine
    with pytest.raises(expected_exception=vendmach.BadCoinError):
        machine.coins = budget

    assert machine.item is None
    # budget is not enough
    assert not machine.is_paid

    budget = [10]
    machine.coins = budget

    # budget is still not enough
    assert machine.item is None
    assert not machine.is_paid

    budget = [10, 10, 50]
    machine.coins = budget

    # budget is just enough, we get the item. The machine's state
    # is paid. There's no change.
    assert machine.item == itemname
    assert machine.is_paid
    assert not machine.change

    # adding more to the budget, maybe we get another item (not implemented...)
    machine.coins += [20, 50]

    # we get the item(s), the machine is paid and we get change back.
    # we get back what we added as extra, the item was precisely paid
    # for the last time.
    assert machine.item == itemname
    assert machine.is_paid
    assert machine.change == [50, 20]

    # we have a bigger budget this time
    machine.coins = [50, 50]

    # we get the item and get change back
    assert machine.item == itemname
    assert machine.is_paid
    assert machine.change == [20, 10]

    # we can get an empty machine and ask it for stuff later
    # when we made up our mind.
    machine = vendmach.VendingMachine()

    # we don't get our item of course
    assert not machine.item
    assert not machine.is_paid

    # if we set the bidget, but don't choose yet we don't get an item
    machine.coins = [50, 50, 50, 50, 50]
    assert machine.item is None
    assert machine.is_paid is None
