"""
Ejercicios practicos

    - Pide al usuario que ingrese su edad y calcula el año de nacimiento,
      luego muéstralo en pantalla. (el año actual es 2024)

    - Solicita al usuario que ingrese su edad y verifica si es elegible para
      conducir un auto en su país (generalmente a partir de los 16 años).
      Imprime un mensaje que indique si es elegible o no.

    - Del ejercicio anterior agregar una validación si la persona no esta
      habilitada para conducir si es mayor de edad 85 años
    
"""


def age_calculator():
    current_year = 2024
    user_year = int(input("What is your year of birth? "))
    
    print(f"You are {current_year - user_year} years old")
      
#age_calculator()    



def drivers_license():
    driver_age = int(input("How old are you? "))
    minimum_age = 16
    maximum_age = 85
    
    if driver_age < minimum_age or driver_age > maximum_age:
        print("You are not eligible to drive")
    else:
        print("You are eligible to drive")
        
#drivers_license()        