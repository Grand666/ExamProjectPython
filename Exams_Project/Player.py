class Player:

    def __init__(self, saldo, playerHand):
        self.saldo = saldo
        self.playerHand = playerHand

    @property
    def saldo(self):
        return self.__saldo

    @saldo.getter
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def playerHand(self):
        return self.__playerHand

    @playerHand.getter
    def playerHand(self):
        return self.__playerHand

    @playerHand.setter
    def playerHand(self, playerHand):
        self.__playerHand = playerHand