# Programa principal para controlar un Banco compuesto de Cuentas (Accounts)
# Importar todo el código de la clase Banco (Banco)
from Bank import *

# Crear una instancia del Banco
objeto_Banco = Banco()

# Código principal
# Crear dos cuentas de prueba
numeroCuentaJoe = objeto_Banco.crearCuenta('Joe', 100, 'ContraseñaDeJoe')
print("El número de cuenta de Joe es:", numeroCuentaJoe)
numeroCuentaMary = objeto_Banco.crearCuenta('Mary', 12345, 'ContraseñaDeMary')
print("El número de cuenta de Mary es:", numeroCuentaMary)

while True:
    print()
    print('Para obtener el saldo de una cuenta, presione b')
    print('Para cerrar una cuenta, presione c')
    print('Para hacer un depósito, presione d')
    print('Para abrir una nueva cuenta, presione o')
    print('Para salir, presione q')
    print('Para mostrar todas las cuentas, presione s')
    print('Para hacer un retiro, presione w')
    print()

    accion = input('¿Qué deseas hacer? ')
    accion = accion.lower()
    print()

    if accion == 'b':
        objeto_Banco.saldo()
    elif accion == 'c':
        objeto_Banco.cerrarCuenta()
    elif accion == 'd':
        objeto_Banco.depositar()
    elif accion == 'o':
        objeto_Banco.abrirCuenta()
    elif accion == 's':
        objeto_Banco.mostrar()
    elif accion == 'q':
        break
    elif accion == 'w':
        objeto_Banco.retirar()
    else:
        print('Lo siento, esa no es una acción válida. Por favor, intenta nuevamente.')

print('¡Hecho!')