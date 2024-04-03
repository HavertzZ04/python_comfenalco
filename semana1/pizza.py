pi = 3.1416

def calcular_area_pizza(diametro):
    radio = diametro / 2
    area = pi * (radio ** 2)
    return area

# Diametro pizzas por centimetros
diametro_pequena = 25
diametro_mediana = 30
diametro_grande = 45

# Calculamos el are total de cada pedido
area_opcion1 = 3 * calcular_area_pizza(diametro_pequena)
area_opcion2 = 2 * calcular_area_pizza(diametro_mediana)
area_opcion3 = calcular_area_pizza(diametro_grande)

# Comparamos las areas totales
if area_opcion1 > area_opcion2 and area_opcion1 > area_opcion3:
    print("Pedir 3 pizzas pequeñas proporcionaría la mayor cantidad de pizza.")
elif area_opcion2 > area_opcion1 and area_opcion2 > area_opcion3:
    print("Pedir 2 pizzas medianas proporcionaría la mayor cantidad de pizza.")
else:
    print("Pedir 1 pizza grande) proporcionaría la mayor cantidad de pizza.")


