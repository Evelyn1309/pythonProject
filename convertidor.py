# Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo. La
# función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.


def tempe_prome(datos, ciudad, semana_inicial, semana_final):
    suma_temp = 0  # Variable para almacenar la suma de las temperaturas
    num_items = 0  # Variable para almacenar el total de items
    for i in range(len(datos[ciudad])):  # se ve el rango y la lonhitud
        if i >= semana_inicial and i <= semana_final:  # se verifica que este dentro del rango
            for j in range(len(datos[ciudad][i])):  # Iteratua sobre los días de la semana
                temp_dia = datos[ciudad][i][j]['temp']  # Obtiene  cada una de las temperaturas del día
                suma_temp += temp_dia  # La Suma  de la temperatura al total
                num_items += 1  # Incrementa  el contador de items
                print(datos[ciudad][i][j])  # Imprimesion de datos

    promedio = suma_temp / num_items  # Calcula el promedio de temperaturas
    return promedio


tempe = (
    (
        [  # Semana 1
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Lunes", "temp": 26},
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Martes", "temp": 80},
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Miércoles", "temp": 45},
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Jueves", "temp": 40},
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Viernes", "temp": 35},
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Sábado", "temp": 38},
            {"CIUDAD": "Quito", "semana": "Semana 1", "dia": "Domingo", "temp": 92}
        ],

        [  # Semana 2
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Lunes", "temp": 78},
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Martes", "temp": 80},
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Miércoles", "temp": 82},
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Jueves", "temp": 79},
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Viernes", "temp": 85},
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Sábado", "temp": 88},
            {"CIUDAD": "Quito", "semana": "Semana 2", "dia": "Domingo", "temp": 92}
        ],

        [  # Semana 3
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Lunes", "temp": 70},
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Martes", "temp": 45},
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Miércoles", "temp": 22},
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Jueves", "temp": 19},
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Viernes", "temp": 35},
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Sábado", "temp": 18},
            {"CIUDAD": "Quito", "semana": "Semana 3", "dia": "Domingo", "temp": 52}
        ],

        [  # Semana 4
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Lunes", "temp": 28},
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Martes", "temp": 20},
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Miércoles", "temp": 82},
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Jueves", "temp": 0},
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Viernes", "temp": 5},
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Sábado", "temp": 8},
            {"CIUDAD": "Quito", "semana": "Semana 4", "dia": "Domingo", "temp": 32}
        ]
    ),

    [  # Ciudad 2
        [  # Semana 1
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Lunes-semana 1", "temp": 8},
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Martes-semana 1", "temp": 0},
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Miércoles-semana 1", "temp": 12},
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Jueves-semana 1", "temp": 29},
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Viernes-semana 1", "temp": 35},
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Sábado-semana 1", "temp": 78},
            {"CIUDAD": "Ibarra", "semana": "Semana 1", "dia": "Domingo-semana 1", "temp": 62}
        ],

        [  # Semana 2
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Lunes-semana 2", "temp": 68},
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Martes-semana 2", "temp": 80},
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Miércoles-semana 2", "temp": 92},
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Jueves-semana 2", "temp": 29},
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Viernes-semana 2", "temp": 65},
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Sábado-semana 2", "temp": 98},
            {"CIUDAD": "Ibarra", "semana": "Semana 2", "dia": "Domingo-semana 2", "temp": 22}
        ],

        [  # Semana 3
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Lunes-semana 3", "temp": 68},
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Martes-semana 3", "temp": 60},
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Miércoles-semana 3", "temp": 22},
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Jueves-semana 3", "temp": 19},
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Viernes-semana 3", "temp": 35},
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Sábado-semana 3", "temp": 48},
            {"CIUDAD": "Ibarra", "semana": "Semana 3", "dia": "Domingo-semana 3", "temp": 42}
        ],
        [  # Semana 4
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Lunes", "temp": 88},
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Martes", "temp": 7},
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Miércoles", "temp": 92},
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Jueves", "temp": 49},
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Viernes", "temp": 15},
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Sábado", "temp": 18},
            {"CIUDAD": "Ibarra", "semana": "Semana 4", "dia": "Domingo", "temp": 22}
        ]
    ],
    [  # Ciudad 3
        [  # Semana 1
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Lunes", "temp": 98},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Martes", "temp": 20},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Miércoles", "temp": 32},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Jueves", "temp": 59},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Viernes", "temp": 45},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Sábado", "temp": 38},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 1", "dia": "Domingo", "temp": 92}
        ],
        [  # Semana 2
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Lunes", "temp": 58},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Martes", "temp": 60},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Miércoles", "temp": 52},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Jueves", "temp": 29},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Viernes", "temp": 25},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Sábado", "temp": 38},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 2", "dia": "Domingo", "temp": 32}
        ],
        [  # Semana 3
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Lunes", "temp": 68},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Martes", "temp": 20},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Miércoles", "temp": 32},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Jueves", "temp": 39},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Viernes", "temp": 25},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Sábado", "temp": 28},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 3", "dia": "Domingo", "temp": 52}
        ],
        [  # Semana 4
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Lunes", "temp": 38},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Martes", "temp": 10},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Miércoles", "temp": 62},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Jueves", "temp": 39},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Viernes", "temp": 35},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Sábado", "temp": 28},
            {"CIUDAD": "Esmeraldas", "semana": "Semana 4", "dia": "Domingo", "temp": 32}
        ]
    ]
)
# Seleccion de la ciudad
ciudad = int(input("Ingrese el número de la ciudad : "))

# Selecciona las semanas inicial y final
semana_inicial = int(input("Ingrese el número de la semana inicial: "))
semana_final = int(input("Ingrese el número de la semana final: "))

promedio_cal = tempe_prome(tempe, ciudad, semana_inicial, semana_final)
print("El promedio de temperaturas es:", promedio_cal)
