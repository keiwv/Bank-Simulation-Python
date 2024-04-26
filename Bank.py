import random
from Account import Account


class Bank:
    def __init__(self, name, accounts=None, ch_count=0):
        self._name = name
        self.__ch_count = ch_count
        self._accounts = accounts if accounts is not None else []

    def addNewAccount(self, account):
        account.account_number = self.generateAccountNumber()
        self._accounts.append(account)
        self.__ch_count += 1

    def displayAllAccounts(self):
        for account in self._accounts:
            print(f"Nombre: {account._name}")
            print(f"Edad: {account._age}")
            print(f"Sexo: {account._sex}")
            print(f"Número de teléfono: {account._phone_number}")
            print(f"Número de cuenta: {account.account_number}")
            print(f"Saldo: ${account._balance}")
            print()

    def generateAccountNumber(self):
        while True:
            account_number = random.randint(30000, 40000)
            if account_number not in self._accounts:
                return account_number
