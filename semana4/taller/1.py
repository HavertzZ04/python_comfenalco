#Escribe un programa que tome tres números como entrada y devuelva el mayor de los tres

def get_mayor(n1, n2,n3):
    texto = "es el numero mayor."
    if n2 <= n1 >= n3:
        return (f"{n1} {texto}")
    elif n1 <= n2 >= n3:
        return (f"{n2} {texto}")
    else:
        return (f"{n3} {texto}")
        
print(get_mayor(2, 6, 25))