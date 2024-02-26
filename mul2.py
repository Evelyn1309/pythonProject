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
