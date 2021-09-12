from library.mod_nombre import *
from library.mod_limpiar import *
from library.mod_empleados import *
from library.class_empleado import *



def opciones():
    op = 0
    
    E1 = Empleado()
    while(op < 1 or op > 3):
        print("----------- -----------")
        print("|     ACTIVIDAD 2     |")
        print("| 1  Menu Personas.   |")
        print("| 2  Menu Empleados.  |")
        print("| 3. Salir.           |")
        print("-----------------------")
        print("")
        op = int(input("Que opcion elijes: "))
        print("")

        if(op < 1 or op > 3):
            print("Por favor elija una opcion entre 1 y 3")

    if (op == 1):
        limpiar_pantalla()
        op = 0
        while(op < 1 or op > 3):
            print("------------------------")
            print("|     MENU PERSONAS    |")
            print("| 1. Agregar Persona.  |")
            print("| 2. Eliminar Persona. |")
            print("| 3. Mostrar Personas  |")
            print("| 4. Salir             |")
            print("------------------------")

            print("")
            op = int(input("Que opcion elijes: "))
            print("")

            if(op < 1 or op > 3):
                print("Por favor elija una opcion entre 1 y 3")
                          
            if(op == 1):
              op = 0
              cargar()
            if(op == 2):
              op = 0
              eliminar()
            if(op ==3):
              op = 0
              mostrarr()
        

        while(op < 1 or op > 3):
            limpiar_pantalla()
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

            if(op == 1): 
              op = 0
              proceso(1)
            if(op == 2):
              op = 0
              proceso(2)
            if(op == 3):
              op = 0
              proceso(3)
            