import pygame
import sys

ROSA = (255, 182, 193)
LILA = (216, 191, 216)
CELESTE = (173, 216, 230)
MENTA = (152, 255, 152)
FRESA = (255, 105, 180)
BLANCO = (255, 250, 250)
MORADO = (186, 85, 211)
GRIS_CLARO = (230, 230, 250)
NEGRO = (0, 0, 0)

ANCHO, ALTO = 800, 600

class Interfaz:
    def __init__(self, maze, algoritmos, heuristicas):
        self.maze = maze
        self.algoritmos = algoritmos
        self.heuristicas = heuristicas
        self.algoritmo_seleccionado = None
        self.heuristica_seleccionada = None

        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Laberinto")

        self.fuente = pygame.font.Font(None, 30)
        self.fuente_titulo = pygame.font.Font(None, 36)

        self.botones_algoritmos = []
        self.botones_heuristicas = []

        self.boton_resolver = pygame.Rect(300, 400, 200, 50)
        self.mensaje_error = ""

        self.crear_botones()

    def crear_botones(self):
        x_alg, y_alg = 50, 100
        for algoritmo in self.algoritmos.keys():
            boton = pygame.Rect(x_alg, y_alg, 200, 40)
            self.botones_algoritmos.append((boton, algoritmo))
            y_alg += 50

        x_heu, y_heu = 300, 100
        for heuristica in self.heuristicas.keys():
            boton = pygame.Rect(x_heu, y_heu, 200, 40)
            self.botones_heuristicas.append((boton, heuristica))
            y_heu += 50

    def dibujar_botones(self):
        titulo_alg = self.fuente_titulo.render("Algoritmos de Búsqueda", True, NEGRO)
        self.pantalla.blit(titulo_alg, (50, 50))

        titulo_heu = self.fuente_titulo.render("Heurísticas", True, NEGRO)
        self.pantalla.blit(titulo_heu, (300, 50))

        for boton, texto in self.botones_algoritmos:
            color = FRESA if self.algoritmo_seleccionado == texto else LILA
            pygame.draw.rect(self.pantalla, color, boton)
            text_surface = self.fuente.render(texto, True, BLANCO)
            self.pantalla.blit(text_surface, (boton.x + 10, boton.y + 10))

        for boton, texto in self.botones_heuristicas:
            color = MENTA if self.heuristica_seleccionada == texto else CELESTE
            pygame.draw.rect(self.pantalla, color, boton)
            text_surface = self.fuente.render(texto, True, BLANCO)
            self.pantalla.blit(text_surface, (boton.x + 10, boton.y + 10))

        color_resolver = MORADO if self.algoritmo_seleccionado and self.heuristica_seleccionada else GRIS_CLARO
        pygame.draw.rect(self.pantalla, color_resolver, self.boton_resolver)
        texto_resolver = self.fuente.render("Resolver", True, BLANCO)
        self.pantalla.blit(texto_resolver, (self.boton_resolver.x + 50, self.boton_resolver.y + 15))

        if self.mensaje_error:
            error_surface = self.fuente.render(self.mensaje_error, True, (255, 0, 0))
            self.pantalla.blit(error_surface, (250, 470))

    def ejecutar(self):
        corriendo = True
        while corriendo:
            self.pantalla.fill(ROSA)
            self.dibujar_botones()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = evento.pos
                    for boton, algoritmo in self.botones_algoritmos:
                        if boton.collidepoint(x, y):
                            self.algoritmo_seleccionado = algoritmo
                            print(f"-> Algoritmo seleccionado: {algoritmo}")

                    for boton, heuristica in self.botones_heuristicas:
                        if boton.collidepoint(x, y):
                            self.heuristica_seleccionada = heuristica
                            print(f"-> Heurística seleccionada: {heuristica}")

                    if self.boton_resolver.collidepoint(x, y):
                        if self.algoritmo_seleccionado and self.heuristica_seleccionada:
                            print(f"... Resolviendo con {self.algoritmo_seleccionado} y heurística {self.heuristica_seleccionada}...")
                            self.mensaje_error = ""
                        else:
                            self.mensaje_error = "Debes seleccionar un algoritmo y una heurística."

            pygame.display.flip()

        pygame.quit()
        sys.exit()
import pygame
import time
from main import cargar_laberinto, ejecutar_algoritmos, encontrar_posiciones

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

TAM_CELDA = 5

def dibujar_laberinto(screen, laberinto, camino_actual=None):
    screen.fill(BLANCO)
    filas, columnas = laberinto.shape
    for x in range(filas):
        for y in range(columnas):
            color = BLANCO
            if laberinto[x, y] == '1':
                color = NEGRO
            elif laberinto[x, y] == '2':
                color = VERDE
            elif laberinto[x, y] == '3':
                color = ROJO
            pygame.draw.rect(screen, color, (y * TAM_CELDA, x * TAM_CELDA, TAM_CELDA, TAM_CELDA))
    if camino_actual:
        for x, y in camino_actual:
            pygame.draw.rect(screen, AZUL, (y * TAM_CELDA, x * TAM_CELDA, TAM_CELDA, TAM_CELDA))
    pygame.display.flip()

def visualizar_algoritmo(laberinto, algoritmo, inicio, meta):
    pygame.init()
    filas, columnas = laberinto.shape
    screen = pygame.display.set_mode((columnas * TAM_CELDA, filas * TAM_CELDA))
    pygame.display.set_caption(f"Visualización - {algoritmo}")
    camino, _, _ = resultados[algoritmo]
    for i in range(len(camino)):
        dibujar_laberinto(screen, laberinto, camino[:i+1])
        time.sleep(0.01)
    pygame.time.delay(2000)
    pygame.quit()

if __name__ == "__main__":
    laberinto = cargar_laberinto("laberinto.txt")
    inicio = encontrar_posiciones(laberinto, '2')[0]
    meta = encontrar_posiciones(laberinto, '3')[0]
    resultados = ejecutar_algoritmos(laberinto, inicio, meta)
    for algoritmo in resultados:
        visualizar_algoritmo(laberinto, algoritmo, inicio, meta)
