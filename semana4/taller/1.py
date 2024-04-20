#Escribe un programa que tome tres números como entrada y devuelva el mayor de los tres

def get_mayor(n1, n2,n3):
    if n2 <= n1 >= n3:
        print(f"{n1} es el numero mayor.")
    elif n1 <= n2 >= n3:
        print(f"{n2} es el numero mayor.")
    else:
        print(f"{n3} es el numero mayor.")
        
get_mayor(2, 29, 29)