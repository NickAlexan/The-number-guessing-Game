import random
difficulty = {
    "e": 10,
    "h": 5,
}


def guess(number, attempts):
    while attempts > 0:
        user_guess = int(input("Try to guess: "))
        if user_guess == number:
            print(f"You win, number is {number}")
            return
        elif user_guess > number:
            print(f"Too high!")
        elif user_guess < number:
            print(f"Too low!")

        attempts -= 1

        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print(f"You Lose, the number is {number}")


def game():
    print("Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")
    dif_choice = input("Choose a difficulty. (E)asy or (H)ard?: ").lower()
    attempts = difficulty[dif_choice]
    guess(number, attempts)


game()
