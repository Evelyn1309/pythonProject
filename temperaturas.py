# Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión,
# puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.),
# y en la tercera dimensión, semanas.

tempe = [
    [
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
    ],

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
]

# lista completa
for fila in range(len(tempe)):
    for columna in range(len(tempe)):
        for pagina in range(len(tempe[fila][columna])):
            print(tempe[fila][columna][pagina])
# Calcular el promedio de temperaturas para cada ciudad y semana

for ciudad in tempe:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(tempe[0][0][0]["CIUDAD"])
        print("promedio de la semana", suma)
        print(tempe[1][0][0]["CIUDAD"])
        print("promedio de la semana", suma)
        print(tempe[2][0][0]["CIUDAD"])
        print("promedio de la semana", suma)
