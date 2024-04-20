#Escribe un programa que imprima un numero si es primo o no
def prime_number(numero):
    if numero <= 1:
        return False
    return all(numero % i for i in range(2, numero))


numero = int(input("Enter a number: "))
if prime_number(numero):
    print(numero, "it's prime")
else:
    print(numero, "it's not prime")
