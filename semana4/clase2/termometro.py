class TermometroEmociones:
    def __init__(self):
        self.emocion_actual = 0
        self.emociones = {
            0: "Triste",
            1: "Feliz",
            2: "Preocupado",
            3: "Aterrorizado"
        }
    
    def aumentar_emocion(self):
        if self.emocion_actual <= 3:
            self.emocion_actual += 1
            print(f"\nEmocion aumentada. Emocion actual: {self.emociones[self.emocion_actual]}")
        else:
            print("\nEstas demasiado emocionado!")
    
    def disminuir_emocion(self):
        if self.emocion_actual > 0:
            self.emocion_actual -= 1
            print(f"\nEmocion disminuida. Emocion actual: {self.emociones[self.emocion_actual]}")
        else:
            print("\nEstas demasiado tranquilo!")

    def acciones(self):
        acciones_list = {
            0: ["Abraza a alguien", "Ejercitate", "Habla con un adulto"],
            1: ["Practica la gratitud", "Usa palabras edificadoras", "Comparte con tus amigos"],
            2: ["Pausa y pida ayuda", "Usa la tecnica de 'grounding'", "Escucha musica relajante"],
            3: ["Cuenta del 1 al 10", "Respira profundo", "Toma una siesta"]
        }
        print("Acciones sugeridas para mejorar:")
        for accion in acciones_list[self.emocion_actual]:
            print("-", accion)

# Ejemplo de uso

termometro = TermometroEmociones()

termometro.aumentar_emocion()  
termometro.acciones()

termometro.aumentar_emocion()  
termometro.acciones()

termometro.aumentar_emocion() 
termometro.acciones()

termometro.disminuir_emocion() 
termometro.acciones()

termometro.disminuir_emocion() 
termometro.acciones()

termometro.disminuir_emocion() 
termometro.acciones()
