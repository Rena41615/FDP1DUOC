#Calculadora de promedio inicial
print("Calculadora de promedio inicial")
print("Debe ingresar las notas en este formato: 2.0, 3.5, 4.0, etc.")
print("La nota máxima es 7.0 y la mínima es 1.0")
nota_1 = float(input("Ingrese la nota 1: "))
if nota_1 < 1.0 or nota_1 > 7.0:
    print("La nota ingresada no es válida")
else:
    nota_2 = float(input("Ingrese la nota 2: "))
    if nota_2 < 1.0 or nota_2 > 7.0:
        print("La nota ingresada no es válida2")
    else:
        nota_3 = float(input("Ingrese la nota 3: "))
        if nota_3 < 1.0 or nota_3 > 7.0:
            print("La nota ingresada no es válida")
        else:
            print("Las notas ingresadas son válidas")


ponderacion_1 = nota_1 * 0.3
ponderacion_2 = nota_2 * 0.4
ponderacion_3 = nota_3 * 0.3

promedio_final = ponderacion_1 + ponderacion_2 + ponderacion_3
print(f"El promedio final es {promedio_final:.1f}")

#calculadora de promedio final

print("Ya tienes tu promedio inicial, este vale un 60% para la nota final de semestre")
print("El examen transversal vale un 40% para la nota final de semestre")
examen_transversal = float(input("Ingrese su nota del examen transversal: "))
if examen_transversal < 1.0 or examen_transversal > 7.0:
    print("La nota ingresada no es válida")
else:
    promedio_final_semestre = (promedio_final * 0.6) + (examen_transversal * 0.4)
    print(f"La nota final de semestre es {promedio_final_semestre:.1f}") 