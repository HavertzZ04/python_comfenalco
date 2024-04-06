"""
Crea un programa en python que permita al usuario ingresar datos utilizando la funcion input()
"""

def countdown():
    number = int(input("Enter a number to countdown: "))
    for i in range(number, 0, -1):
        print(i)
        
        
def repeat_greeting(n):
    greeting = input("Say hello: ")
    while n > 0:
        print(greeting)
        n -= 1
        
        
def sum_range(stop):
    total = sum(range(1, stop + 1))
    print(total)


def print_odd_numbers(stop):
    for i in range(1, stop + 1, 2): 
        print(i)

        
#countdown()
#repeat_greeting(3)
#sum_range(3)
#print_odd_numbers(9)



        
    
    