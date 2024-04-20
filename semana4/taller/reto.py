import random 

def dimentions(func):
    def wrapper():
        dimention = int(input("Enter a number for the table dimentions: "))
        letter1 = input("Select the first character: ")
        letter2 = input("Select the second character: ")
        print("")
        
        func(dimention, letter1, letter2)
    return wrapper


@dimentions
def table_game(dimention, letter1, letter2):
    table = []
    
    table = [i for i in (letter1 * ((dimention * dimention) - 1))]
    table.insert(random.randint(0, len(table) -1), letter2)
    
    for i in range(dimention):
        print(table[:dimention])
        del table[:dimention]
    
    
table_game()