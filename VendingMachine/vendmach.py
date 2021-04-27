"""
VendingMachine module.

- Add new items with their price to the config.VALID_ITEMS dict.
- Configure accepted coins in the config.VALID_COINS list
"""

import VendingMachine.config as config



class VendingMachine:
    """
    Instances of this class can return items from the config.VALID_ITEMS
    dict keys if enough valid coins are added.
    """
    def __init__(self, itemrequest, coins):
        if not itemrequest in config.VALID_ITEMS:
            raise Exception('[ERROR] Invalid item.')

        is_goodcoin = lambda x: x in config.VALID_COINS

        if not all(map(is_goodcoin, coins)):
            raise Exception('[ERROR] Valid coin values: {}'.format(config.VALID_COINS))

        self.itemrequest = itemrequest
        self.coins = coins


    @property
    def is_payed(self):
        is_payed = False
        budget = sum(self.coins)

        if budget >= self.cost:
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
        return config.VALID_ITEMS[self.itemrequest]


    @property
    def change(self):
        # Guard condition. There won't be a change
        # if there are not enough coins in the first place.
        if not self.is_payed:
            return

        payed = sum(self.coins)
        extra = payed - self.cost
        change = []
        candidatecoins = sorted(config.VALID_COINS)

        while extra > 0:
            coin = candidatecoins.pop()

            while coin <= extra:
                change += [coin]
                extra -= coin

        return change
