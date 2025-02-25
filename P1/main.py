import pygame
from lectura import cargar_laberinto
from maze import Maze
from algoritmos_busqueda import bfs, dfs, a_star, greedy
from heuristicas import distancia_manhattan, distancia_euclidea
from interfaz import Interfaz
import performance

pygame.init()

def main():
    archivo_laberinto = "Laberinto1.txt"  
    laberinto_data = cargar_laberinto(archivo_laberinto)
    laberinto = Maze(laberinto_data)

    heuristicas = {
        "manhattan": distancia_manhattan,
        "euclidiana": distancia_euclidea
    }

    algoritmos = {
        "BFS": bfs,
        "DFS": dfs,
        "A*": a_star,
        "Greedy": greedy
    }

    interfaz = Interfaz(laberinto, algoritmos, heuristicas)
    interfaz.ejecutar()

if __name__ == "__main__":
    main()
