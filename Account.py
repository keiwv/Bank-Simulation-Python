from Person import Person

class Account(Person):
    def __init__(self, name, age, sex, phone_number, password, initial_balance=0):
        super().__init__(name, age, sex)
        self._phone_number = phone_number
        self._balance = initial_balance
        self._transactions = []
        self._password = password
        self.account_number = 0

    def sendAmount(self, amount, recipient_account):
        if self._balance >= amount:
            self._balance -= amount
            recipient_account.receiveAmount(amount, self)
            self._transactions.append(f'Transferencia enviada: -${amount}.')
        else:
            print("Fondos insuficientes para realizar el envío")

    def receiveAmount(self, amount):
        self._balance += amount
        self._transactions.append(f'Transferencia recibida: +${amount}.')

    def receiveAmount(self, amount, account):
        self._balance += amount
        self._transactions.append(f'Transferencia recibida: +${amount} por ${account._name}')
