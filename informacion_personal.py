# Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al
# menos las claves "nombre", "edad", "ciudad" y "profesion".

informacion_personal = {"nombre": "Evelyn", "edad": 18, "ciudad": "Esmeraldas", "profesion": "Estudiante"}

# Acceso a los datos y modifica
informacion_personal["ciudad"] = "Ibarra"

# Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Comerciante"

# Añadir un dato
if "telefono" not in informacion_personal:
    informacion_personal['Telefono'] = '0981204520'

# Eliminar la clave "edad"
if "ciudad" in informacion_personal:
    del informacion_personal['ciudad']

print('Informacion  Personal: ')
print(informacion_personal)
