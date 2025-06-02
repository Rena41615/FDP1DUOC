abrir_menu = False
pokedex = False
equipo = False
mochila = False
guardar = False
volver = False


def pokedex(abrir_pokedex):
    if abrir_pokedex == True:
          print("Abrir pokedex")
    else:
        print("Pokedex cerrada")

def equipo(abrir_equipo):
    if abrir_equipo == True:
        equipo_pokemones = [
            {"nombre": "Pikachu", "tipo": "Eléctrico", "nivel": 25},
            {"nombre": "Charmander", "tipo": "Fuego", "nivel": 18},
            {"nombre": "Squirtle", "tipo": "Agua", "nivel": 16},
            {"nombre": "Charizard", "tipo": "Fuego", "nivel": 20},
            {"nombre": "Vaporeon", "tipo": "Agua", "nivel": 17}
        ]
        print("Tu equipo pokemón")
        for pokemon in equipo_pokemones:
            print(f"- {pokemon['nombre']} | Tipo: {pokemon['tipo']} | Nivel: {pokemon['nivel']}")
    else:
        print("Equipo cerrado")

def mochila(abrir_mochila):
    if abrir_mochila == True:
        print("Abrir mochila")
    else:
        print("Mochila cerrada")

def guardar(esta_guardando):
    if esta_guardando == True:
          print("Guardando progreso")
    else:
        print("Sin guardar")

def volver(volver_atras):
    if volver_atras == True:
          print("Volver")
    else:
        print("Mantenerse en ubicación actual")

def menuDos():
        print("Menú abierto")
        print("1. Pokedex")
        print("2. Equipo") #Equipo de 6 pokemones
        print("3. Mochila")
        print("4. Guardar")
        print("5. Volver")
        opcion_dentro_del_menu = int(input("Ingrese el número: "))
        if opcion_dentro_del_menu == 1:
            pokedex(True)
        if opcion_dentro_del_menu == 2:
            equipo(True)
        if opcion_dentro_del_menu == 3:
            mochila(True)
        if opcion_dentro_del_menu == 4:
            guardar(True)
        if opcion_dentro_del_menu == 5:
            volver(True)

def menu(opcion):
    global abrir_menu
    if opcion == 1:
        abrir_menu = True
        menuDos()
    if opcion == 2: #Pq no un else? porque defino que sucede en ambos casos
        abrir_menu = False #No solo si una opicon no es seleccionada
        print("Menú cerrado")
######################################################################
print("Bienvenid@ al menú de pokemón")
print("1. Abrir menú")
print("2. Cerrar menú")
opcion = int(input())
menu(opcion)