while True: 
    entrada = input("Ingrese un número: ")
    if entrada.isdigit():
        numero = int(entrada)
        break
    else:
        print("Debe ingresar números válidos(enteros positivos)")

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"Los divisores de {numero} son:  {divisores}")

if len(divisores) == 2:
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")