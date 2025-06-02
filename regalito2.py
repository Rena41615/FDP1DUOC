#Tengo: if, listas, while, try, except
num_list = []

print("MENÚ PRINCIPAL")
print("1.- Ingresar número")
print("2.- Mostrar mayor")
print("3.- Mostrar menor")
print("4.- Salir")
answer = int(input("Seleccione una opción: "))
if answer == 1:
    while True:
        try: #Valida todo
            num1 = int(input("Ingrese un número el 1 al 100: "))
            if 1 <= num1 <= 100:
                num_list.appends(num1)
                print(f"Ha ingresado el número {num1}")
                break
        except ValueError:
            print("No ingrese caracteres")
if answer == 2:
    print("")