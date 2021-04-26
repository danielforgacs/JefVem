import VendingMachine.vendmach as vendmach



def test_can_init_vendingmachine_w_item_and_coins():
    choice = list(vendmach.VALID_ITEMS)[0]
    response = vendmach.VendingMachine(item=choice, coins=[10])


def test_vendingmachine_knows_if_coins_are_enough():
    choice = list(vendmach.VALID_ITEMS)[0]
    item = vendmach.VendingMachine(item=choice, coins=[10])

    assert not item.is_payed

    item.coins = [50, 50, 50, 50]

    assert item.is_payed
