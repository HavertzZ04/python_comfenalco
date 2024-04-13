def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

def main():
    print("Welcome to the temperature converter.")
    print("Please choose the desired option:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    option = int(input("Enter the option number (1-6): "))

    if option == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius)
        print(f"{celsius} degrees Celsius is equal to {round(result)} degrees Fahrenheit.")

    elif option == 2:
        celsius = float(input("Enter the temperature in Celsius: "))
        result = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is equal to {round(result)} Kelvin.")

    elif option == 3:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {round(result)} degrees Celsius.")

    elif option == 4:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        result = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to {round(result)} Kelvin.")

    elif option == 5:
        kelvin = float(input("Enter the temperature in Kelvin: "))
        result = kelvin_to_celsius(kelvin)
        print(f"{kelvin} Kelvin is equal to {round(result)} degrees Celsius.")

    elif option == 6:
        kelvin = float(input("Enter the temperature in Kelvin: "))
        result = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin is equal to {round(result)} degrees Fahrenheit.")

    else:
        print("Invalid option. Please enter a number from 1 to 6.")


#main()




def cop_dollar(cop):
    dollar = 3824
    usd_amount = cop * (1 / dollar)
    conversion = f"{cop} COP are ${usd_amount:.2f} USD"
    return conversion
    
#print(cop_dollar(200000))


#https://s3.static.brasilescola.uol.com.br/be/2023/12/padroes-numericos-da-sequencia-de-fibonacci.jpg

def fibonacci(number):
    fib_sequence = [1, 1]
    
    for i in range(2, number):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        
    return fib_sequence
    
#print(fibonacci(8))