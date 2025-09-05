
# Realizado por: Evelin Perlaza

# Ciudades, días y semanas
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 2

# Matriz 3D: temperaturas[ciudad][semana][día]
# Datos de ejemplo: temperaturas reales aproximadas para dos semanas

temperaturas = [
    [   # Quito (clima templado)
        [14, 15, 16, 14, 15, 17, 16],  # Semana 1
        [15, 16, 17, 15, 16, 18, 17]   # Semana 2
    ],
    [   # Guayaquil (clima cálido)
        [28, 29, 30, 31, 29, 30, 32],  # Semana 1
        [29, 30, 31, 32, 30, 31, 33]   # Semana 2
    ],
    [   # Cuenca (clima frío)
        [11, 12, 13, 12, 14, 13, 12],  # Semana 1
        [12, 13, 14, 13, 15, 14, 13]   # Semana 2
    ]
]

# Mostrar matriz completa
print("=== Registro de temperaturas diarias ===")
for i in range(len(ciudades)):
    print(f"\nCiudad: {ciudades[i]}")
    for j in range(num_semanas):
        print(f"  Semana {j+1}: {temperaturas[i][j]}")

# Calcular y mostrar promedios
print("\n=== Promedios de temperatura por ciudad y semana ===")
for i in range(len(ciudades)):  # Ciudades
    print(f"\nPromedios de {ciudades[i]}:")
    for j in range(num_semanas):  # Semanas
        suma = 0
        for k in range(len(dias)):  # Días
            suma += temperaturas[i][j][k]
        promedio = suma / len(dias)
        print(f"  Semana {j+1}: {promedio:.2f} °C")

