# Tarea: Trabajo con Archivos de Texto en Python
# Universidad Estatal Amazónica
# Autor: Evelyn Perlaza

# ESCRITURA DE ARCHIVO DE TEXTO
archivo = open("my_notes.txt", "w")

archivo.write("Aprender Python me ayuda a desarrollar la lógica para resolver problemas.\n")
archivo.write("La programación me permite automatizar tareas que antes hacía manualmente.\n")
archivo.write("Comprender cómo funcionan los archivos facilita el manejo de información real.\n")

archivo.close()
print("Archivo 'my_notes.txt' creado y guardado correctamente.\n")

# LECTURA DE ARCHIVO DE TEXTO
archivo = open("my_notes.txt", "r")

print("=== Lectura del contenido del archivo 'my_notes.txt' ===\n")
linea = archivo.readline()
while linea:
    print(linea.strip())
    linea = archivo.readline()

archivo.close()
print("\nEl archivo 'my_notes.txt' fue cerrado exitosamente.")
