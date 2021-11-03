from entry import *

empty_entry = Entry()

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

if(filled_entry._date != None and filled_entry.time != None and filled_entry.sleep != None and filled_entry.habits != None and filled_entry.exercises != None):
    print("All instance objects are filled")


print(filled_entry)
print("CHANGING EXERCISE list~~~~~~~~~~~~~~~~~~~~~")
exercise_obj = Exercise("new_obj", 12,13,"Ok", "Away",2)
exercises_lst.append(exercise_obj)
print(filled_entry)

exercise_obj = Exercise("another_new_obj", 12,13,"Ok", "Away",2)
filled_entry.exercises = exercise_obj
print(filled_entry)

print("changing object")
exercise_obj = Exercise("not_the_right_exercise",1,2,"Terrible","Park",3)
print(filled_entry)

