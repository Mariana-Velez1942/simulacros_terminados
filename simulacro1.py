
# Paso 1: Declaramos el saldo inicial y el historial vacío
saldo = 1000  # El usuario empieza con $1000
historial = []  # Aquí se guardarán los movimientos (retiros y depósitos)

# Paso 2: Creamos un bucle para que el programa se repita hasta que el usuario decida salir
while True:
    # Mostramos el menú de opciones
    print("\n------ Cajero Automático ------")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir")

    # Pedimos al usuario que elija una opción
    opcion = input("Selecciona una opción (1-5): ")

    # Opción 1: Ver saldo
    if opcion == "1":
        print(f"\nTu saldo actual es: ${saldo}")

    # Opción 2: Retirar dinero
    elif opcion == "2":
        cantidad = float(input("Ingresa la cantidad a retirar: $"))

        # Verificamos si hay suficiente saldo
        if cantidad <= saldo:
            saldo -= cantidad  # Restamos la cantidad al saldo
            historial.append(f"Retiro: -${cantidad}")  # Guardamos el movimiento
            print("Retiro exitoso.")
        else:
            print("Fondos insuficientes.")

    # Opción 3: Depositar dinero
    elif opcion == "3":
        cantidad = float(input("Ingresa la cantidad a depositar: $"))
        saldo += cantidad  # Sumamos la cantidad al saldo
        historial.append(f"Depósito: +${cantidad}")  # Guardamos el movimiento
        print("Depósito exitoso.")

    # Opción 4: Ver historial de movimientos
    elif opcion == "4":
        print("\n--- Historial de movimientos ---")
        if len(historial) == 0:
            print("No hay movimientos aún.")
        else:
            for movimiento in historial:
                print(movimiento)

    # Opción 5: Salir del programa
    elif opcion == "5":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break  # Salimos del bucle y terminamos el programa

    # Si elige una opción no válida
    else:
        print("Opción no válida. Intenta nuevamente.")
