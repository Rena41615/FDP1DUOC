#programa de numeros y sumatoria
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))
contador_pares = 0
contador_impares = 0
#detectar si los numeros son  pares o impares
if num1 % 2 == 0:
    contador_pares += 1
else:
    contador_impares += 1
if num2 % 2 == 0:
    contador_pares += 1
else:
    contador_impares += 1
if num3 % 2 == 0:
    contador_pares += 1
else:
    contador_impares += 1
#expresar contadores
print(f"Se ingresaron {contador_pares} numeros pares")
print(f"Se ingresaron {contador_impares} numeros impares")
#sumar los tres numeros ingresados
suma = num1 + num2 + num3
if suma > 100:
    print("La suma de los numeros ingresados es mayor a 100")
else: 
    print("La suma de los numeros ingresados es menor a 100")
#verificar si la suma es par o impar
if suma % 2 == 0:
    print("La suma de los numeros ingresados es par")
else:
    print("La suma de los numeros ingresados es impar")