def change():
    # El test espera exactamente este mensaje
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero_recibido = float(input())
    print(int(dinero_recibido))

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    # Líneas vacías y etiquetas exactas
    print("")  # Línea vacía
    print("Vuelto")
    print("")  # Otra línea vacía
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)