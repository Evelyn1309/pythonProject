num = [
    [23, 50, 45],
    [26, 60, 100],
    [22, 40, 10]
]
valor_bus= 100
if any(valor_bus in fila for fila in num):
    print(f"se encontro {valor_bus} en la matriz")
else:
    print(f"{valor_bus} no se encontro ")

lista1 = [
    [23, 50, 45],
    [26, 60, 100],
    [60, 70, 40]
]

#proyecto2
def particionado(lista1):
    pivot = lista1[0]
    menor = []
    mayor = []
    for i in range(len(lista1)):
        if lista1[i] < pivot:
            menor.append(lista1[i])
        else:
            mayor.append(lista1[i])


def quicksort(lista2):
    if len(lista2) < 2:
        return lista2
    particionado(lista2)


print(quicksort())
