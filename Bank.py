# Banco que administra un diccionario de objetos Cuenta (Cuenta)
from Account import *

class Banco():
  def __init__(self):
    self.cuentasDict = {}
    self.siguienteNumeroCuenta = 0

  def crearCuenta(self, elNombre, elSaldoInicial, elPassword):
    objeto_Cuenta = Cuenta(elNombre, elSaldoInicial, elPassword)
    nuevoNumeroCuenta = self.siguienteNumeroCuenta
    self.cuentasDict[nuevoNumeroCuenta] = objeto_Cuenta
    # Incrementar para prepararse para la próxima cuenta a crear
    self.siguienteNumeroCuenta = self.siguienteNumeroCuenta + 1
    return nuevoNumeroCuenta

  def abrirCuenta(self):
    print('*** Abrir Cuenta ***')
    nombreUsuario = input('¿Cuál es el nombre para la nueva cuenta de usuario? ')
    saldoInicialUsuario = float(input('¿Cuál es el saldo inicial para esta cuenta? '))
    passwordUsuario = input('¿Cuál es la contraseña que deseas utilizar para esta cuenta? ')
    numeroCuentaUsuario = self.crearCuenta(nombreUsuario, saldoInicialUsuario, passwordUsuario)
    print('Tu nuevo número de cuenta es:', numeroCuentaUsuario)
    print()

  def cerrarCuenta(self):
    print('*** Cerrar Cuenta ***')
    numeroCuentaUsuario = int(input('¿Cuál es tu número de cuenta? '))
    passwordUsuario = input('¿Cuál es tu contraseña? ')
    objeto_Cuenta = self.cuentasDict[numeroCuentaUsuario]
    elSaldo = objeto_Cuenta.getBalance(passwordUsuario)
    if elSaldo is not None:
      print('Tenías', elSaldo, 'en tu cuenta, que se te está devolviendo.')
      # Eliminar la cuenta del usuario del diccionario de cuentas
      del self.cuentasDict[numeroCuentaUsuario]
      print('Tu cuenta está cerrada.')

  def saldo(self):
    print('*** Obtener Saldo ***')
    numeroCuentaUsuario = int(input('Por favor, ingresa tu número de cuenta: '))
    passwordUsuario = input('Por favor, ingresa la contraseña: ')
    objeto_Cuenta = self.cuentasDict[numeroCuentaUsuario]
    elSaldo = objeto_Cuenta.getBalance(passwordUsuario)
    if elSaldo is not None:
      print('Tu saldo es:', elSaldo)

  def depositar(self):
    print('*** Depósito ***')
    numCuenta = input('Por favor, ingresa el número de cuenta: ')
    numCuenta = int(numCuenta)
    cantidadDeposito = int(input('Por favor, ingresa la cantidad a depositar: '))
    passwordUsuario = input('Por favor, ingresa la contraseña: ')
    objeto_Cuenta = self.cuentasDict[numCuenta]
    elSaldo = objeto_Cuenta.deposit(cantidadDeposito, passwordUsuario)
    if elSaldo is not None:
      print('Tu nuevo saldo es:', elSaldo)

  def mostrar(self):
    print('*** Mostrar ***')
    for numeroCuentaUsuario in self.cuentasDict:
      objeto_Cuenta = self.cuentasDict[numeroCuentaUsuario]
      print('    Cuenta:', numeroCuentaUsuario)
      objeto_Cuenta.show()

  def retirar(self):
    print('*** Retirar ***')
    numeroCuentaUsuario = int(input('Por favor, ingresa tu número de cuenta: '))
    cantidadRetiro = int(input('Por favor, ingresa la cantidad a retirar: '))
    passwordUsuario = input('Por favor, ingresa la contraseña: ')
    objeto_Cuenta = self.cuentasDict[numeroCuentaUsuario]
    elSaldo = objeto_Cuenta.withdraw(cantidadRetiro, passwordUsuario)
    if elSaldo is not None:
      print('Retiraste:', cantidadRetiro)
      print('Tu nuevo saldo es:', elSaldo)