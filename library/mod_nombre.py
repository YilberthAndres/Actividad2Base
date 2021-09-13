from library.mod_limpiar import *
from library.class_desarrollo import *

E1 = Desarrolloo()

def cargar():
    amig = {}
    continua = "s"
    print("-------------------------------")
    print("---- AGREGAR A UNA PERSONA ----")
    # archivo = open("library/base.csv","a")
    while continua == "s":
        no = input("ingrese su nombre por favor: ")
        print("-----------------------------------")
        ap = input("ingrese su apellido por favor: ")
        print("-----------------------------------")
        tel = input("ingrese su telefono por favor: ")
        print("-----------------------------------")
        cod = input("ingrese su codigo por favor: ")
        print("-----------------------------------")
        continua = input("desea continuar s/n:  ")
        print(continua)
        E1.datosguardados(no,ap,tel,cod)
        limpiar_pantalla()
    return amig
    
def mostrarr():
    E1.mostraspersonas()
    
def eliminar():
    E1.eliminarpersona()


