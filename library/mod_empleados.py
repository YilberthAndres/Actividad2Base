from library.class_empleado import *
from library.mod_limpiar import *

E1 = Empleado()

def proceso(op):
  
  cont = True

  if(op == 1):
      while(cont):
        print("")
        print("LLENAR DATOS DEL NUEVO EMPLEADO")
        print("")
        ce = input("Ingrese la cedula: "  )
        no = input("Ingrese el nombre: "  )
        ap = input("Ingrese el apellido: ")
        te = input("Ingrese el telefono: ")
        su = input("Ingrese el sueldo: ")

        E1.agregarEmpleado(ce, no, ap, te,su)

        salir = input("Desea seguir agregando empleados s/n: ")
        salir = salir.lower()

        if(salir == "s"):
          cont = True
        else:
          cont = False
        limpiar_pantalla()
  if(op == 2):
      E1.borrarEmpleado()
  if(op == 3):
      E1.mostrarEmpleado()