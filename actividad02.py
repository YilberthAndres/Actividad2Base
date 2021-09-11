
from library.mod_limpiar import *
from library.mod_menu import *

class Persona():

    def __init__(self):
        self.__perso = {}
        self.__listarPersona = []

    def agregarPersona(self, cedula, nombre, apellidos,telefono):
        self.__perso = {
            'cedula': cedula,
            'nombre': nombre,
            'apellidos': apellidos,
            'telefono': telefono, 
        }

        self.__listarPersona.append(self.__perso)

    def mostrarPersona(self):
      #print(self.__listarPersona, '/n')

     for i in self.__listarPersona:
         print(i)


def ingresoDato():
  p1 = Persona()
  cont = True
  while(cont):
    ce = input("Ingrese la cedula: ")
    no = input("Ingrese el nombre: ")
    ap = input("Ingrese el apellido: ")
    te = int(input("Ingrese el telefono: "))

    p1.agregarPersona(ce, no, ap, te)

    salir = input("Desea seguir agregando personas s/n: ")
    salir = salir.lower()

    if(salir == "s"):
      cont = True
    else:
      cont = False
    limpiar_pantalla()

  p1.mostrarPersona()


def inicio():
  opciones()



if __name__ == "__main__":
    limpiar_pantalla()
    inicio()
