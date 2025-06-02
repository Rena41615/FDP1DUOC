def preguntar_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        print(f"Tu edad es {edad} años.")
    except ValueError:
        print("Debes agregar solo números.")