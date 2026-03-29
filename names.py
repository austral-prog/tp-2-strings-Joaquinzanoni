def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input('ingrese su nombre : ')
    apellido= input("ingrese su apellido: ")
    nya = nombre +' '+ apellido

    print(nya. lower())
    print(nya. title())
    print(nya. upper())
    print("\t" + nya)

names()