# 1. Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Evelin Perlaza",         # Nombre ficticio basado en ti
    "edad": 34,                         # Edad ficticia
    "ciudad": "Quito",                  # Ciudad inicial
    "profesion": "Estudiante de Derecho y TI"    # Profesión inicial
}

# 2. Acceder y modificar valores
# Cambiar la ciudad de "Quito" a "Sangolquí"
informacion_personal["ciudad"] = "Sangolquí"

# Modificar la clave "profesion"
informacion_personal["profesion"] = "Estudiante de Derecho y TI"

# 3. Verificar la existencia de la clave "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0962666820"  # Número ficticio

# 4. Eliminar la clave "edad"
del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print("Diccionario final con la información personal:")
print(informacion_personal)
