"""
VendingMachine module.

- Add new items with their price to the VALID_ITEMS dict.
- Configure accepted coins in the VALID_COINS list
"""


VALID_ITEMS = {
    'nuke license': 30,
    'renderfarm time': 70,
}
VALID_COINS = [10, 20, 50]


class VendingMachine:
    """
    Instances of this class can return items from the VALID_ITEMS
    dict keys if enough valid coins are added.
    """
    def __init__(self, itemrequest, coins):
        if not itemrequest in VALID_ITEMS:
            raise Exception('[ERROR] Invalid item.')

        is_goodcoin = lambda x: x in VALID_COINS

        if not all(map(is_goodcoin, coins)):
            raise Exception('[ERROR] Valid coin values: {}'.format(VALID_COINS))

        self.itemrequest = itemrequest
        self.coins = coins


    @property
    def is_payed(self):
        is_payed = False

        if sum(self.coins) >= VALID_ITEMS[self.itemrequest]:
            is_payed = True

        return is_payed


    @property
    def item(self):
        item = None

        if self.is_payed:
            item = self.itemrequest

        return item


    @property
    def cost(self):
        return VALID_ITEMS[self.itemrequest]


    @property
    def change(self):
        return




if __name__ == '__main__':
    pass

    result = VendingMachine(item='nuke license', coins=[1])
