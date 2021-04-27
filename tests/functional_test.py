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
    with pytest.raises(Exception):
        machine.coins = budget

    assert machine.item is None
    # budget is not enough
    assert not machine.is_payed
