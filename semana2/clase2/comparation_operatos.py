"""
Crea un programa en python que permita al usuario ingresar datos utilizando la funcion input()
"""

def comparate_numbers():
    n1 = int(input("Enter the first number here: "))
    n2 = int(input("Enter the second number here: "))
    
    if n1 == n2:
        print("The numbers are iqual")
    else:
        print("The numbers are different")
        

def greater_than():
    n1 = int(input("Enter the first number here: "))
    n2 = int(input("Enter the second number here: "))
    
    if n1 > n2:
        print(f"The number {n1} is greater than {n2}")
    elif n2 > n1:
        print(f"The numbers {n2} are greater than {n1}")
    else:
        print("The numbers are iqual")


def even_odd():
    number = int(input("Enter a number to see if this one is even or odd: "))
    
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")
        

def triangle_type():
    a = int(input("First side: "))
    b = int(input("Second side: "))
    c = int(input("Third side: "))
    # Check if this ia valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        print("This is not a triangle")
    
    if a == b == c:
        print("Equilateral Triangle")  # All sides are equal
    elif a == b or a == c or b == c:
        print("Isosceles Triangle")  # Two sides are equal
    else:
        print("Scalene Triangle")  # All sides are different
    
    
def can_retire():
    retirement_age = 65
    age = int(input("How old are you? "))
    
    if age >= retirement_age:
        print("You can retire!")
    else:
        print(f"You cannot retire yet. You need to wait {retirement_age - age} more years.")
    

def working_day():
    day = input("Type a day of week: ").capitalize()
    
    if day in ["Monday", "Tuesday", "Wendsday", "Thursday", "Friday"]:
        print(f"{day} is a working day")
    elif day in ["Saturday", "Sunday"]:
        print(f"{day} is a weekend day")
    else:
        print("This is not a day -_-'") 
    
#comparate_numbers()
#greater_than()
#even_odd()
#triangle_type()
#can_retire()
#working_day()


    