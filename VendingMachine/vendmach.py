"""
VendingMachine module.

for configuraton see the config.py module.
"""

import VendingMachine.config as config




class VendingMachineErrors(BaseException):
    """
    Base class for the vending machine framework exceptions
    to save on rewriting the init method. Subclass this for
    custom exceptions and set the "message" classmethod.
    """
    def __init__(self):
        super().__init__(self.message)






class BadCoinError(VendingMachineErrors):
    message = '[ERROR] Valid coin values: {}'.format(config.VALID_COINS)







class CoinsDescriptor:
    def __set__(self, obj, value):
        is_goodcoin = lambda x: x in config.VALID_COINS

        if not all(map(is_goodcoin, value)):
            raise BadCoinError()

        obj.__dict__['coins'] = value


    def __get__(self, obj, objtype):
        return obj.__dict__['coins']





class VendingMachine:
    """
    Instances of this class can return items from the config.VALID_ITEMS
    dict keys if enough valid coins are added.
    """
    coins = CoinsDescriptor()


    def __init__(self, itemrequest=None, coins=[]):
        self.itemrequest = itemrequest
        self.coins = coins

        if itemrequest:
            if not itemrequest in config.VALID_ITEMS:
                raise Exception('[ERROR] Invalid item.')



    @property
    def is_paid(self):
        # If we didn't make an item choice yet,
        # being paid or not doesn't make sense.
        if not self.itemrequest:

            return

        is_paid = False
        budget = sum(self.coins)

        if budget >= self.cost:
            is_paid = True

        return is_paid



    @property
    def item(self):
        item = None

        if self.is_paid:
            item = self.itemrequest

        return item



    @property
    def cost(self):
        cost = None

        if self.itemrequest:
            cost = config.VALID_ITEMS[self.itemrequest]

        return cost



    @property
    def change(self):
        # Guard condition. There won't be a change
        # if there are not enough coins in the first place.
        if not self.is_paid:
            return

        paid = sum(self.coins)
        extra = paid - self.cost
        change = []
        candidatecoins = sorted(config.VALID_COINS)

        while extra > 0:
            coin = candidatecoins.pop()

            while coin <= extra:
                change += [coin]
                extra -= coin

        return change
