import json


try:
    archivo = open("cuentas.json")
    cuentas = json.load(archivo)
    archivo.close()
except:
    cuentas = {}


def guardar():
    archivo = open("cuentas.json", "w")
    json.dump(cuentas, archivo)
    archivo.close()


while True:
    print()
    print("1. Crear cuenta")
    print("2. Ingresar dinero")
    print("3. Sacar dinero")
    print("4. Transferir dinero")
    print("5. Salir")
    opcion = input("¿Qué quieres hacer? ")

    if opcion == "1":
        nombre = input("Nombre de la cuenta: ")
        cuentas[nombre] = 0
        guardar()
        print("Cuenta creada")

    elif opcion == "2":
        nombre = input("Cuenta: ")
        if nombre in cuentas:
            importe = float(input("Importe: "))
            cuentas[nombre] = cuentas[nombre] + importe
            guardar()
            print("Saldo:", cuentas[nombre])
        else:
            print("Esa cuenta no existe")

    elif opcion == "3":
        nombre = input("Cuenta: ")
        if nombre in cuentas:
            importe = float(input("Importe: "))
            if importe <= cuentas[nombre]:
                cuentas[nombre] = cuentas[nombre] - importe
                guardar()
                print("Saldo:", cuentas[nombre])
            else:
                print("No hay saldo suficiente")
        else:
            print("Esa cuenta no existe")

    elif opcion == "4":
        origen = input("Cuenta de origen: ")
        destino = input("Cuenta de destino: ")
        if origen in cuentas and destino in cuentas:
            importe = float(input("Importe: "))
            if importe <= cuentas[origen]:
                cuentas[origen] = cuentas[origen] - importe
                cuentas[destino] = cuentas[destino] + importe
                guardar()
                print("Transferencia hecha")
            else:
                print("No hay saldo suficiente")
        else:
            print("Alguna cuenta no existe")

    elif opcion == "5":
        print("Hasta luego")
        break

    else:
        print("Opción no válida")