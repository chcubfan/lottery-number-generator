
import pandas
import random


class CashFive:

    def __init__(self):
        self.sets_of_numbers = 0
        self.my_numbers = []
        self.all_numbers = []

    def get_number_of_sets(self):
        self.sets_of_numbers = int(input("How many sets of Cash 5 numbers do you want?: "))
        return self.sets_of_numbers

    def generate_numbers(self, number_of_sets):
        for set_num in range(1, number_of_sets - 1):
            data = pandas.read_csv("cash5.csv")
            print(data)
            self.my_numbers = []
            # for number in range(1, 6):
            #     selected_number = random.choice(data)
            #     self.my_numbers.append(selected_number)
            #     data.remove(selected_number)
            # self.all_numbers.append(self.my_numbers)

        print(self.all_numbers)
