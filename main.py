import time
import heapq
import random
from queue import Queue, LifoQueue
import numpy as np

def cargar_laberinto(archivo):
    with open(archivo, 'r') as f:
        laberinto = [list(line.strip().replace(',', '')) for line in f.readlines()]
    return np.array(laberinto)

def encontrar_posiciones(laberinto, valor):
    return list(zip(*np.where(laberinto == valor)))

def movimientos_validos(laberinto, pos):
    filas, columnas = laberinto.shape
    x, y = pos
    movimientos = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
    return [(nx, ny) for nx, ny in movimientos if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx, ny] != '1']

def bfs(laberinto, inicio, meta):
    queue = Queue()
    queue.put((inicio, [inicio]))
    visitados = set()
    nodos_explorados = 0
    
    while not queue.empty():
        actual, camino = queue.get()
        if actual in visitados:
            continue
        visitados.add(actual)
        nodos_explorados += 1
        if actual == meta:
            return camino, nodos_explorados, len(camino)
        for vecino in movimientos_validos(laberinto, actual):
            queue.put((vecino, camino + [vecino]))
    return None, nodos_explorados, 0

def dfs(laberinto, inicio, meta):
    stack = LifoQueue()
    stack.put((inicio, [inicio]))
    visitados = set()
    nodos_explorados = 0
    
    while not stack.empty():
        actual, camino = stack.get()
        if actual in visitados:
            continue
        visitados.add(actual)
        nodos_explorados += 1
        if actual == meta:
            return camino, nodos_explorados, len(camino)
        for vecino in movimientos_validos(laberinto, actual):
            stack.put((vecino, camino + [vecino]))
    return None, nodos_explorados, 0

def greedy(laberinto, inicio, meta, heuristica):
    pq = []
    heapq.heappush(pq, (heuristica(inicio, meta), inicio, [inicio]))
    visitados = set()
    nodos_explorados = 0
    
    while pq:
        _, actual, camino = heapq.heappop(pq)
        if actual in visitados:
            continue
        visitados.add(actual)
        nodos_explorados += 1
        if actual == meta:
            return camino, nodos_explorados, len(camino)
        for vecino in movimientos_validos(laberinto, actual):
            heapq.heappush(pq, (heuristica(vecino, meta), vecino, camino + [vecino]))
    return None, nodos_explorados, 0

def a_star(laberinto, inicio, meta, heuristica):
    pq = []
    heapq.heappush(pq, (0, inicio, [inicio]))
    visitados = {}
    nodos_explorados = 0
    
    while pq:
        _, actual, camino = heapq.heappop(pq)
        if actual in visitados:
            continue
        visitados[actual] = True
        nodos_explorados += 1
        if actual == meta:
            return camino, nodos_explorados, len(camino)
        for vecino in movimientos_validos(laberinto, actual):
            costo = len(camino) + heuristica(vecino, meta)
            heapq.heappush(pq, (costo, vecino, camino + [vecino]))
    return None, nodos_explorados, 0

def heuristica_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def heuristica_euclidiana(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def elegir_punto_aleatorio(laberinto):
    caminos = encontrar_posiciones(laberinto, '0')
    return random.choice(caminos) if caminos else None

def ejecutar_algoritmos(laberinto, inicio, meta):
    resultados = {}
    for nombre, funcion in [('BFS', bfs), ('DFS', dfs)]:
        inicio_tiempo = time.time()
        camino, explorados, largo_camino = funcion(laberinto, inicio, meta)
        tiempo = time.time() - inicio_tiempo
        resultados[nombre] = (camino, explorados, tiempo, largo_camino)
    for nombre, heuristica in [('A*_Manhattan', heuristica_manhattan), ('A*_Euclidiana', heuristica_euclidiana)]:
        inicio_tiempo = time.time()
        camino, explorados, largo_camino = a_star(laberinto, inicio, meta, heuristica)
        tiempo = time.time() - inicio_tiempo
        resultados[nombre] = (camino, explorados, tiempo, largo_camino)
    for nombre, heuristica in [('Greedy_Manhattan', heuristica_manhattan), ('Greedy_Euclidiana', heuristica_euclidiana)]:
        inicio_tiempo = time.time()
        camino, explorados, largo_camino = greedy(laberinto, inicio, meta, heuristica)
        tiempo = time.time() - inicio_tiempo
        resultados[nombre] = (camino, explorados, tiempo, largo_camino)
    return resultados

def ejecutar_algoritmos_y_mostrar(laberinto, inicio, meta, caso):
    print(f"\n{caso}:")
    resultados = ejecutar_algoritmos(laberinto, inicio, meta)
    for nombre, (camino, explorados, tiempo, largo_camino) in resultados.items():
        print(f"{nombre}: Nodos explorados: {explorados}, Tiempo: {tiempo:.4f}s, Largo del camino: {largo_camino}")

if __name__ == "__main__":
    laberinto = cargar_laberinto("Laberinto1.txt")
    
    inicio_base = encontrar_posiciones(laberinto, '2')[0]
    meta_base = encontrar_posiciones(laberinto, '3')[0]
    ejecutar_algoritmos_y_mostrar(laberinto, inicio_base, meta_base, "Caso Base")
    
    inicio_aleatorio = elegir_punto_aleatorio(laberinto)
    meta_aleatorio = elegir_punto_aleatorio(laberinto)
    if inicio_aleatorio and meta_aleatorio:
        ejecutar_algoritmos_y_mostrar(laberinto, inicio_aleatorio, meta_aleatorio, "Caso Aleatorio")
    else:
        print("No se encontraron puntos de inicio y meta válidos en el laberinto para el caso aleatorio.")
