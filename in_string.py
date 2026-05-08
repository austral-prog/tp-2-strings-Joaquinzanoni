def check_vowels():
    """
    Lee un nombre y verifica si contiene cada una de las vocales.
    """
    nombre = input().lower()

    print(f"Contiene a: {'a' in nombre}")
    print(f"Contiene e: {'e' in nombre}")
    print(f"Contiene i: {'i' in nombre}")
    print(f"Contiene o: {'o' in nombre}")
    print(f"Contiene u: {'u' in nombre}")

