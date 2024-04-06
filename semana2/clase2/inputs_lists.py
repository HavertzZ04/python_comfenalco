"""
Crea un programa en python que permita al usuario ingresar datos utilizando la funcion input()
"""

def input_numbers():
    number = int(input("Enter a number: "))
    numbers_list.append(number)
    print()
    
    answer = (input(
    """Wanna add another one?
    1. YES
    2. NO
    your answer here: """))
    
    if answer == "1" or answer.upper() == "YES":
        input_numbers()
    else:
        print("tysm!")  
        
        
def calculate_average(list):
    sum_total = 0
    for i in list:
        sum_total += i
    print(f"The are {len(list)} numbers on the list and the average is: {sum_total / len(list)}")
        
        
def calculate_factorial():
    n = int(input("Enter a number to find the factorial: "))
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is: {fact}")
    
    
def calculate_vocals():
    vocals = 0
    text = input("Type something... ")
    for i in text.lower():
        if i in ["a", "e", "i", "o", "u"]:
            vocals += i
    print(f"There are: {vocals} vocals in the string")
    
    
def name_characters():
    name = input("What's your name? ")
    print(f"Your name has {len(name)} characters")
        
        
def multiplication_table():
    number = int(input("Type any number you want: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {i * number}")
        i += 1


def number_escale():
    number = int(input("Type a number: "))
    for i in range(2, 10, 1):
        print(f"{i} x {number} = {i * number}")
        number *= i
                
    for i in range(9, 1, -1):
        print(f"{i} / {number} = {int(number / i)}")
        number /= i
            
    
    
numbers_list = []

#input_numbers()
#calculate_average(numbers_list)
#calculate_factorial()

#calculate_vocals()
#name_characters()

#multiplication_table()
#number_escale()



