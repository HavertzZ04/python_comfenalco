#Escribe un programa que imprima un patrón de asteriscos

def character_loop(rows):
    stars = "*"
    for i in range(rows + 1):
        print(stars * i)
    
character_loop(10)
