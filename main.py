from Bank import Bank
from Account import Account
import os
import platform

# Verify platform for cleaning screen
system = platform.system()

if system == "Windows":
    clear = "cls"
else:
    clear = "clear"

# --------------- USEFUL FUNCTIONS ----------
def clearConsole():
    os.system(clear)

def pauseConsole():
    input("Presiona enter para continuar...")
# ---------------- MENU FUNCTIONS --------
def displayMenuMsg():
    userInput = -1
    while (userInput < 0 or userInput >= 5):
        clearConsole()
        print("---- MENU -----")
        print("1.- Iniciar sesión")
        print("2.- Registrar usuario")
        print("0.- Salir")
        userInput = int(input("Ingresa tu opcion: "))
    return userInput

def menu():
    op = -1
    while op != 0:
        op = displayMenuMsg()
        if op == 1:
            userAccount = verifyUserLogInMenu()
            if userAccount is not None:
                loggedInMenu(userAccount)
        elif op == 2:
            registerUser()
            
# ------- LOG IN FUNCTIONS ----------
def getUserLogIn():
    clearConsole()
    print("----- INGRESA TUS DATOS ------")
    accountNumberInput = int(input("Ingresa tu numero de cuenta: "))
    accountUserPassword = input("Ingresa tu contraseña: ") 
    return accountNumberInput, accountUserPassword

def verifyUserLogIn(userNumber, userPassword):
    for account in BancoBienestar._accounts:
        if account.account_number == userNumber and account._password == userPassword:
            return account
    return None

def verifyUserLogInMenu():
    while True:
        userNumber, userPassword = getUserLogIn()
        userAccount = verifyUserLogIn(userNumber, userPassword)

        if userAccount is not None:
            return userAccount
        else:
            print("Numero de cuenta o contraseña incorrecta, intenta de nuevo")
            if (int(input("Desea salir? (1.- Sí / 0.- No): "))):
                break
    return None
# ---------- LOGGED IN FUNCTIONS ---------
def loggedInMsg():
    clearConsole()
    print("----- REALIZA OPERACIONES ----- ")
    print("1.- Transferir")
    print("2.- Depositar")
    print("3.- Retirar")
    print("4.- Mostrar saldo")
    print("0.- Cerrar sesión")
    return int(input("Selecciona tu opción: "))


def loggedInMenu(userAccount):
    userOption = -1
    while userOption != 0:
        userOption = loggedInMsg()
        if userOption == 1:
            transfer(userAccount)
        if userOption == 2:
            deposit(userAccount)
        if userOption == 3:
            withdraw(userAccount)
        if userOption == 4:
            showBalance(userAccount)

# ----------- REGISTER FUNCTION -----------
def registerUser():
    clearConsole()
    print("---- REGISTRAR USUARIO ------")
    name = input("Ingresa el nombre de la cuenta: ")
    age = input("Introduce la edad: ")
    sex = input("Introduce tu sexo: ")
    phone_number = int(input("Introduce tu numero de teléfono: "))
    password = input("Ingresa tu contraseña: ")
    num_account = BancoBienestar.addNewAccount(Account(name, age, sex,phone_number,password))
    clearConsole()
    print("Usuario registrado con éxito.")
    print("Por favor, guarda tu numero de cuenta.")
    print(f'Numero de cuenta: {num_account}')
    pauseConsole()

# ---------- TRANSFER MONEY FUNCTION ------
def transfer(account):
    userAccount = 1
    while userAccount != -1:
        clearConsole()
        userAccount = int(input("Ingresa el numero de cuenta a transferir (Ingresa -1 para salir): "))

        if userAccount == account.account_number:
            print("No puedes transferir dinero a la misma cuenta")
        else:
            if userAccount != -1:
                if not BancoBienestar.transferToAccount(account, userAccount):
                    print("No existen demasiados fondos o la cuenta no existe.")


        pauseConsole();

def deposit(account):
    userAccount = 1
    while userAccount != -1:
        clearConsole()
        userAccount = int(input("Ingresa el numero de cuenta a depositar (Ingresa -1 para salir): "))
        if userAccount != -1:
            if userAccount == account.account_number:
                if BancoBienestar.deposit(userAccount):
                    print("Se ha realizado el deposito con exito. ")
                else:
                    print("No se ha podido realizar el deposito")
            else:
                print("Numero de cuenta equivocado.")
            pauseConsole()

def withdraw(account):
    userAccount = 1
    while userAccount != -1:
        clearConsole()
        userAccount = int(input("Ingresa el numero de cuenta a retirar (Ingresa -1 para salir): "))
        if userAccount != -1:
            if userAccount == account.account_number:
                if BancoBienestar.withdraw(userAccount):
                    print("Se ha realizado el retiro con exito. ")
                else:
                    print("No se ha podido realizar el retiro")
            else:
                print("Numero de cuenta equivocado.")
            pauseConsole()

def showBalance(account):
    clearConsole()
    BancoBienestar.showBalance(account)
    pauseConsole()
    
        



# (self, name, age, sex, phone_number, password, initial_balance=0)     

op = 1
BancoBienestar = Bank("Bienestar")

menu()

# DISPLAY INFORMATION
clearConsole()
print()
BancoBienestar.displayAllAccounts()
print()
BancoBienestar.displayAllTransactions()
