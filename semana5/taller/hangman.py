import random
import string

class HangmanGame:
    def __init__(self):
        self.words = ["python", "javascript", "php", "java", "rust", "go", "sql", "matlab"]
        self.secret_word = random.choice(self.words).upper()
        self.found_letters = set()
        self.wrong_letters = set()
        self.remaining_attempts = 10

    
    def show_secret_word(self):
        result = ''
        for letter in self.secret_word:
            if letter in self.found_letters:
                result += letter 
            else:
                result += "_" 
        return result

    
    def play_hangman(self):
        print("👀 HANGMAN GAME 👀") 
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
                
            while True:
                letter = input("🔆 Enter a letter (A - Z): ").strip().upper()      
                
                if len(letter) != 1 or letter not in string.ascii_uppercase:
                    print("📛 Please enter a single letter (A - Z).\n")
                elif letter in self.found_letters or letter in self.wrong_letters:
                    print(f'\n🔄 You tried "{letter}" already, try a different letter.')
                    print(f"\n🎲 Remaining Attempts: {self.remaining_attempts}")
                    print(f"📝 Word: {current_result}")
                else:
                    break
            
            if letter in self.secret_word:
                self.found_letters.add(letter)
            else:
                self.wrong_letters.add(letter)
                self.remaining_attempts -= 1
                print(f"❌ '{letter}' is not in the word.")
            
            print(f"\n🎲 Remaining Attempts: {self.remaining_attempts}")
                 
        print("🧩 Thanks for playing! 🧩")

