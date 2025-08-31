# Programa 1: Búsqueda en Arreglo Multidimensional

# Definimos una matriz 3x3
matriz = [
    [4, 8, 15],
    [16, 23, 42],
    [10, 20, 30]
]

# Función para buscar un valor dentro de la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Ejemplo de prueba
valor_buscado = 42
print(buscar_valor(matriz, valor_buscado))
