# promedios.py

# Función para calcular el promedio de temperaturas por ciudad.
# Recibe un diccionario con las ciudades como claves y listas de temperaturas como valores.

def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros:
        temperaturas (dict): 
            - clave: nombre de la ciudad (str)
            - valor: lista de temperaturas (list de números)

    Retorna:
        dict: 
            - clave: nombre de la ciudad
            - valor: temperatura promedio (float) o None si no hay datos
    """
    promedios = {}  # Diccionario vacío para almacenar los resultados

    # Recorremos cada ciudad y su lista de temperaturas
    for ciudad, valores in temperaturas.items():
        # Si la lista está vacía, no hay promedio
        if len(valores) == 0:
            promedios[ciudad] = None
        else:
            # Promedio = suma de temperaturas dividido para la cantidad
            promedios[ciudad] = sum(valores) / len(valores)

    return promedios


# Ejemplo de uso de la función
if __name__ == "__main__":
    # Diccionario con temperaturas de distintas ciudades en varias semanas
    datos = {
        "Quito": [20, 22, 21, 19],
        "Guayaquil": [28, 30, 29, 27],
        "Cuenca": [18, 17, 19]
    }

    # Llamada a la función
    resultado = calcular_promedios(datos)

    # Mostrar los resultados en pantalla
    print("Promedios de temperaturas por ciudad:")
    for ciudad, promedio in resultado.items():
        if promedio is not None:
            print(f"{ciudad}: {promedio:.2f} °C")
        else:
            print(f"{ciudad}: No hay datos suficientes")