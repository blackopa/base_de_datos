from insert import *
from query import *
def menu_inicial():
    print("Base de datos personaje de rol \n")
    print("Escoja una opcion:")
    print("1. Ingresar")
    print("2. Registrarse")
    print("0. Salir")
    x = int(input())
    switcher = {
        1: ingresar_user,
        2: create_user,
        0: terminar
    }
    func = switcher.get(x, lambda: "Entrada no valida")
    func()
def create_user():#from insert.py
    print("Ingresar datos")
    print("1.Rut sin digito verificador:")
    rut = input()
    print("2.nombre :")
    Nombre = input()
    print("3.Edad : ")
    edad = input()
    print("4.nickname :")
    nickname = input()
    print("5.direccion :")
    direccion = input()
    print("6.game master Yes= 1 ; No=0:")
    if(input()==1 or input()==Yes):

            game_master=True

    else:

        game_master=False

    print("7.pasword :")
    password = input()
    insert_Usuarios(rut,Nombre,edad,nickname,direccion, Game_master, password)
    print("Registrado, volviendo a menu ")
def ingresar_user():
    print("rut sin digito verificador")
    rut=input()
    varificar=query_3(rut)
    menu_query()
    print("password")
    password=input()
    if(verificar==password):

            func = switcher.get(menu_usuario(rut), lambda: "Entrada no valida")
            func()

def menu_usuario(rut):
    print("menu usuario \n")
    print("Escoja una opcion:")
    print("1. crear personaje")
    print("2. ver personajes")
    print("0. Salir")
    x = int(input())
    switcher = {
        1: crear_personaje(rut),
        2: ver_personaje(rut),
        0: terminar
    }
    func = switcher.get(x, lambda: "Entrada no valida")
    func()

def ver_persona(rut):
    query_see_pj(rut)

    main_query()



#def crear_personaje(rut):#from insert.py
#    print("Ingresar datos")
#    print("1.Nombre:")
#    nombre = input()
#    print("2.Rut Usuario :")
#    rut = input()
#    print("Raza  ")
#    print("Escoja una opcion:")
#    print("1. Enano de las colinas")
#    print("3. Alto Elfo")
#    print("4. Elfo de los Bosques")
#    print("5. Elfo oscuro")
#    print("6. piesligero")
#    print("7.Fornido")
#    print("8. humano")
#    print("9. linaje")
#    print("10. gnomos de los bosques")
#    print("11. gnomos de las rocas")
#    print("12.de dos mundos ")
#    print("13.grums")
#    print("14.infernal")
#    Raza = input()
#    print("clase  ")
#    print("Escoja una opcion:")
#    print("1. Barbaro")
#    print("2. Bardo")
#    print("3. Brujo ")
#    print("4. Clerigo")
#    print("5. Druida")
#    print("6. Explorador")
#    print("7. Guerrero")
#    print("8. Hechicero")
#    print("9. Mago")
#    print("10. Monje")
#    print("11. Paladin")
#    print("12. Picaro ")
#    Clase = input()
#
#    print("7.pasword :")
#    password = input()
#    insert_Usuarios(rut,Nombre,edad,nickname,direccion, Game_master, password)
#    print("Registrado, volviendo a menu ")
