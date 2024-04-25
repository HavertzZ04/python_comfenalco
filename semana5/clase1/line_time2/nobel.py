from nobel_db import nobel_fisica

def exit_question(func):
    def wrapper():
        while True:
            print(func())
            print("\n0. Salir ⭕")
            print("1. Continuar aprendiendo ✅\n")
            
            answer = input("📝 Tu respuesta aqui: ")
            if answer == "0":
                print("Chao! 👋")
                break           
    return wrapper      


@exit_question
def get_year():
    while True:
        print("\n🪐 PREMIOS NOBEL DE FISICA 🪐")
        year = int(input("⭐ Dime un año (1901-2023) para obtener mas detalles: "))
        
        if year in nobel_fisica:
            details = nobel_fisica[year]
            return(f"\n- Año: {year}\n- Ganador(es): {details['ganador']}.\n- Logro: {details['logro']}.")
        
        print(f"\nNo existe un ganador para el año {year}")
       
                               
get_year()
 
