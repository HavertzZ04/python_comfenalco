def display_menu():
    user_menu = ["1. Numbers from 1 to N", "2. Even numbers", "3. Odd numbers"]   
    method_menu = [display_numbers, even_number, odd_number]

    print("\n<--------These are our options menu-------->\n")
    for option in user_menu:
        print(option)
    
    while True:                
        answer = int(input("\nSelect your option here: "))
        if 0 < answer < 4:
            method_menu[answer - 1]()
            break
        else:
            print("Please select a valid option (1 to 3).")


#Decorated Function
def display_exit(func):
    def wrapper():
        func()
        exit_menu = ["1. Go to the options menu", "2. Exit"]
    
        while True:
            print("\n<---Select the best option for you--->\n")
            for option in exit_menu:
                print(option)
            
            exit_answer = int(input("\nSelect your option here: "))   
            if exit_answer == 1:
                display_menu()
                break             
            elif exit_answer == 2:
                print("\nThank you!")
                break
            else:
                print("Please choose a valid option (1 or 2).")                  
     
    return wrapper
                 
    
#Decorated Function
def positive_number(func):
    def wrapper():
        while True:
            answer = int(input("Enter any number: "))
            if answer > 0:
                func(answer)
                break
            else:
                print("\nPlease enter a positive number.")           
                    
    return wrapper             
               
             
@display_exit                                          
@positive_number
def display_numbers(answer):
    print(f"\nNumbers from 1 to {answer}:")
    for i in range(1, answer + 1):
        print(i)
   
@display_exit                                                     
@positive_number
def even_number(answer):
    print(f"\Even numbers up to {answer}:")
    for i in range(2, answer + 1, 2):
        print(i)
          
@display_exit                                                       
@positive_number      
def odd_number(answer):
    print(f"\nOdd numbers up to {answer}:")
    for i in range(1, answer + 1, 2):
        print(i)


display_menu() #You only need to use this function and the program will work alone <3