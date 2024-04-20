#Escribe un programa que imprima un patrón de asteriscos

def character_loop(rows):
    stars = "*"
    for i in range(1):
        for j in range(rows + 1):
            print(stars * j)
    
character_loop(10)