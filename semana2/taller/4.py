"Explica con tus palabras que significan las siguientes terminos en programacion:"


"""
    Respuesta:
    - Bucle: Una estructura que repite un bloque de código varias veces.
    - For: Un tipo de bucle usado para iterar sobre una secuencia o colección.
    - While: Un tipo de bucle que ejecuta un bloque de código mientras una condición sea verdadera.
"""



"TABLAS DE MULTIPLICAR"

"""
    Haciendo uso de los bucles vistos en clase crea un programa
    que le solicite al usurario ingresar un numer entero y muestra
    las tablas de multiplicar de dicho numero.
"""

def multiplication_table():
    number = int(input("Type any number you want: "))
    for i in range(1, 11, 1):
        print(f"{number} x {i} = {i * number}")
        
#multiplication_table()



"ESCALA - MULTIPLICACION Y DIVISION"

"""
    Haciendo uso de los bucles vistos en clase crea un programa que
    le solicite al usurario ingresar un numer entero y muestra
    en pantalla una “escala”
"""

def number_escale():
        number = int(input("Type a number: "))
        
        #Multiplication
        for i in range(2, 10, 1): 
            print(f"{i} x {number} = {i * number}")
            number *= i
                
        #Division    
        for i in range(9, 1, -1): 
            print(f"{i} / {int(number)} = {int(number / i)}")
            number /= i
            
        answer = input("Do you want to continue? (y/n) ")
        if answer.lower() == "y":
            number_escale()
        else:
            print("thank you!!")
        
number_escale()