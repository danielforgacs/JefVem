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



if __name__ == '__main__':
    pass

    result = VendingMachine(item='nuke license', coins=[1])
