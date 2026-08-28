opcion = int(input("Ingrese una opcion (1-3): "))

match opcion:
    case 1:
        print("Saldo")
    case 2:
        print("Deposito")
    case 3:
        print("Salir")
    case _:
        print("Opcion invalida")