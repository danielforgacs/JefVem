import VendingMachine.vendmach as vendmach



def test_can_init_vendingmachine_w_item_and_coins():
    choice = list(vendmach.VALID_ITEMS)[0]
    response = vendmach.VendingMachine(item=choice, coins=[10])
