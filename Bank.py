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
        return account.account_number

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
    
    def updateAccount(self, updateAccount):
        for account in self._accounts:
            if account.account_number == updateAccount.account_number:
                account = updateAccount
                return
    
    def transferToAccount(self, send_account, receive_account):
        for account in self._accounts:
            if receive_account.account_number == account.account_numer:
                amountToSend = int(input("Ingresa la cantidad a enviar: "))
                send_account.sendAmount(amountToSend, receive_account)
                return True
        return False
