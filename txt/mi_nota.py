# En esta tarea, realizarás operaciones de lectura y escritura en archivos de texto en Python. Sigue las instrucciones
# detalladas a continuación:
mis_notas = open("my_notes.txt", "r")  # definimos la variable y le pedimos que abra el archivo de texto para leer
print(mis_notas)  # imprimir la variable
linea = mis_notas.readlines()  # lee line a linea
print(linea)  # imprime las lineas
mis_notas.close()  # cierra el archivo
