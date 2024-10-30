from datetime import datetime

# Variables
usuarios = {
    "admin": {"password": "admin", "role": "administrador"},
    "chaustre": {"password": "chaustre", "role": "operario"},
    "usuario": {"password": "usuario", "role": "usuario"},
}
listafinal = []

# Función para verificar los roles de los usuarios
def obtener_rol(usuario):
    if usuario in usuarios:
        return usuarios[usuario]["role"]
    return None

def ingresar_datos():
    print("\nSolicitar datos al cliente\n")
    nombre = input("Ingrese el nombre del cliente: ")
    
    while True:
        cedula = input("Ingrese la cédula (mínimo 8 dígitos): ")
        if cedula.isdigit() and len(cedula) >= 8:
            cedula = int(cedula)
            break
        else:
            print("Cédula inválida. Debe ser un número positivo y tener al menos 8 dígitos.")

    while True:
        fecha = input("Ingrese la fecha en el formato dd/mm/aaaa: ")
        try:
            dia, mes, año = map(int, fecha.split('/'))
            if 1 <= dia <= 30 and 1 <= mes <= 12 and año >= 2024:
                break
            else:
                print("Fecha inválida. Asegúrese de que el día, mes y año sean correctos.")
        except ValueError:
            print("Formato de fecha inválido. Debe ser dd/mm/aaaa.")

    fecha_actual5 = datetime.now().strftime("%d/%m/%Y")
    print(fecha_actual5)

    hora_actual = datetime.now().strftime("%H:%M")
    print(f"Hora actual: {hora_actual}")

    while True:
        print("Seleccione una opción:\n")
        print("1) Instalación de software")
        print("2) Falla")
        print("3) Formateo")
        print("4) Venta")
        caso = input("Ingrese el número de la opción deseada: ")
        if caso in ["1", "2", "3", "4"]:
            break
        else:
            print("Opción inválida. Debe ser un número entre 1 y 4.")

    # Guardar datos
    cliente_data = {
        "nombre": nombre,
        "cedula": cedula,
        "fecha": fecha,
        "hora": hora_actual,
        "caso": caso
    }
    listafinal.append(cliente_data)
    print("Datos ingresados correctamente.\n")

def buscar_datos():
    if not listafinal:
        print("No hay datos para buscar.")
        return

    print("Opciones de búsqueda:")
    print("1) Buscar por mes ingresado")
    print("2) Buscar por nombre ingresado")
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        mes_buscar = input("Ingrese el mes (1-12) para buscar: ")
        if mes_buscar.isdigit() and 1 <= int(mes_buscar) <= 12:
            mes_buscar = int(mes_buscar)
            found = False
            for cliente in listafinal:
                if int(cliente["fecha"].split('/')[1]) == mes_buscar:
                    mostrar_datos(cliente)
                    found = True
            if not found:
                print("No se encontraron registros para el mes especificado.")
        else:
            print("Mes inválido.")

    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre del usuario: ")
        found = False
        for cliente in listafinal:
            if cliente["nombre"].lower() == nombre_buscar.lower():
                mostrar_datos(cliente)
                found = True
        if not found:
            print("No se encontraron registros para el nombre especificado.")
    else:
        print("Opción no válida.")

def mostrar_datos(cliente):
    print("Cliente:")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Cédula: {cliente['cedula']}")
    print(f"Fecha: {cliente['fecha']}")
    print(f"Hora: {cliente['hora']}")
    print(f"Caso: {cliente['caso']}")
    print("-" * 20)

# Función para verificar si un usuario es válido
def usuario_valido(usuario):
    return usuario in usuarios

# Nueva función para usuarios básicos
def funcion_basica():
    print("Función disponible solo para usuarios básicos.")

# Función para crear un nuevo usuario
def crear_usuario_funcion():
    print("\nCrear nuevo usuario\n")
    
    while True:
        nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ")
        if nuevo_usuario in usuarios:
            print("El usuario ya existe. Intente nuevamente.")
        else:
            break

    nueva_contraseña = input("Ingrese la contraseña para el nuevo usuario: ")

    while True:
        nuevo_rol = input("Ingrese el rol para el nuevo usuario (usuario/operario/administrador): ").lower()
        if nuevo_rol in ["usuario", "operario", "administrador"]:
            break
        else:
            print("Rol inválido. Debe ser usuario, operario o administrador.")

    # Agregar nuevo usuario al diccionario
    usuarios[nuevo_usuario] = {"password": nueva_contraseña, "role": nuevo_rol}
    print(f"Usuario {nuevo_usuario} creado con éxito.\n")

    # Opción para salir e iniciar sesión con el nuevo usuario
    while True:
        salir = input("¿Desea salir e iniciar sesión con el nuevo usuario? (s/n): ").lower()
        if salir == 's':
            iniciar_sesion_con_usuario(nuevo_usuario)
            break
        elif salir == 'n':
            print("Regresando al menú principal...")
            break
        else:
            print("Opción inválida. Por favor, ingrese 's' o 'n'.")

def iniciar_sesion_con_usuario(usuario):
    while True:
        contraseña = input("Ingrese contraseña: ")
        if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
            menu_principal(usuario)
            break
        else:
            print("Contraseña incorrecta. Intente nuevamente.")

# Menú principal con roles
def menu_principal(usuario):
    rol = obtener_rol(usuario)
    if rol is None:
        print("Usuario no encontrado.")
        return

    while True:
        print(f"\nBienvenido, {usuario}. Rol: {rol}")
        print("Seleccione una opción:\n")
        
        if rol == "administrador":
            print("1) Ingresar datos")
            print("2) Buscar datos")
            print("3) Crear usuario")
            print("4) Cambiar rol")
            print("5) Función de usuario básico")
            print("6) Salir")
        elif rol == "operario":
            print("1) Ingresar datos")
            print("2) Buscar datos")
            print("3) Salir")
        elif rol == "usuario":
            print("1) Función básica")
            print("2) Salir")

        opcion = input("Ingrese la opción deseada: \n")

        if rol == "administrador":
            if opcion == "1":
                ingresar_datos()
            elif opcion == "2":
                buscar_datos()
            elif opcion == "3":
                crear_usuario_funcion()
            elif opcion == "4":
                cambiar_rol()
            elif opcion == "5":
                funcion_basica()
            elif opcion == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")

        elif rol == "operario":
            if opcion == "1":
                ingresar_datos()
            elif opcion == "2":
                buscar_datos()
            elif opcion == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")

        elif rol == "usuario":
            if opcion == "1":
                funcion_basica()
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")

    # Regresar al inicio de sesión
    iniciar_sesion()

# Lógica de inicio de sesión
def iniciar_sesion():
    while True:
        usuario = input("\nIngrese usuario: ")
        contraseña = input("Ingrese contraseña: ")
        if usuario in usuarios and usuarios[usuario]["password"] == contraseña:
            menu_principal(usuario)
            break
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")

# Inicio del programa
iniciar_sesion()
