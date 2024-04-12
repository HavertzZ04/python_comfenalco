def exit_answer():
    while True:
        answer = input("""
Do you want to stay here?
    1. YES
    2. NO
    
Your answer here: """)
        
        if answer == "1":
            return True
        elif answer == "2":
            print("Thank you!!")
            return False
        else:
            print("Invalid answer")


def display_menu(options):
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        choice = int(input("\nYour answer here: "))
        if 1 <= choice <= len(options):
            return choice - 1
        else:
            print("Invalid input. Please enter a valid number.")

def site(menu_options):
    choice = display_menu(menu_options)
    
    if choice is not None:
        print(menu_options[choice])
        if exit_answer():
            site(menu_options)  # Repetir si el usuario quiere quedarse


def sports_site():
    menu_options = ["Team Sports", "Individual Sports", "Extreme Sports", "Cardio Box"]
    site(menu_options)

def food_site():
    menu_options = ["Breakfast", "Lunch", "Dinner", "Dessert"]
    site(menu_options)

def pets_site():
    menu_options = ["Dogs", "Cats", "Birds", "Reptiles"]
    site(menu_options)


#sports_site()
#food_site()
#pets_site()