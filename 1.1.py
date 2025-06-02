#NO IA
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

while num1 > num2:
    print("El 1er numero debe ser menor que el 2do")
    num1 = int(input("Ingrese nuevamente el primer numero: "))
    num2 = int(input("Ingrese nuevamente el segundo numero: "))

punto_medio = (num1 + num2)/2
ajuste_numero_aleatorio = (num2 - num1)*0.2

if (num1 + num2)%2==0: #como pedia que no fuera completamente aleatorio lo hice así :v
    numero_adivinar = int(punto_medio + ajuste_numero_aleatorio)
else:
    numero_adivinar = int(punto_medio - ajuste_numero_aleatorio)

print("Adivina el numero")

intentos = 0
while intentos < 3:
    intento = int(input("Ingrese numero para adivinar: "))
    intentos += 1
    if intento == numero_adivinar:
        print("Ganaste")
        break
    if intento > numero_adivinar:
        print("El numero ingresado es mayor al correcto")
    if intento < numero_adivinar:
        print("El numero ingresado es menor al correcto")
if intentos == 3 and intento != numero_adivinar:
    print(f"Fallaste, el numero correcto era {numero_adivinar}")