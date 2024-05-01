from math_exam import Student
from hangman import HangmanGame


def exit_validation(func):
    def wrapper():
        while True:
            func()
            
            print("0️⃣. Exit")
            print("1️⃣. Play another game")
            
            answer = input("\n🟣 Your answer here: ")
            
            if answer == "0" :
                print("\n🔱 Have a good day, bye 🔱")
                break                    
    return wrapper


@exit_validation
def select_game(): 
    while True:
        print("🤖 GAMES GAMES GAMES 🤖\n")
        print("1️⃣. Math Game")
        print("2️⃣. Hangman Game\n")
        
        game_to_play = input("🟡 Select the game: ")
        
        if game_to_play == "1":
            user = Student()
            user.start_exam()
            user.grade_exam()
            break
            
            
        if game_to_play == "2":
            user = HangmanGame()
            user.play_hangman()
            break
        

select_game()