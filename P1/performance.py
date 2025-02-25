import time
from algoritmos_busqueda import bfs, dfs, a_star, greedy
from heuristicas import manhattan, euclidean

def medir_tiempo(algoritmo, maze, heuristic=None):
    inicio = time.time()
    if heuristic:
        resultado = algoritmo(maze, heuristic)
    else:
        resultado = algoritmo(maze)
    fin = time.time()
    tiempo_total = fin - inicio
    return tiempo_total, resultado

def evaluar_algoritmos(maze):
    tiempos = {}

    tiempos["BFS"] = medir_tiempo(bfs, maze)
    tiempos["DFS"] = medir_tiempo(dfs, maze)
    tiempos["A* (Manhattan)"] = medir_tiempo(a_star, maze, manhattan)
    tiempos["A* (Euclidean)"] = medir_tiempo(a_star, maze, euclidean)
    tiempos["Greedy (Manhattan)"] = medir_tiempo(greedy, maze, manhattan)
    tiempos["Greedy (Euclidean)"] = medir_tiempo(greedy, maze, euclidean)

    return tiempos

def imprimir_resultados(tiempos):
    for algoritmo, (tiempo, resultado) in tiempos.items():
        print(f"{algoritmo}: {tiempo:.6f} segundos, pasos: {len(resultado) if resultado else 'No encontrado'}")
