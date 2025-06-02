verificador = 0
contador_primos = 0
contador_primosnt = 0
print("Verificador de numeros primos")

def es_primo(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

rango = int(input("Ingrese cuantos numeros desea verificar: "))

while verificador < rango:
    num = int(input("Ingrese un numero: "))
    if es_primo(num):
        print(f"El número {num} es primo")
    else:
        print("El numero no es primo o no válido")
print("Ya se verificaron todos los numeros")