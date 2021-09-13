from library.mod_limpiar import *

class Desarrolloo():
    def __init__(self):
        self.__personas = {}
        self.__listapersonas = []
    

    def datosguardados(self,nombre, apellido, telefono, codigo):
        self.__listapersonas.append([nombre, apellido, telefono, codigo])
    
    def mostraspersonas(self):
        for i in self.__listapersonas:
            print(f"Nombre: {i[0]} Apellido: {i[1]} Telefono: {i[2]} Codigo: {i[3]} ")


    
    def eliminarpersona(self):
        borrar = False
        borrar = input("Ingrese el numero de codigo a borrar:  ")
        for i in self.__listapersonas:
            if(borrar == i[3]):
                self.__listapersonas.remove(i)
                borrar = True
                input("Fue borrado exitosamente, pulse cualquier tecla")
                limpiar_pantalla()