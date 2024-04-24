#Este codigo imprime un hijo de seleccionar le elemnto diferente dentro de un tabla
import random 

def dimentions(func):
    def wrapper():
        dimention = int(input("Enter a number for the table dimentions: "))
        letter1 = input("Select the first character: ")
        letter2 = input("Select the second character: ")
        print("")
        
        func(dimention, letter1, letter2)
    return wrapper


def exit_question(func):
    def wrapper(dimention, letter1, letter2):
        while True:
            func(dimention, letter1, letter2)
            print("1. Continue")
            print("2. Exit.")
            
            answer = input("\nYour answer here: ")
                
            if answer == "2":
                print("Thank you!")
                break
    return wrapper



@dimentions
@exit_question
def table_game(dimention, letter1, letter2):
    table = []
    
    table = [i for i in (letter1 * ((dimention * dimention) - 1))]
    table.insert(random.randint(0, len(table) -1), letter2)
    
    for i in range(dimention):
        print(table[i*dimention:(i+1)*dimention])
        
        
    location_list = table.index(letter2)
    location_h = (location_list // dimention) + 1
    location_v = (location_list % dimention) + 1
        
        
    while True:
        answer_h = int(input("\nPosicion horizontal: "))
        answer_v = int(input("Posicion vertical: "))
        
        if answer_h == location_h and answer_v == location_v:
            print("\nGanaste \n")
            break
        else:
            print("\nIntentalo Nuevamente")      

table_game()

    
