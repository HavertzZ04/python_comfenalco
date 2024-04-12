def print_numbers(start, end, steps=1):
    for i in range(start, end +1, steps):
        print(i)


def multiplication_table():
    number = int(input("Enter a number: ")) 
    for i in range(1, 11, 1):
        print(f"{number} x {i} = {i * number}")       
    
           
def exit_answer():
    answer = int(input("""
Do you wanna keep here?
    1. YES
    2. NO
    
Your answer here: """))
    print('')
    
    if answer == 1:
        menu()
    elif answer == 2:
        print("Thank you!!")
    else:
        print("This is not a valid answer -.-'")
        exit_answer()
    


def menu():  
    
    answer = int(input("""Choose something from this menu:
    1. To see numbers from 1 to 100
    2. to see even numbers up to n number
    3. To see odd numbers up to n number
    4. To see a multiplication table
    
    Your answer here: """))  
    
    if answer == 1:   
        print_numbers(1, 100)
        
    elif answer == 2:
        number = int(input("Enter a number: "))
        print_numbers(2, number, 2)
        
    elif answer == 3:
        number = int(input("Enter a number: "))
        print_numbers(1, number, 2)  
        
    elif answer == 4:
        multiplication_table()
        
    else:
        print("Invalidad answer")
    
    exit_answer()   
    
menu()

