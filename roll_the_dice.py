import random

def roll_the_dice():
    return random.randint(1,6)

if __name__ == "__main__":
    while True:
        user_input = input("Do you want to roll the dice (y/n): ")
        if user_input.lower() == 'y':
            print(roll_the_dice())
        elif user_input.lower() == 'n':
            print(f"See you next time!")
            print()
            break
        else:
            print(f"Is that a 'yes' or 'no'...?")

