import random

choices = {1: "🪨", 2: "🧻", 3: "✂️"}

def get_user_choice():
    while True:
        guess = input("Rock, paper, scissors? (r/p/s): ").lower()
        if guess == "r":
            return 1
        elif guess == "p":
            return 2
        elif guess == "s":
            return 3
        else:
            print("Invalid choice!")


def game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.randint(1, 3)

        if user_choice == computer_choice:
            print("It is a tie")
        elif (
            (user_choice == 1 and computer_choice == 3)
            or (user_choice == 2 and computer_choice == 1)
            or (user_choice == 3 and computer_choice == 2)
        ):
            print(
                f"Computer chose {choices[computer_choice]}  \nYou chose {choices[user_choice]} \nYou win."
            )
        else:
            print(
                f"Computer chose {choices[computer_choice]}  \nYou chose {choices[user_choice]} \nComputer win."
            )
        continue_game = input("Continue? (y/n): ").lower()
        if continue_game == "n":
            break


game()
