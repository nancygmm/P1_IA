import os

def cargar_laberinto(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), "P1", "Laberintos", nombre_archivo)
    with open(ruta, 'r') as archivo:
        laberinto = [list(linea.strip()) for linea in archivo.readlines()]
    return laberinto
