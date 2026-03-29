def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y eltotal."""

    precio= int(input())
    descuento = float(input())
    cantidad = int(input())

    precio_des = precio - descuento
    total= precio_des * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_des}")
    print(f"Total: {total}")

casting()


