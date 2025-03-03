import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
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

def ejecutar_seleccion(algoritmo):
    laberinto = cargar_laberinto("Laberinto1.txt")
    inicio = encontrar_posiciones(laberinto, '2')
    meta = encontrar_posiciones(laberinto, '3')
    
    if not inicio or not meta:
        messagebox.showerror("Error", "No se encontraron los puntos de inicio o meta en el laberinto.")
        return
    
    inicio, meta = inicio[0], meta[0]
    resultados = ejecutar_algoritmos(laberinto, inicio, meta)
    
    if algoritmo in resultados:
        camino, explorados, tiempo = resultados[algoritmo]
        mensaje = f"{algoritmo}:\nNodos explorados: {explorados}\nTiempo: {tiempo:.4f}s"
        messagebox.showinfo("Resultados", mensaje)
        if camino:
            dibujar_recorrido(laberinto, camino, f"Recorrido - {algoritmo}")
        else:
            messagebox.showinfo("Sin solución", f"{algoritmo} no encontró una solución.")
    else:
        messagebox.showerror("Error", "Algoritmo no válido.")

def crear_interfaz():
    root = tk.Tk()
    root.title("Seleccionar Algoritmo")
    
    tk.Label(root, text="Seleccione un algoritmo para ejecutar:").pack(pady=10)
    
    algoritmos = ["BFS", "DFS", "A*_Manhattan", "A*_Euclidiana", "Greedy_Manhattan", "Greedy_Euclidiana"]
    for alg in algoritmos:
        tk.Button(root, text=alg, command=lambda a=alg: ejecutar_seleccion(a)).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    crear_interfaz()
