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
        print("------------- CUENTAS ---------------")
        for account in self._accounts:
            print(f"Nombre: {account.name}")
            print(f"Edad: {account._age}")
            print(f"Sexo: {account._sex}")
            print(f"Número de teléfono: {account._phone_number}")
            print(f"Número de cuenta: {account.account_number}")
            print(f"Saldo: ${account._balance}")
            print("-------------------------------------")

    def displayAllTransactions(self):
        print("---------- TRANSFERENCIAS -----------")
        for account in self._accounts:
            print(f'Nombre del usuario: {account.name}')
            print(f'Numero de cuenta: {account.account_number}')
            for transfer in account.transactions:
                print(transfer)
            print("-------------------------------------")


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
            if receive_account == account.account_number:
                amountToSend = int(input("Ingresa la cantidad a enviar: "))
                if send_account.sendAmount(amountToSend, account):
                    print("Se ha realizado la transferencia con exito")
                    return True
                else:
                    return False
                
        return False

    def deposit(self, account):
        for accountDeposit in self._accounts:
            if account == accountDeposit.account_number:
                amountToDeposit = int(input("Ingrese la cantidad a depositar: "))
                accountDeposit.receiveDeposit(amountToDeposit)
                return True
        return False

    def withdraw(self, account):
        for accountWithdraw in self._accounts:
            if account == accountWithdraw.account_number:
                amountToWithdraw = int(input("Ingresa la cantidad a retirar: "))
                accountWithdraw.withdraw(amountToWithdraw)
                return True
        return False
