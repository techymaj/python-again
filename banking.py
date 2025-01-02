class Account:
    """ Simple account class """

    def __init__(self, name: str, balance: float):
        self.name = name
        self.__balance = balance  # private field

    def show_balance(self):
        print(f"The balance is {self.__balance}")


    def describe(self):
        self.show_balance()


dfcu = Account("Maria", 50000000)
dfcu.show_balance()
dfcu.balance = 0
Account.show_balance(dfcu)
