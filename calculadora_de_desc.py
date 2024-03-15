def calcular_descuento(monto, porcentaje_des=10):  # Definicion de parametros
    desc = monto * (porcentaje_des / 100)  # la formula para resolver
    return desc


# resultado
monto = 400  # El total de la compra
descuento = calcular_descuento(monto)  # Calcula el descuento
print("su compra es de ", monto)  # Inprime el valor de comprs
print("El descuento es:", descuento)  # Imprime el total de descuento
