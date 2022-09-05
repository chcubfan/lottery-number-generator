import os
import random
from lottery import CashFive
from art import logo2

keep_going = True
cash_five = CashFive()


def cash_five_selection():
    sets_of_numbers = int(input("How many sets of Cash 5 numbers do you want?: "))
    for i in range(1, sets_of_numbers + 1):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
        my_numbers = []
        for number in range(1, 6):
            selected_number = random.choice(data)
            my_numbers.append(selected_number)
            data.remove(selected_number)

        print(f"Your Cash 5 numbers are: {my_numbers}")


def powerball_selection():
    sets_of_numbers = int(input("How many sets of PowerBall numbers do you want?: "))
    for i in range(1, sets_of_numbers + 1):
        pb_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
        pb_ball_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        pb_numbers = []
        for number in range(1, 6):
            selected_number = random.choice(pb_data)
            pb_numbers.append(selected_number)
            pb_data.remove(selected_number)

        powerball_ball = random.choice(pb_ball_data)
        print(f"Your PowerBall numbers are: {pb_numbers} PowerBall: {powerball_ball}")


def megamillions_selection():
    sets_of_numbers = int(input("How many sets of MegaMillions numbers do you want?: "))
    for i in range(1, sets_of_numbers + 1):
        mm_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
        mm_ball_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        mm_numbers = []
        for number in range(1, 6):
            selected_number = random.choice(mm_data)
            mm_numbers.append(selected_number)
            mm_data.remove(selected_number)

        megaball_ball = random.choice(mm_ball_data)
        print(f"Your MegaMillions numbers are: {mm_numbers} MegaBall: {megaball_ball}")


def continue_game():
    answer = input("Whould you like to generate more lottery numbers? Type 'y' for yes or 'n' for no: ").lower()
    if answer == "y":
        return True
    else:
        return False


def clear_screen():
    os.system("clear")


while keep_going:
    clear_screen()
    print(logo2)
    print("Welcome to the Lottery Number Generator!")
    print("1. Cash 5")
    print("2. PowerBall")
    print("3. MegaMillions")
    game_selection = input("Select the lottery game that you want numbers for. 1, 2 or 3: ")
    if game_selection == "1":
        cash_five_selection()
        # sets = cash_five.get_number_of_sets()
        # cash_five.generate_numbers(sets)
    elif game_selection == "2":
        powerball_selection()
    else:
        megamillions_selection()
    keep_going = continue_game()
