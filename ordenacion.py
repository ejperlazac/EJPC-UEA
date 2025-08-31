# Programa 2: Ordenación de una fila de la matriz con BubbleSort

# Definimos una matriz 3x3
matriz = [
    [9, 2, 7],
    [4, 8, 1],
    [6, 3, 5]
]

# Algoritmo de ordenación BubbleSort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Elegimos la fila 1 (segunda fila) para ordenar
fila_a_ordenar = 2

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
