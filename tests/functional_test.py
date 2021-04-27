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
    assert not machine.is_payed

    budget += [-1]

    # The budget contains coins not configured
    # for the vending machine
    with pytest.raises(expected_exception=vendmach.BadCoinError):
        machine.coins = budget

    assert machine.item is None
    # budget is not enough
    assert not machine.is_payed

    budget = [10]
    machine.coins = budget

    # budget is still not enough
    assert machine.item is None
    assert not machine.is_payed

    budget = [10, 10, 50]
    machine.coins = budget

    # budget is just enough, we get the item. The machine's state
    # is payed. There's no change.
    assert machine.item == itemname
    assert machine.is_payed
    assert not machine.change

    # adding more to the budget, maybe we get another item (not implemented...)
    machine.coins += [20, 50]

    # we get the item(s), the machine is payed and we get change back.
    # we get back what we added as extra, the item was precisely paid
    # for the last time.
    assert machine.item == itemname
    assert machine.is_payed
    assert machine.change == [50, 20]

    # we have a bigger budget this time
    machine.coins = [50, 50]

    # we get the item and get change back
    assert machine.item == itemname
    assert machine.is_payed
    assert machine.change == [20, 10]
