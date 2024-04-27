from bmi_db import bmi_diccionary

class User():
    def __init__(self):
        self.first_name = input("\n👤 Enter your name: ")
        self.height = float(input("📏 Enter your height in meters (example: 1.71): "))
        self.weight = int(input("🧬 Enter your weight in kilograms (example: 66): "))  

    def BodyMassIndex(self): 
        bmi = round(self.weight / (self.height ** 2), 1) 
        
        for bmi_status, bmi_range in bmi_diccionary.items():
            
            min_normal_bmi = bmi_diccionary['Normal'][0]
            max_normal_bmi = bmi_diccionary['Normal'][1]
            
            answer = f"\n🩻  Body Mass Index: {bmi}\n📂 Status: {bmi_status}"
            
            if bmi_range[0] <= bmi <= bmi_range[1]:
                if bmi < min_normal_bmi: 
                    win_weight = round((min_normal_bmi - bmi) * self.height ** 2)
                    return f"{answer}\n📈 {self.first_name}, you have to win {win_weight} kgs."

                elif bmi > max_normal_bmi:
                    lose_weight = round((bmi - max_normal_bmi) * self.height ** 2)
                    return f"{answer}\n📉 {self.first_name}, you have to lose {lose_weight} kgs."
                
                else:
                    return f"{answer}\n🎉 Congratulations {self.first_name}!"
                 
         
usuario1 = User()
print(usuario1.BodyMassIndex())

