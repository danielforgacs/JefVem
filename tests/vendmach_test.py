import pytest
import VendingMachine.vendmach as vendmach



def test_can_init_vendingmachine_w_item_and_coins():
    choice = list(vendmach.config.VALID_ITEMS)[0]
    vendmach.VendingMachine(itemrequest=choice, coins=[10])



def test_vendingmachine_knows_if_coins_are_enough():
    choice = list(vendmach.config.VALID_ITEMS)[0]
    machine = vendmach.VendingMachine(itemrequest=choice, coins=[10])
    assert not machine.is_paid

    machine.coins = [50, 50, 50, 50]
    assert machine.is_paid



def test_if_item_is_not_paid_for_item_attr_is_none():
    choice = list(vendmach.config.VALID_ITEMS)[0]
    mchine = vendmach.VendingMachine(itemrequest=choice, coins=[10])
    assert not mchine.is_paid
    assert mchine.item is None

    mchine.coins = [50, 50, 50, 50]
    assert mchine.is_paid
    assert mchine.item == choice



def test_vending_machine_errors_on_bad_arguments():
    """
    Negative tests for better developer feedback
    """
    with pytest.raises(expected_exception=Exception):
        vendmach.VendingMachine(itemrequest='AAA')

    with pytest.raises(expected_exception=Exception):
        vendmach.VendingMachine(itemrequest='AAA', coins=1)

    with pytest.raises(expected_exception=vendmach.BadCoinError):
        vendmach.VendingMachine(itemrequest='AAA', coins=';lkj')



@pytest.mark.parametrize('budget, expected', [
    [[], None],
    [[10], None],
    [[10, 10], None],

    [[10, 10, 10], []],
    [[20, 10], []],
    [[10, 20], []],

    [[10, 10, 10, 10], [10]],
    [[10, 10, 10, 10, 10, 10], [20, 10]],
    [[10, 10, 10, 10, 10, 10, 10], [20, 20]],
    [[10, 10, 10, 10, 10, 10, 10, 10], [50]],

    [[50, 50, 50], [50, 50, 20]],
])
def test_vendingmachine_returns_change_if_overpaid(budget, expected):
    machine = vendmach.VendingMachine(itemrequest='nuke license', coins=budget)
    assert machine.change == expected



def test_can_not_update_coins_with_not_configured_coins():
    machine = vendmach.VendingMachine(
        itemrequest='nuke license',
        coins=[],
    )

    with pytest.raises(expected_exception=vendmach.BadCoinError):
        machine.coins = [123451]



def test_can_instantiate_machine_without_arguments_for_later_use():
    machine = vendmach.VendingMachine()
    assert isinstance(machine, vendmach.VendingMachine)
