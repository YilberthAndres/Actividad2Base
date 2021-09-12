from library.mod_limpiar import limpiar_pantalla


class Empleado():

    def __init__(self):
        self.__Emplead = {}
        self.__listarEmpleado = []

    def agregarEmpleado(self, cedula, nombre, apellido,telefono, sueldo):

        self.__listarEmpleado.append([cedula, nombre, apellido,telefono,sueldo])

    def mostrarEmpleado(self):
      #print(self.__listarPersona, '/n')
        
        for i in self.__listarEmpleado:
           print(f"El empleado de nombre {i[1]} {i[2]} con cedula {i[0]} y telefono {i[3]} gana {i[4]}")
           print("")
        
        input(f"Prescione cualquier tecla para continuar...")

        limpiar_pantalla()
           

    def borrarEmpleado(self):
        borre = False
        borrar = input("Escriba la cedula del usuario que desea eliminar: ")
        for i in self.__listarEmpleado:

            if(borrar == i[0]):
                self.__listarEmpleado.remove(i)
                borre = True
                input(f"Borrado empleado de cedula {borrar} prescione cualquier tecla para continuar...")
                limpiar_pantalla()
            else:
                borre = False

        if(borre == False):
            input(f"El empleado de cedula {borrar} no esta reguistrado prescione cualquier tecla para continuar...")
            limpiar_pantalla()
        #self.__listarEmpleado.pop