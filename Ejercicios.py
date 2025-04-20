#Crea un programa que pida el nombre de una película y el año de estreno, luego muestre cuántos años han pasado desde su estreno
#movie = input("Introduce el nomrbe de la película: ")
#year = int(input("Introduce el año de estreno: "))
#current_year = 2025
#years_passed = current_year - year
#print(f"Han pasado {years_passed} años desde el estreno de {movie}.")
#Escribe un programa que solicite un número y muestre su doble y su mitad
#number = int(input("Introduce un número entero:"))
#double = number * 2
#half = number / 2
#print(f"El doble del numero seleccionado es {double} y su mitad es {half}")
#Crea una calculadora que pida dos números y muestre la suma, resta, multiplicación y división de ambos.
#number1 = int(input("Introduce el primer número: "))
#number2 = int(input("Introduce el segundo número: "))
#suma = number1 + number2
#resta = number1 - number2
#multiplicacion = number1 * number2
#division = number1 / number2
#print(f"La suma de {number1} y {number2} es {suma}, su resta es {resta}, su multiplicación es {multiplicacion} y su división es {division}.")
#Conversor de tiempo que pida una cantidad de segundos y la convierta a horas, minutos y segundos
#segundos_totales = int(input("Ingresa una cantidad de segundos: "))
#horas = segundos_totales // 3600
#minutos = (segundos_totales % 3600) // 60
#segundos = segundos_totales % 60
#print(f"{segundos_totales} segundos son {horas} horas, {minutos} minutos y {segundos} segundos.")
#Escribe un programa que determine si un número ingresado por el usuario es par o impar.
#num = int(input("Introduce un número entero: "))
#if num %2 == 0:
#    print(f"{num} es un número par.")
#else:
#    print(f"{num} es un número impar.")
#Edad del usuario y muestre un mensaje diferente para rangos: niño (0-12), adolescente (13-17), adulto (18-64), adulto mayor(65+)
age = int(input("Introduce tu edad: "))

while age < 0:
    print("Edad no válida. Por favor, introduce una edad válida.")
    age = int(input("Introduce tu edad: "))

if age <= 12:
    print("You are a child.")
elif age <= 17:
    print("You are a teenager.")
elif age <= 64:
    print("You are an adult.")
else:
    print("You are a senior.")
   