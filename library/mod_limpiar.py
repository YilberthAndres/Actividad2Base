import platform
import os
import time

def limpiar_pantalla():
    time.sleep(0.2)

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')