from entry import *

# Exercise menu/creation debug #
exercise_list = exercise_menu()

for i, value in enumerate(exercise_list):
    print(vars(value))