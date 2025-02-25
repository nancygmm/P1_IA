import pygame
import sys
from maze import Maze

ROSA = (255, 182, 193)
LILA = (216, 191, 216)
CELESTE = (173, 216, 230)
MENTA = (152, 255, 152)
FRESA = (255, 105, 180)
BLANCO = (255, 250, 250)
MORADO = (186, 85, 211)
GRIS_CLARO = (230, 230, 250)

TAM_CELDA = 30

def dibujar_laberinto(pantalla, maze, solucion=None):
    filas, columnas = len(maze.grid), len(maze.grid[0])
    for fila in range(filas):
        for columna in range(columnas):
            x, y = columna * TAM_CELDA, fila * TAM_CELDA
            if maze.grid[fila][columna] == "#":
                pygame.draw.rect(pantalla, MORADO, (x, y, TAM_CELDA, TAM_CELDA))  
            elif maze.grid[fila][columna] == "S":
                pygame.draw.rect(pantalla, FRESA, (x, y, TAM_CELDA, TAM_CELDA)) 
            elif maze.grid[fila][columna] == "E":
                pygame.draw.rect(pantalla, MENTA, (x, y, TAM_CELDA, TAM_CELDA))  
            else:
                pygame.draw.rect(pantalla, BLANCO, (x, y, TAM_CELDA, TAM_CELDA)) 
                pygame.draw.rect(pantalla, GRIS_CLARO, (x, y, TAM_CELDA, TAM_CELDA), 1)  

    if solucion:
        for fila, columna in solucion:
            x, y = columna * TAM_CELDA, fila * TAM_CELDA
            pygame.draw.rect(pantalla, CELESTE, (x, y, TAM_CELDA, TAM_CELDA))  

def iniciar_interfaz(maze, solucion):
    pygame.init()
    filas, columnas = len(maze.grid), len(maze.grid[0])
    ancho, alto = columnas * TAM_CELDA, filas * TAM_CELDA

    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("🌸 Laberinto Girlie 🌸")

    corriendo = True
    while corriendo:
        pantalla.fill(ROSA)  
        dibujar_laberinto(pantalla, maze, solucion)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()
