
import random 

class Bank:
    def __init__(self, name, ch_count, accounts=None):
        self._name = name
        self.__ch_count = ch_count
        self._accounts = accounts if accounts is not None else []

    def addNewAccount(self, account):
        self._accounts.append(account)
        self.__ch_count += 1
        account.account_number = self.generateAccountNumber()

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

class Account:
    def __init__(self, name, age, sex, phone_number, password, initial_balance=0):
        self._name = name
        self._age = age
        self._sex = sex
        self._phone_number = phone_number
        self._balance = initial_balance
        self._transactions = []
        self._password = password
        self.account_number = 0

    def sendAmount(self, amount, recipient_account):
        if self._balance >= amount:
            self._balance -= amount
            recipient_account.receiveAmount(amount)
            self._transactions.append(f'Transferencia enviada: -${amount}.')
        else:
            print("Fondos insuficientes para realizar el envío")

    def receiveAmount(self, amount):
        self._balance += amount
        self._transactions.append(f'Transferencia recibida: +${amount}.')


# Testing
# BancoBienestar = Bank("Bienestar", 0)
# nueva_cuenta = Account("Brayan", 19, "Hombre", 5727382, "hola", 1000)
# BancoBienestar.addNewAccount(nueva_cuenta)
# old_cuenta = Account("Robasdn", 19, "Hombre", 5727382, "hola", 1000)
# BancoBienestar.addNewAccount(old_cuenta)
# 
# nueva_cuenta.sendAmount(100, old_cuenta)
# 
# BancoBienestar.displayAllAccounts()

