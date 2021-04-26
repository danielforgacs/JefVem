import VendingMachine.vendmach as vendmach



def test_functionality_example():
    itemname = 'renderfarm time'
    budget = []
    item = vendmach.VendingMachine(
        itemrequest=itemname,
        coins=budget,
    )

    assert item.item is None

    print('item cost:', item.cost)
