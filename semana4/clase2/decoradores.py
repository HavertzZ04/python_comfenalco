def display_menu():
    user_menu = {
        1 : "1. Numbers from 1 to N",
        2 : "2. Even numbers",
        3 : "3. Odd numbers"
    }
       
    method_menu = {
        1 : display_numbers,
        2 : even_number,
        3 : odd_number
    }
   
    print("\n<---This is our numbers menu--->\n")
    for option in user_menu.values():
        print(option)
                    
    answer = int(input("\nSelect your method option here: "))
    if answer > 0 and answer < 4:
        method_menu[answer]()
    else:
        print("Invalid option. Please choose a valid option.")


#Decorated Function
def display_exit(func):
    def wrapper():
        func()
        exit_menu = {
            1 : "1. Go to the options menu",
            2 : "2. Exit"
        }
    
        print("\n<---Select the best option for you--->\n")
        for option in exit_menu.values():
            print(option)
        
        exit_answer = int(input("\nSelect your option here: "))   
        if exit_answer == 1:
            display_menu()     
        elif exit_answer == 2:
            print("\nThank you!")    
        else:
            print("Invalid option. Please choose a valid option.")
        
    return wrapper
                 
    
#Decorated Function
def positive_number(func):
    def wrapper():
        answer = int(input("Enter any number: "))
        func(answer)
    return wrapper             
             
  
@display_exit                                          
@positive_number
def display_numbers(answer):
    for i in range(1, answer + 1):
        print(i)
  
@display_exit                                                     
@positive_number
def even_number(answer):
    for i in range(2, answer + 1, 2):
        print(i)
     
@display_exit                                                       
@positive_number      
def odd_number(answer):
    for i in range(1, answer + 1, 2):
        print(i)


display_menu()