import math

def distancia_manhattan(actual, objetivo):
    return abs(actual[0] - objetivo[0]) + abs(actual[1] - objetivo[1])

def distancia_euclidea(actual, objetivo):
    return math.sqrt((actual[0] - objetivo[0])**2 + (actual[1] - objetivo[1])**2)
