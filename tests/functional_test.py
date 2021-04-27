import VendingMachine.vendmach as vendmach



def test_functionality_example():
    itemname = 'renderfarm time'
    budget = []
    machine = vendmach.VendingMachine(
        itemrequest=itemname,
        coins=budget,
    )

    assert machine.item is None

    print('item cost:', machine.cost)
