class Cuenta():
  # Constructor de la clase Cuenta
  def __init__(self, name, balance, password):
    self.name = name
    self.balance = int(balance)
    self.password = password

  # Método para depositar en la cuenta
  def deposit(self, amountToDeposit, password):
    if password != self.password:
      print('Lo siento, contraseña incorrecta')
      return None

    if amountToDeposit < 0:
      print('No puedes depositar una cantidad negativa')
      return None

    self.balance = self.balance + amountToDeposit
    return self.balance

  # Método para retirar dinero de la cuenta
  def withdraw(self, amountToWithdraw, password):
    if password != self.password:
      print('Contraseña incorrecta para esta cuenta')
      return None

    if amountToWithdraw < 0:
      print('No puedes retirar una cantidad negativa')
      return None

    if amountToWithdraw > self.balance:
      print('No puedes retirar más de lo que tienes en tu cuenta')
      return None

    self.balance = self.balance - amountToWithdraw
    return self.balance

  # Método para obtener el saldo de la cuenta
  def getBalance(self, password):
    if password != self.password:
      print('Lo siento, contraseña incorrecta')
      return None

    return self.balance

  # Agregado para depuración
  def show(self):
    print(' Nombre:', self.name)
    print(' Saldo:', self.balance)
    print(' Contraseña:', self.password)
    print()