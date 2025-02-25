import math

def distancia_manhattan(nodo1, nodo2):
    return abs(nodo1[0] - nodo2[0]) + abs(nodo1[1] - nodo2[1])

def distancia_euclidea(nodo1, nodo2):
    return ((nodo1[0] - nodo2[0]) ** 2 + (nodo1[1] - nodo2[1]) ** 2) ** 0.5

