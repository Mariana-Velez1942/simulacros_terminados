# Sistema de Gestión de Estudiantes

# Paso 1: Base de datos inicial con 5 estudiantes
estudiantes = [
    {"id": "101", "nombre": "Juan Pérez", "edad": 20, "nota": 4.2},
    {"id": "102", "nombre": "María López", "edad": 19, "nota": 3.5},
    {"id": "103", "nombre": "Carlos Ruiz", "edad": 21, "nota": 2.8},
    {"id": "104", "nombre": "Ana Gómez", "edad": 18, "nota": 4.7},
    {"id": "105", "nombre": "Luis Torres", "edad": 22, "nota": 3.0}
]

# Función para buscar un estudiante por ID (búsqueda exacta)
def buscar_estudiante_por_id(id_busqueda):
    for est in estudiantes:
        if est["id"] == id_busqueda:
            return est
    return None

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    print("\n--- Agregar Estudiante ---")
    id_nuevo = input("Ingrese el ID del estudiante: ")

    # Validar que el ID sea único
    if buscar_estudiante_por_id(id_nuevo):
        print("Error: Ya existe un estudiante con ese ID.")
        return

    nombre = input("Ingrese el nombre completo: ")
    try:
        edad = int(input("Ingrese la edad: "))
        if edad <= 0:
            print("Error: La edad debe ser un número positivo.")
            return
        nota = float(input("Ingrese la nota (0.0 - 5.0): "))
        if nota < 0.0 or nota > 5.0:
            print("Error: La nota debe estar entre 0.0 y 5.0.")
            return
    except ValueError:
        print("Error: Ingrese valores válidos.")
        return

    estudiantes.append({"id": id_nuevo, "nombre": nombre, "edad": edad, "nota": nota})
    print("Estudiante agregado exitosamente.")

# Función para buscar estudiantes por nombre (búsqueda parcial)
def buscar_estudiantes_por_nombre():
    nombre_busqueda = input("Ingrese el nombre o parte del nombre a buscar: ").lower()
    encontrados = [e for e in estudiantes if nombre_busqueda in e["nombre"].lower()]
    
    print("\n--- Resultados de la búsqueda ---")
    if encontrados:
        for e in encontrados:
            print(f"ID: {e['id']} | Nombre: {e['nombre']} | Edad: {e['edad']} | Nota: {e['nota']}")
    else:
        print("No se encontraron estudiantes con ese nombre.")

# Función para actualizar la edad o nota de un estudiante
def actualizar_estudiante():
    print("\n--- Actualizar Estudiante ---")
    id_est = input("Ingrese el ID del estudiante: ")
    est = buscar_estudiante_por_id(id_est)

    if est is None:
        print("Error: Estudiante no encontrado.")
        return

    print("¿Qué desea actualizar?")
    print("1. Edad")
    print("2. Nota")
    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        try:
            nueva_edad = int(input("Ingrese la nueva edad: "))
            if nueva_edad > 0:
                est["edad"] = nueva_edad
                print("Edad actualizada correctamente.")
            else:
                print("Error: La edad debe ser positiva.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    elif opcion == "2":
        try:
            nueva_nota = float(input("Ingrese la nueva nota: "))
            if 0.0 <= nueva_nota <= 5.0:
                est["nota"] = nueva_nota
                print("Nota actualizada correctamente.")
            else:
                print("Error: La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print("Opción no válida.")

# Función para eliminar un estudiante
def eliminar_estudiante():
    print("\n--- Eliminar Estudiante ---")
    id_est = input("Ingrese el ID del estudiante a eliminar: ")
    est = buscar_estudiante_por_id(id_est)

    if est:
        estudiantes.remove(est)
        print("Estudiante eliminado exitosamente.")
    else:
        print("Error: Estudiante no encontrado.")

# Función para calcular el promedio de notas
def calcular_promedio():
    if estudiantes:
        suma = sum(e["nota"] for e in estudiantes)
        promedio = suma / len(estudiantes)
        print(f"\nEl promedio de notas es: {promedio:.2f}")
    else:
        print("No hay estudiantes registrados.")

# Función para listar estudiantes con nota inferior a un umbral
def listar_inferiores(umbral=3.0):
    print(f"\n--- Estudiantes con nota menor a {umbral} ---")
    inferiores = [e for e in estudiantes if e["nota"] < umbral]
    
    if inferiores:
        for e in inferiores:
            print(f"ID: {e['id']} | Nombre: {e['nombre']} | Nota: {e['nota']}")
    else:
        print("No hay estudiantes con nota inferior al umbral.")

# Menú principal del programa
while True:
    print("\n===== Sistema de Estudiantes =====")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante por ID")
    print("3. Buscar estudiante por nombre")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Calcular promedio de notas")
    print("7. Listar estudiantes con nota inferior a 3.0")
    print("8. Salir")

    opcion = input("Seleccione una opción (1-8): ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        id_busqueda = input("Ingrese el ID del estudiante: ")
        estudiante = buscar_estudiante_por_id(id_busqueda)
        if estudiante:
            print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']} | Edad: {estudiante['edad']} | Nota: {estudiante['nota']}")
        else:
            print("Estudiante no encontrado.")
    elif opcion == "3":
        buscar_estudiantes_por_nombre()
    elif opcion == "4":
        actualizar_estudiante()
    elif opcion == "5":
        eliminar_estudiante()
    elif opcion == "6":
        calcular_promedio()
    elif opcion == "7":
        listar_inferiores()
    elif opcion == "8":
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
