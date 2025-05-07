#Desarrollar programa en python que permita calcular los beneficios en becas de alimentacion
#pide dos datos, promedio final de la nota del curso y el decil al que pertenece
#primero se debe definir el decil
money = 0
print("Bienvenido")
print("Ingrese el número de opción que corresponda a su decil")
print("1. Primer Decil")
print("2. Segundo Decil")
print("3. Tercer Decil")
print("4. Cuarto Decil")
print("5. Quinto Decil")
print("6. Sexto Decil")
print("7. Séptimo Decil")
print("8. Octavo Decil")
print("9. Noveno Decil")
print("10. Décimo Decil")
answer_decil = int(input("Ingrese el decil al que pertenece (1-10): "))
grade = float(input("Coloque su promdeio de notas de enseñanza media: "))
if (grade > 6.5) and (answer_decil == 1 or answer_decil == 2):
    money = 200000
    print(f"Le corresponde una beca de ${money}")
elif (grade > 6.5) and (answer_decil == 3 or answer_decil == 4):
    money = 150000
    print(f"Le corresponde una beca de ${money}")
elif (grade > 5.5 and grade <= 6.5) and (answer_decil == 1 or answer_decil == 2):
    money = 120000
    print(f"Le corresponde una beca de ${money}")
elif (grade > 5.5 and grade <= 6.5) and (answer_decil == 3 or answer_decil == 4):
    money = 100000
    print(f"Le corresponde una beca de ${money}")
else:
    print("")

if (answer_decil == 1 or answer_decil == 2 or answer_decil == 3):
    bono = 50000
    if grade >= 6.0:
        bono += 30000
print(f"Por lo cual la beca tiene un aumento a {bono + money}")