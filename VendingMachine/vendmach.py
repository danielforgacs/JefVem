VALID_ITEMS = {
    'nuke license': 200,
    'renderfarm time': 10000,
}
VALID_COINS = [10, 20, 50]


class VendingMachine:
    def __init__(self, item, coins):
        if not item in VALID_ITEMS:
            raise Exception('[ERROR] Invalid item.')

        is_goodcion = lambda x: x in VALID_COINS

        if not all(map(is_goodcion, coins)):
            raise Exception('[ERROR] Valid coin values: {}'.format(VALID_COINS))

        self.item = item
        self.coins = coins


    @property
    def is_payed(self):
        is_payed = False

        if sum(self.coins) >= VALID_ITEMS[item]:
            is_payed = True

        return is_payed




if __name__ == '__main__':
    pass

    result = VendingMachine(item='nuke license', coins=[1])
