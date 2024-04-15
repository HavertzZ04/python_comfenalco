import random

def play_guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts_made = 0
    max_attempts = 10
    
    print("Welcome to the Guess the Number game!")
    print(f"Guess a number between 1 and 100. You have a maximum of {max_attempts} attempts.")

    while attempts_made < max_attempts:
        try:
            guessed_number = int(input("Enter a number: "))
            if guessed_number < 1 or guessed_number > 100:
                print("Please enter a number within the range between 1 and 100.")
                continue
            
            attempts_made += 1

            if guessed_number == number_to_guess:
                print("Congratulations! You guessed the correct number!")
                break
            elif guessed_number < number_to_guess:
                print("The entered number is less than the number to guess.")
            else:
                print("The entered number is greater than the number to guess.")

        except ValueError:
            print("Please enter a valid number.")

    if attempts_made >= max_attempts:
        print(f"Sorry! You have reached the maximum of {max_attempts} attempts. The number to guess was {number_to_guess}.")


play_guess_the_number()
