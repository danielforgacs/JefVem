import VendingMachine.vendmach as vendmach



def test_can_init_vendingmachine_w_item_and_coins():
    choice = list(vendmach.VALID_ITEMS)[0]
    vendmach.VendingMachine(itemrequest=choice, coins=[10])



def test_vendingmachine_knows_if_coins_are_enough():
    choice = list(vendmach.VALID_ITEMS)[0]
    item = vendmach.VendingMachine(itemrequest=choice, coins=[10])
    assert not item.is_payed

    item.coins = [50, 50, 50, 50]
    assert item.is_payed



def test_if_item_is_not_payed_for_item_attr_is_none():
    choice = list(vendmach.VALID_ITEMS)[0]
    item = vendmach.VendingMachine(itemrequest=choice, coins=[10])
    assert not item.is_payed
    assert item.item is None

    item.coins = [50, 50, 50, 50]
    assert item.is_payed
    assert item.item == choice
