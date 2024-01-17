from random import randint
from art import logo

Easy_Lever_turns = 10
Hard_Level_turn = 5

turns = 0
# function to check user's guess against actual number
def check_answer(guess, answer, turns):
    if guess > answer:
        print("TO High.")
        return turns-1
    elif guess < answer:
        print("TO Low.")
        return turns -1
    else:
        print("YOu got it! The answer was {answer}.")


# Make fucction to set difficulty
def set_difficulty():
    level = input("Choose a difficulty! type 'Easy' or 'Hard': ")
    if level == "Easy":
        return Easy_Lever_turns
    else:
        return Hard_Level_turn


def game():
    print(logo)
    # Choosing a number between 1 to 100
    print("Welcome the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")

    answer = randint(1, 100)
    #print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()
    

    # repeat the guessing functionality if they get it wrong

    guess = 0
    while guess != answer:
        print(f"YOu have {turns} attempt to remaining to guess the number.")

        # Let the user guess the number
        guess = int(input("Make a guess: "))
        # Track the number of turn and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"you've run out the guesses, YOU LOOSE.")
            return
        elif guess != answer:
            print("guess again")
game()