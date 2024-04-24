#Escribe un programa que imprima un patrón de numeros en forma de piramide

def numbers_pyramid(rows):
    for i in range(rows + 1):
        print(str(i) * i)
            
numbers_pyramid(9)