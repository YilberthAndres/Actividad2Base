from library.mod_limpiar import *


def opciones():
    op = 0
    
   
    while(op < 1 or op > 3):
        print("             ACTIVIDAD 2        ")
        print("")
        print("")
        print("1............Menu Personas.")
        print("2............Menu Empleados.")
        print("3............Salir.")
        print("")
        op = int(input("Que opcion elijes: "))
        print("")

        if(op < 1 or op > 3):
            print("Por favor elija una opcion entre 1 y 3")

    if (op == 1):
        limpiar_pantalla()
        op = 0
        while(op < 1 or op > 3):
            print("             MENU PERSONAS        ")
            print("")
            print("")
            print("1............Agregar Persona.")
            print("2............Eliminar Persona.")
            print("3............Mostrar Personas")
            print("4............Salir")
            print("")
            op = int(input("Que opcion elijes: "))
            print("")

            if(op < 1 or op > 3):
                print("Por favor elija una opcion entre 1 y 3")

    if (op == 2):
        limpiar_pantalla()
        op = 0
        while(op < 1 or op > 3):
            print("             MENU EMPLEADOS       ")
            print("")
            print("")
            print("1............Agregar Empleado.")
            print("2............Eliminar Empleado.")
            print("3............Mostrar Empleados.")
            print("4............Salir.")
            print("")
            op = int(input("Que opcion elijes: "))
            print("")

            if(op < 1 or op > 3):
                print("Por favor elija una opcion entre 1 y 3")

