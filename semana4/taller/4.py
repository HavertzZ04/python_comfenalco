#Escribe un programa que imprima un patrón de numeros en forma de piramide

def numbers_pyramid(rows):
    for i in range(1):
        for j in range(rows + 1):
            print(str(j) * j)
            
numbers_pyramid(9)