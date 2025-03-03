import matplotlib.pyplot as plt
import numpy as np
from main import cargar_laberinto, ejecutar_algoritmos, encontrar_posiciones, elegir_punto_aleatorio

def dibujar_recorrido(laberinto, camino, titulo):
    plt.figure(figsize=(8, 8))
    laberinto_mapa = np.where(laberinto == '1', 1, 0) 
    plt.imshow(laberinto_mapa, cmap='gray_r', origin='upper')
    
    if camino and len(camino) > 1:
        x, y = zip(*camino)
        plt.plot(y, x, marker='o', linestyle='-', color='blue', markersize=2)
    
    plt.title(titulo)
    plt.axis('off')
    plt.show(block=True)

def ejecutar_seleccion():
    opciones = ["Caso Base", "Caso Aleatorio"]
    print("Seleccione una opción:")
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    
    seleccion = input("Ingrese el número de la opción: ")
    
    try:
        seleccion = int(seleccion) - 1
        if seleccion < 0 or seleccion >= len(opciones):
            print("Selección no válida.")
            return
    except ValueError:
        print("Entrada no válida. Ingrese un número.")
        return
    
    laberinto = cargar_laberinto("Laberinto1.txt")
    
    if opciones[seleccion] == "Caso Base":
        inicio = encontrar_posiciones(laberinto, '2')[0]
        meta = encontrar_posiciones(laberinto, '3')[0]  
    else:
        inicio = elegir_punto_aleatorio(laberinto)
        meta = encontrar_posiciones(laberinto, '3')[0]  

    if not inicio or not meta:
        print("Error: No se encontraron puntos válidos en el laberinto.")
        return

    
    resultados = ejecutar_algoritmos(laberinto, inicio, meta)
    
    print(f"\n{opciones[seleccion]}:")
    for nombre, (camino, explorados, tiempo, largo_camino) in resultados.items():
        print(f"{nombre}: Nodos explorados: {explorados}, Tiempo: {tiempo:.4f}s, Largo del camino: {largo_camino}")
    
    print("\n¿Desea visualizar un recorrido en particular?")
    algoritmos = list(resultados.keys())
    for i, alg in enumerate(algoritmos):
        print(f"{i+1}. {alg}")
    
    seleccion_alg = input("Ingrese el número del algoritmo: ")
    
    try:
        seleccion_alg = int(seleccion_alg) - 1
        if seleccion_alg < 0 or seleccion_alg >= len(algoritmos):
            print("Selección no válida.")
            return
    except ValueError:
        print("Entrada no válida. Ingrese un número.")
        return
    
    algoritmo = algoritmos[seleccion_alg]
    camino, explorados, tiempo, largo_camino = resultados[algoritmo]
    if camino:
        dibujar_recorrido(laberinto, camino, f"Recorrido - {algoritmo}")
    else:
        print(f"{algoritmo} no encontró una solución.")

if __name__ == "__main__":
    ejecutar_seleccion()