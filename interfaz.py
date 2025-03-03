import matplotlib.pyplot as plt
import numpy as np
from main import cargar_laberinto, ejecutar_algoritmos, encontrar_posiciones

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
    algoritmos = ["BFS", "DFS", "A*_Manhattan", "A*_Euclidiana", "Greedy_Manhattan", "Greedy_Euclidiana"]
    print("Seleccione un algoritmo:")
    for i, alg in enumerate(algoritmos):
        print(f"{i+1}. {alg}")
    
    seleccion = input("Ingrese el número del algoritmo: ")
    
    try:
        seleccion = int(seleccion) - 1
        if seleccion < 0 or seleccion >= len(algoritmos):
            print("Selección no válida.")
            return
    except ValueError:
        print("Entrada no válida. Ingrese un número.")
        return
    
    algoritmo = algoritmos[seleccion]
    laberinto = cargar_laberinto("Laberinto1.txt")
    inicio = encontrar_posiciones(laberinto, '2')
    meta = encontrar_posiciones(laberinto, '3')
    
    if not inicio or not meta:
        print("Error: No se encontraron los puntos de inicio o meta en el laberinto.")
        return
    
    inicio, meta = inicio[0], meta[0]
    resultados = ejecutar_algoritmos(laberinto, inicio, meta)
    
    if algoritmo in resultados:
        camino, explorados, tiempo = resultados[algoritmo]
        print(f"{algoritmo}:\nNodos explorados: {explorados}\nTiempo: {tiempo:.4f}s")
        if camino:
            dibujar_recorrido(laberinto, camino, f"Recorrido - {algoritmo}")
        else:
            print(f"{algoritmo} no encontró una solución.")
    else:
        print("Error: Algoritmo no válido.")

if __name__ == "__main__":
    ejecutar_seleccion()
