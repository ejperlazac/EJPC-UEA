# promedios.py

def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros:
    temperaturas (dict): claves = nombre de ciudad, valores = lista de temperaturas.

    Retorna:
    dict: claves = ciudad, valor = temperatura promedio.
    """
    promedios = {}
    for ciudad, valores in temperaturas.items():
        if len(valores) == 0:
            promedios[ciudad] = None
        else:
            promedios[ciudad] = sum(valores) / len(valores)
    return promedios


if __name__ == "__main__":
    # Ejemplo de uso
    datos = {
        "Quito": [20, 22, 19, 21],
        "Guayaquil": [28, 30, 27, 29],
        "Cuenca": [18, 19, 20, 17]
    }
    resultados = calcular_promedios(datos)
    print("Temperaturas promedio por ciudad:")
    for ciudad, promedio in resultados.items():
        if promedio is not None:
            print(f"{ciudad}: {promedio:.2f} °C")
        else:
            print(f"{ciudad}: No hay datos")
