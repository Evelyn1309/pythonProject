# Declaracion de variables enteras
print("sueldos de este mes")
uni_dim1 = [["300", "400", "50", "60", "40", "80"]]

for a in list(uni_dim1):
    print(a)

# Declare variables flot
print("calificaciones de alex")
uni_dim2 = [["4.5", "8.6", "9.5", "7.8", "10.0", "5.5"]]
for i in list(uni_dim2):
    print(i)

# Declare  variables de textos
print("meses del año en ingles ")
uni_dim3 = [[" January", " February", " March", "April", " May", "June"]]
for i in list(uni_dim3):
    print(i)

# Declare  valores de enteros, flotantes y texto
print("La estudiante es :")
uni_dim4 = [["NOMBRE:Evelyn Arce", "Edad:", 18, "Nota:", 8.9, "Semestre:", 1]]
for i in list(uni_dim4):
    print(i)

# Declare 2 variables bidimensionales enteras 2x3
print("variables bidimensionales enteras 2x3")
dos_dim1 = [
    [26, 45, 80],
    [80, 20, 30]
]
for i in range(len(dos_dim1)):
    for j in range(len(dos_dim1[i])):
        print(dos_dim1[i][j])

dos_dim2 = [
    [80, 75, 50],
    [40, 20, 90]
]
for i in range(len(dos_dim2)):
    for j in range(len(dos_dim2[i])):
        print(dos_dim2[i][j])

# Declare 2 variables bidimensionales 2x3
print("variables bidimensionales float 2x3")
dos_dim3 = [
    [8.8, 9.0, 8.8],
    [7.8, 6.2, 3.4]
]
for i in list(dos_dim3):
    print(i)

dos_dim4 = [
    [8.8, 9.0, 8.8],
    [7.8, 6.2, 3.4]
]

for i in range(len(dos_dim4)):
    for j in range(len(dos_dim4[i])):
        print(dos_dim4[i][j])

# Declare 2 variables  texto
print("variables bidimensionales de texto")
dos_dim5 = [
    [" Maria", "Mara", "Macarena"],
    ["Mario", "Montalvo", "Moises"]
]
for i in range(len(dos_dim5)):
    for j in range(len(dos_dim5[i])):
        print(dos_dim5[i][j])

dos_dim6 = [
    [" Denis", "Carlos", "Camilo"],
    ["Marco", "Camila", "Moi"]
]
for i in range(len(dos_dim6)):
    for j in range(len(dos_dim6[i])):
        print(dos_dim6[i][j])

# Declare 2 variables bidimensionales 2x3 y asignar valores de enteros, flotantes y texto
print("variables bidimensionales combinadas")
dos_dim7 = [
    [80, 8.5, "Mario4.5"],
    ["Carlos", 100, 10.5]
]
for i in range(len(dos_dim7)):
    for j in range(len(dos_dim7[i])):
        print(dos_dim7[i][j])
dos_dim8 = [
    ["Denis", 45, 40.45],
    ["Marco", 45, "Camila"]
]
for i in range(len(dos_dim8)):
    for j in range(len(dos_dim8[i])):
        print(dos_dim8[i][j])

#  Declare 2 variables tridimensionales 2x3x2 y asigne valores enteros
print("variables tridimensionales enteros")
tri_dim1 = [
    [
        [1, 2, 3],
        [5, 6, 7],
    ],
    [
        [13, 14],
        [17, 18],
        [21, 22]
    ]
]

for fila in range(len(tri_dim1)):
    for columna in range(len(tri_dim1)):
        for pagina in range(len(tri_dim1[fila][columna])):
            print(tri_dim1)

tri_dim2 = [
    [
        [45, 50, 80],
        [50, 50, 40]
    ],
    [
        [20, 50, 50],
        [10, 40, 70]
    ]
]
for fila in range(len(tri_dim2)):
    for columna in range(len(tri_dim2)):
        for pagina in range(len(tri_dim2[fila][columna])):
            print(tri_dim2[fila][columna][pagina])

#  Declare 2 variables tridimensionales 2x3x3 y asigne valores de texto
print("variables tridimensionales de texto")
tri_dim3 = [
    [
        ["LUNES", "MIERCOLES", "JUEVES"],
        ["VIERNES", "SABADO", "DOMINGO"],
    ],
    [
        ["LUNES", "NU", "SE"],
        ["MIERCOLES", "WE", "E"],
    ],
    [
        ["LUNES", "NU", "SE"],
        ["VIERNES", "SABADO", "DOMINGO"]
    ]
]
for fila in range(len(tri_dim3)):
    for columna in range(len(tri_dim3)):
        for pagina in range(len(tri_dim3[fila])):
            print(tri_dim3)

tri_dim4 = [
    [
        ["DICIEMBRE", "VENUS", "JUEVES"],
        ["MARZO", "SABADO", "ENERO"]
    ],
    [
        ["DICIEMBRE", "GY", "UJ"],
        ["MARZO", "YU", "TE"],
    ],
    [
        ["ENERO", "HU", "JI"],
        ["MARZO", "SABADO", "ENERO"]
    ]
]
for i in range(len(tri_dim4)):
    for col in range(len(tri_dim4)):
        for pagina in range(len(tri_dim4)):
            print(tri_dim4)

#  Declare 2 variables tridimensionales 2x3x1 y asigne valores de Float
print("variables tridimensionales 2x3x1 y asigne valores de Float")
tri_dim5 = [
    [
        [8.5, 5.2, 20.3],
        [20.1, 45.12, 45.6]
    ]
]
for i in range(len(tri_dim5)):
    for j in range(len(tri_dim5[i])):
        print(tri_dim5[i][j])
# Declare 2 variables tridimensionales 2x3x2 asignar valores de enteros, flotantes y texto
print("variables tridimensionales 2x3x2 asignar valores de enteros, flotantes y texto")
tri_dim6 = [
    [
        ["arroz", 3, "lib", "marca chavelita"],
        [9.8, "Evelyn", 3]
    ],
    [
        ["tiene", 5.5, "dolares"],
        ["azucar", 6, "dolares"]
    ]
]
for fila in range(len(tri_dim6)):
    for columna in range(len(tri_dim6)):
        for pagina in range(len(tri_dim6[fila][columna])):
            print(tri_dim6[fila][columna][pagina])
