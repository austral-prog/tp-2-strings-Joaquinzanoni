def names():
    # El test no quiere mensajes, solo los inputs
    nombre = input()
    apellido = input()
    nya = nombre + ' ' + apellido

    print(nya.lower())
    print(nya.title())
    print(nya.upper())
    # Corregido el error de los paréntesis y el .lower()
    print("\t" + nya.lower())