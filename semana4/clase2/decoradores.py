class menu_options:
    def __init__(self):
        self.menu = {
            1 : "1. Numbers from 1 to N.",
            2 : "2. Even numbers",
            3 : "3. Odd numbers"
        }
    
    # def display_menu(self, decorated_function):  
    #     def wrapper():
    #             for option in self.menu.values():
    #                 print(option)
    #                 option += 1
                    
    #             answer = int(input("Select your option here: "))
    #             if answer > 0 and answer < 4:
    #                 decorated_function
    #             else:
    #                 print("Invalid option. Please choose a valid option.")


    #     return wrapper()
    
    def positive_number(decorated_function):
        def wrapper(self):
            answer = int(input("Enter any number: "))
            decorated_function(self, answer)
        return wrapper             
          
                                  
    @positive_number
    def display_numbers(self, answer):
        for i in range(1, answer + 1):
            print(i)
                                                    
    @positive_number
    def even_number(self, answer):
        for i in range(2, answer + 1, 2):
            print(i)
                                                     
    @positive_number      
    def odd_number(self, answer):
        for i in range(1, answer + 1, 2):
            print(i) 


menu = menu_options()
menu.even_number()

