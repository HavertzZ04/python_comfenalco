import random

class HangmanGame:
    def __init__(self):
        self.words = ["python", "javascript", "php", "java", "rust", "go", "sql", "matlab"]
        self.secret_word = self.get_secret_word().upper()
        self.found_letters = []
        self.wrong_letters = []
        self.remaining_attempts = 10
    
    def get_secret_word(self):
        return random.choice(self.words)
    
    def show_secret_word(self):
        result = ''
        for letter in self.secret_word:
            if letter in self.found_letters:
                result += letter
            else:
                result += "_"
        return result
    
    def play(self):
        print("\n👀 HANGMAN GAME 👀") 
        print("🎮 Find the word related with programming languages 🎮\n")
        
        while True:
            current_result = self.show_secret_word()
            print(f"📝 Word: {current_result}")
            
            if current_result == self.secret_word:
                print("\n🎖️  Congrats, you got it! 🎖️")
                break
            
            if self.remaining_attempts == 0:
                print(f"\n⛔ You don't have more attempts, the word was: {self.secret_word} ⛔")
                break
                
            letter = input("🔆 Enter a letter (A - Z): ").upper()
            attempts_message = f"🎲 Remaining Attempts: {self.remaining_attempts} \n"
            
            if letter in self.found_letters or letter in self.wrong_letters:
                print(f'🔄 You tried with "{letter}" already, try with a different one.')
                print(attempts_message)
                continue
            
            if letter in self.secret_word:
                self.found_letters.append(letter)
            else:
                self.wrong_letters.append(letter)
                self.remaining_attempts -= 1
            
            print(attempts_message)
        
        print("🧩 Thanks for playing 🧩")


game = HangmanGame()
game.play()
