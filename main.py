from Bank import Bank
from Account import Account
import os

def displayMenuMsg():
    userInput = -1
    while (userInput < 0 or userInput >= 5):
        os.system("clear")
        print("---- MENU -----")
        print("1.- Iniciar sesión")
        print("2.- Registrar usuario")
        print("0.- Salir")
        userInput = int(input("Ingresa tu opcion: "))
    return userInput

def getUserLogIn():
    os.system("clear")
    print("----- INGRESA TUS DATOS ------")
    accountNumberInput = int(input("Ingresa tu numero de cuenta: "))
    accountUserPassword = input("Ingresa tu contraseña: ") 
    return accountNumberInput, accountUserPassword

def verifyUserLogIn(userNumber, userPassword):
    for account in BancoBienestar._accounts:
        if account.account_number == userNumber and account.password == userPassword:
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

def loggedInMsg():
    os.system("clear")
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
        userOption = loggedInMenu()

def menu():
    op = -1
    while op != 0:
        op = displayMenuMsg()
        if op == 1:
            userAccount = verifyUserLogInMenu()
            if userAccount is not None:
                loggedInMenu(userAccount)
            
            

op = 1
BancoBienestar = Bank("Bienestar")

menu()









