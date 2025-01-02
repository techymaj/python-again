import datetime


class Account:
    """ Simple account class """

    def __init__(self, name: str, balance: float):
        self.name = name
        self.__balance = balance  # private field (Name mangling)

    def show_balance(self):
        print(f"The balance is {self.__balance}")

    def describe(self):
        self.show_balance()
        self.__show_date()

    @staticmethod
    def __show_date():  # private
        print(datetime.datetime.now())

    @staticmethod
    def _show_something():  # protected
        pass


dfcu = Account("Maria", 50000000)
dfcu.show_balance()
dfcu.balance = 0
Account.show_balance(dfcu)
Account.describe(dfcu)
Account._show_something()
print("*" * 10)
Account._Account__show_date()  # accessing name mangled method
