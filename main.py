import random
import art

numbers = [1] + [i for i in range(2, 99)] + [100]

def random_number():
    chosen_number = random.choice(numbers)
    return chosen_number

def choose_difficulty():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_input == "easy":
        return "easy"
    elif user_input == "hard":
        return "hard"
    else:
        print("Please type 'easy' or 'hard' only.")
        return choose_difficulty()

def life_checker(life):
    if life <= 0:
        return False
    else:
        return True

def play_again():
    while True:
        play_again_input = input("Do you want to play again? Please type 'y' for yes and 'n' for no: ").lower()
        if play_again_input == "y":
            return "y"
        elif play_again_input == "n":
            return "n"
        else:
            print("Please type 'y' for yes and 'n' for no only.")

def integer_input():
    try:
        user_input = int(input("Make a guess: "))
        return user_input
    except ValueError:
        print("Your input is not an integer. Please input number only")
        return integer_input()

def guess_number():
    life = 0
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_in_guess = random_number()

    difficulty = choose_difficulty()
    if difficulty == "easy":
        life = 10
    else:
        life = 5

    def game_start():
        nonlocal life
        print(f"You have {life} attempts remaining to guess the number.")
        guessed_number = integer_input()

        if guessed_number < number_in_guess:
            print("Too low.")
            life -= 1
            if life_checker(life):
                print("Guess again.")
                game_start()
            else:
                print("You've run out of guesses. You lose.\nGame over!")
        elif guessed_number > number_in_guess:
            print("Too high.")
            life -= 1
            if life_checker(life):
                print("Guess again.")
                game_start()
            else:
                print("You've run out of guesses. You lose.\nGame over!")
        else:
            print(f"You got it! The answer was {number_in_guess}.")

    game_start()

    if play_again() == 'y':
        guess_number()

guess_number()