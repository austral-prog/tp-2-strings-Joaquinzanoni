def ficha():
    # 1. Lectura de datos
    nombre = input()
    email = input()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    # 2. Procesamiento dinámico
    nombre_limpio = nombre.strip().title()
    email_lower = email.lower()
    caracteres = len(nombre_limpio)

    # Buscamos dónde está el espacio para separar nombre de apellido
    espacio = nombre_limpio.find(" ")

    # Iniciales: Primera letra y la letra después del espacio
    iniciales = nombre_limpio[0] + nombre_limpio[espacio + 1]

    # Usuario: apellido.nombre (usando el índice del espacio)
    apellido = nombre_limpio[espacio + 1:].lower()
    nombre_solo = nombre_limpio[:espacio].lower()
    usuario = f"{apellido}.{nombre_solo}"

    # Email: Validar y extraer dominio dinámicamente
    email_valido = "@" in email_lower
    arroba = email_lower.find("@")
    dominio = email_lower[arroba + 1:]  # Desde después del @ hasta el final

    # Otros datos
    nombre_archivo = nombre_limpio.replace(" ", "_")
    cantidad_a = nombre_limpio.lower().count("a")
    codigo = nombre_limpio[::-1].upper()

    # Cálculos matemáticos
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3
    separador = "=" * 24

    # 3. Salida por pantalla (Ojo con los espacios exactos en FICHA DEL ALUMNO)
    print(separador)
    print("    FICHA DEL ALUMNO")  # Fíjate que hay 4 espacios antes de FICHA
    print(separador)
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_lower}")
    print(f"Caracteres en nombre: {caracteres}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {email_valido}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_archivo}")
    print(f"Cantidad de a: {cantidad_a}")
    print(f"Codigo secreto: {codigo}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print(separador)