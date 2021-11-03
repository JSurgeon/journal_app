from entry import *

empty_entry = Entry()
new_habit = Habit("smoking", 9,"Bad","bar",4)
empty_list = []
empty_list.append(new_habit)
print(empty_list)
if(empty_entry._date == None and empty_entry.time == None and empty_entry.sleep == None and not empty_entry.habits and not empty_entry.exercises):
    print("All instance objects are None")

rest_obj = Rest("sleep", 10,11,"Good","Home",3)

habits_lst = []
habit = Habit("smoking", 9,"Bad","bar",4)
habits_lst.append(habit)
habits_lst.append(habit)

exercises_lst = []
exercise = Exercise("bball",2,3,"Great","Gym",5)
exercises_lst.append(exercise)
exercises_lst.append(exercise)

filled_entry = Entry().filled("11/2/21",10,rest_obj,habits_lst,exercises_lst)
print(habits_lst)
if(filled_entry.date != None and filled_entry.time != None and filled_entry.sleep != None and filled_entry.habits != None and filled_entry.exercises != None):
    print("All instance objects are filled")


print(filled_entry)
print("\nCHANGING EXERCISE list~~~~~~~~~~~~~~~~~~~~~")
exercise_obj = Exercise("new_obj", 12,13,"Ok", "Away",2)
exercises_lst.append(exercise_obj)
if(len(filled_entry.exercises) == 2):
    print("Change Successful: filled_entry was not altered by changing the exercise_lst")
else:
    print("Change FAILED:  filled_entry WAS altered by changing the exercise_lst ")
print()

print("Testing exercise object addition to Entry().exercises~~~~~~~~~")
exercise_obj = Exercise("another_new_obj", 12,13,"Ok", "Away",2)
filled_entry.exercises = exercise_obj
print(filled_entry)
if(len(filled_entry.exercises) == 3):
    print("Exercise list addition successful: exercise_obj was properly added to the list")
else:
    print("Exercise list addition FAILED: exercise_obj WAS NOT properly added to the list")


print("\n~~~~~~~~~~changing object")
exercise_obj = Exercise("not_the_right_exercise",1,2,"Terrible","Park",3)
print(filled_entry)

print("\n~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~\nTesting Entry.new()\n~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~")

new_entry = Entry().new()
print("\nPrinting entry object created with new()~~~~~~~~~~~~~\n")
print(new_entry)