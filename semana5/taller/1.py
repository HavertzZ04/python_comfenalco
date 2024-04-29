import time

class User():
    def __init__(self, name):
        self.name = name
        
        
    def start_exam(self):
        print("\n📚 MATH EXAM 📚")
        print("🗿 This exam has 5 questions, you will know your exam grade and the time it took you at the end. 🗿\n")
        
        questions = {      
            "1": "76 - 33",
            "2": "6 + 41",
            "3": "98 - 39",
            "4": "17 * 4",
            "5": "11 * 10 - 14"
        }  
        
        answers = {}
        
        start_time = time.time()
        
        for key in questions:
            while True:
                try:
                    user_answer = int(input(f"🛸 Result for {questions[key]} : "))
                    break
                except ValueError:
                    print("⛔ Invalid input. Please enter a valid number.\n")
            answers[key] = user_answer
        
        print('')
         
        correct_answers = 0
        for key in questions:
            if answers[key] == eval(questions[key]):
                print(f"Answer #{key}: ✅")
                correct_answers += 1
            else:
                print(f"Answer #{key}: ❌")
        
        final_time = time.time()
        total_time = final_time - start_time
        
        value_answer = 100 / len(questions) 
        grade = value_answer * correct_answers
        
        if grade <= 49:
            print(f"\n🎯 Come on, you can do it better {self.name}!")
        elif grade <= 69:
            print(f"\n✨ Good job {self.name}!")
        else:
            print(f"\n🧩 You are a Master Mind {self.name}!")
        
        print(f'🏆 Your score is {grade}% and it took you {total_time:.2f} seconds to finish the exam.')

        
user1 = User("Johan")
user1.start_exam()