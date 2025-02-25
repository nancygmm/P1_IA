import os

def cargar_laberinto(nombre_archivo):
    ruta = os.path.join(os.path.dirname(__file__), "Laberintos", nombre_archivo)
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")
    
    with open(ruta, 'r') as archivo:
        laberinto = [list(linea.strip()) for linea in archivo.readlines()]
    return laberinto
