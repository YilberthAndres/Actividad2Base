

def cargar():
    amig = {}
    continua = "s"
    print("-------------------------------")
    print("---- AGREGAR A UNA PERSONA ----")
    # archivo = open("library/base.csv","a")
    while continua == "s":
        nombre = input("ingrese su nombre por favor ---> ")
        apellido = input("ingrese su apellido por favor --> ")
        telefono = input("ingrese su telefono por favor --> ")
        codigo = input("ingrese su codigo por favor --> ")
        amig[codigo] = (nombre, apellido)
        continua = input("desea continuar s/n  ")
        print(continua)
    return amig


