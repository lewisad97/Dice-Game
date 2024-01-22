import random
import time

def roll_dice():
    """Roll two dice and return their sum."""
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

def play_game():
    while True:
        input("Press 'Enter' to roll the dice ...")
        total = roll_dice()
        print(f"You rolled a total of: {total}")

        if total in [7, 11]:
            print("Congratulations! You won!")
            break
        elif total in [2, 3, 12]:
            print("Sorry, you lost!")
            break
        else:
            print("Roll again!")
            time.sleep(1)

if __name__ == "__main__":
    print("Welcome to the Dice Game!")
    play_game()
