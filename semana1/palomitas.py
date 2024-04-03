pi = 3.1416

def calcular_volumen_cilindro(radio, altura):
    volumen = pi * (radio ** 2) * altura
    return volumen

def calcular_volumen_rectangular(largo, ancho, alto):
    volumen = largo * ancho * alto
    return volumen

def calcular_volumen_cono(radio, altura):
    volumen = (1/3) * pi * (radio ** 2) * altura
    return volumen

# Dimensiones de los empaques en centímetros
diametro_cilindro = 8
altura_cilindro = 15

largo_rectangular = 12
ancho_rectangular = 8
alto_rectangular = 10

radio_cono = 6
altura_cono = 12

# Calculamos el volumen total para cada  empaque
volumen_total_cilindro = calcular_volumen_cilindro((diametro_cilindro / 2), altura_cilindro)
volumen_total_rectangular = calcular_volumen_rectangular(largo_rectangular, ancho_rectangular, alto_rectangular)
volumen_total_cono = calcular_volumen_cono(radio_cono, altura_cono)

# Comparamos los volúmenes totales
if volumen_total_cilindro > volumen_total_rectangular and volumen_total_cilindro > volumen_total_cono:
    print("El empaque cilíndrico es la mejor opcion.")
elif volumen_total_rectangular > volumen_total_cilindro and volumen_total_rectangular > volumen_total_cono:
    print("El empaque rectangular es la mejor opcion.")
else:
    print("El empaque con forma de cono es la mejor opcion.")
