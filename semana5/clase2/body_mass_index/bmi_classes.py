from bmi_db import bmi_diccionary

class User():
    def __init__(self):
        self.first_name = input("\n👤 Enter your name: ")
        self.height = float(input("📏 Enter your height in meters (example: 1.71): "))
        self.weight = int(input("🧬 Enter your weight in kilograms (example: 66): "))  

    def BodyMassIndex(self): 
        min_normal_weight = 18.5 # Peso min normal de un imc
        max_normal_weight = 24.5 # Peso max normal de un imc
        bmi = round(self.weight / (self.height ** 2), 1) # imc del usuario
        
        # Ingresamos a la llave y valor (range, status) del diccionario
        for key, value in bmi_diccionary.items():
            # Asignamos los valores a unas variables
            bmi_range = value["range"] 
            bmi_status = value["status"] 
            
            #Respuesta que se repite para todos los casos
            answer_template = f"\n🩻  Body Mass Index: {bmi}\n📂 Status: {bmi_status}"
            
            #Condicional para saber si el usuario tiene desnutricion, sobre peso o esta normal 
            if bmi_range[0] <= bmi <= bmi_range[1]: #bmi_range tiene como valor una lista con dos numeros para saber los rangos
                
                #Confirmamos si el usuario tiene desnutricion
                if bmi < min_normal_weight: 
                    #win_weght es el peso que el usuario debe ganar
                    win_weight = round((min_normal_weight - bmi) * self.height ** 2)
                    return f"{answer_template}\n📈 {self.first_name}, you have to win {win_weight} kgs."
                
                
                #Confirmamos si el usuario tiene sobrepeso
                elif bmi > max_normal_weight:
                    #lose_weght es el peso que el usuario debe perder
                    lose_weight = round((bmi - max_normal_weight) * self.height ** 2)
                    return f"{answer_template}\n📉 {self.first_name}, you have to lose {lose_weight} kgs."
                
                #Felicitamos al usuario si su peso es normal
                else:
                    return f"{answer_template}\n🎉 Congratulations {self.first_name}!"
                 
         
usuario1 = User()
print(usuario1.BodyMassIndex())

