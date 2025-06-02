#Código funcional y bien hecho, pero con copilot. x
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

while num1 > num2:
    print("El primer número debe ser menor que el segundo número.")
    num1 = int(input("Ingrese nuevamente el primer número: "))
    num2 = int(input("Ingrese nuevamente el segundo número: "))

punto_medio = (num1 + num2) / 2
ajuste = (num2 - num1) * 0.2

if (num1 + num2) % 2 == 0:   
    numero_objetivo = int(punto_medio + ajuste)
else:
    numero_objetivo = int(punto_medio - ajuste)

print("Debe adivinar el número generado. Tiene 3 intentos.")

intentos = 0
while intentos < 3: 
    intento = int(input(f"Intento {intentos + 1}: Ingrese un número para adivinar: "))
    intentos += 1
    if intento == numero_objetivo:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif intento > numero_objetivo:
        print("El número ingresado es mayor que el correcto.")
    else:
        print("El número ingresado es menor que el correcto.")
    if intentos == 3 and intento != numero_objetivo:
        print(f"Lo siento, no adivinaste el número. El número correcto era {numero_objetivo}.")