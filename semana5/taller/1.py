import time

class Student():
    def __init__(self, name):
        self.name = name
        self.questions = {      
            "1": "76 - 33",
            "2": "13 + 46",
            "3": "78 - 35",
            "4": "15 * 4",
            "5": "11 + 10 - 14"
        }     
        

    def start_exam(self):
        print("\n📚 MATH EXAM 📚")
        print(f"🗿 This exam has {len(self.questions)} questions, you will know your exam grade and the time it took you at the end. 🗿\n")
      
        answers = {}
        start_time = time.time()
        
        for key in self.questions:
            while True:
                try:
                    user_answer = int(input(f"🛸 Result for {self.questions[key]} : "))
                    break
                except ValueError:
                    print("⛔ Invalid input. Please enter a valid number.\n")
            answers[key] = user_answer
        
        final_time = time.time()
        total_time = final_time - start_time
        
        print('')
        return answers, total_time
           
        
    def grade_exam(self, answers, total_time):
        correct_answers = 0    
         
        for key in self.questions:
            if answers[key] == eval(self.questions[key]):
                print(f"Answer #{key}: ✅")
                correct_answers += 1
            else:
                print(f"Answer #{key}: ❌")
        
        value_question = 100 / len(self.questions) 
        grade = value_question * correct_answers
        
        if grade <= 49:
            print(f"\n🎯 Come on, you can do it better {self.name}!")
        elif grade <= 69:
            print(f"\n✨ Good job {self.name}!")
        else:
            print(f"\n🧩 You are a Master Mind {self.name}!")
        
        print(f'🏆 Your score is {grade:.1f}% and it took you {total_time:.2f} seconds to finish the exam.')      
        
student1 = Student("Johan")
answers, total_time = student1.start_exam()
student1.grade_exam(answers, total_time)