# test file for activity Class and children
from copy import copy, deepcopy
from activity import Activity, Exercise, Habit, Rest


activity_name = "activity_name"
startime = 0
endtime = 2
quality = "Good"
location = "Home"

expected_dictionary = {
    "name" : activity_name,
    "start" : startime,
    "end" : endtime,
    "quality" : quality,
    "location" : location
}

def test_activity_values(activity_object, expected_values, test_name):


    print(f"\n--------------------------------------\nRunning Test: {test_name}\n--------------------------------------\n")
    print("activity.name get Test Passed") if activity_object.name == expected_values["name"] \
        else print("\nactivity.name get Test FAILED")

    print("\nactivity.start_time get  Test Passed") if activity_object.startime == expected_values["start"] \
        else print("\nactivity.start_time get Test FAILED")

    print("\nactivity.end_time get Test Passed") if activity_object.endtime == expected_values["end"] \
        else print("\nactivity.end_time get Test FAILED")

    print("\nactivity.quality get Test Passed") if activity_object.quality == expected_values["quality"] \
        else print("\nactivity.quality get Test FAILED")

    print("\nactivity.location get Test Passed") if activity_object.location == expected_values["location"] \
        else print("\nactivity.location get Test FAILED")

    return 
    
# create initial instance of object
obj_activity = Activity(expected_dictionary["name"], expected_dictionary["start"], expected_dictionary["end"], expected_dictionary["quality"], expected_dictionary["location"])


# test getters
test_activity_values(obj_activity, expected_dictionary, "Activity() getters test")

# set new expected values values; test setters
expected_dictionary["name"] = "new_name"
expected_dictionary["start"] = 5
expected_dictionary["end"] = 7
expected_dictionary["quality"] = "Terrible"
expected_dictionary["location"] = "Gym"

obj_activity.name = expected_dictionary["name"]
obj_activity.startime = expected_dictionary["start"]
obj_activity.endtime = expected_dictionary["end"]
obj_activity.quality = expected_dictionary["quality"]
obj_activity.location = expected_dictionary["location"]

test_activity_values(obj_activity, expected_dictionary, "Activity() setters test" )

# copying test case 1: values in original and new object are the same
new_activity = deepcopy(obj_activity)
test_activity_values(obj_activity, expected_dictionary, "Activity copy test case #1")
test_activity_values(new_activity, expected_dictionary, "New Object copy test case #1")

# copy test case 2: values in new object change
new_values =  {
    "name" : "a brand new activity",
    "start" : 1,
    "end" : 11,
    "quality" : "Ok",
    "location" : "Park"
}

new_activity.name = new_values["name"]
new_activity.startime = new_values["start"]
new_activity.endtime = new_values["end"]
new_activity.quality = new_values["quality"]
new_activity.location = new_values["location"]

test_activity_values(obj_activity, expected_dictionary, "Activity copy test case #2")
test_activity_values(new_activity, new_values, "New Object copy test case #2")

# test habit
def test_habit_values(habit_obj, expected_values, test_name):
    test_activity_values(habit_obj, expected_values, test_name)
    print("\nhabit.amount get Test Passed") if habit_obj.amount == expected_values["amount"] \
        else print("\nhabit.amount get Test FAILED")

expected_dictionary["name"] = "habit_name"
expected_dictionary["start"] = 5
expected_dictionary["end"] = 0
expected_dictionary["quality"] = "Okay"
expected_dictionary["location"] = "Bar"
expected_dictionary["amount"] = 29


# test initialization
habit_obj = Habit(expected_dictionary["name"],\
    expected_dictionary["start"],\
    expected_dictionary["quality"],\
    expected_dictionary["location"],\
    expected_dictionary["amount"])

test_habit_values(habit_obj, expected_dictionary, "Habit() initialization")

# set new expected values values; test setters
new_values["name"] = "new_name"
new_values["start"] = 5
new_values["end"] = 7
new_values["quality"] = "Terrible"
new_values["location"] = "Gym"
new_values["amount"] = 10

habit_obj.name = new_values["name"]
habit_obj.startime = new_values["start"]
habit_obj.endtime = new_values["end"]
habit_obj.quality = new_values["quality"]
habit_obj.location = new_values["location"]
habit_obj.amount = new_values["amount"]

test_habit_values(habit_obj, new_values, "Habit() setters")

# copying test case 1: values in original and new object are the same
expected_dictionary["end"] = 0

habit_obj = Habit(expected_dictionary["name"],\
    expected_dictionary["start"],\
    expected_dictionary["quality"],\
    expected_dictionary["location"],\
    expected_dictionary["amount"])

new_habit = deepcopy(habit_obj)

test_habit_values(habit_obj, expected_dictionary, "Habit() copy test case #1")
test_habit_values(new_habit, expected_dictionary, "New Habit() copy test case #1")

# copy test case 2: values in new object change
new_values =  {
    "name" : "a brand new activity",
    "start" : 1,
    "end" : 11,
    "quality" : "Ok",
    "location" : "Park",
    "amount" : 42
}

new_habit.name = new_values["name"]
new_habit.startime = new_values["start"]
new_habit.endtime = new_values["end"]
new_habit.quality = new_values["quality"]
new_habit.location = new_values["location"]
new_habit.amount = new_values["amount"]

test_habit_values(habit_obj, expected_dictionary, "Habit() copy test case #2")
test_habit_values(new_habit, new_values, "New Habit() copy test case #2")


########
# Rest Testing
########
def test_rest_values(rest_obj, expected_values, test_name):
    test_activity_values(rest_obj, expected_values, test_name)
    print("\nrest.amount get Test Passed") if rest_obj.interuptions == expected_values["interuptions"] \
        else print("\nrest.amount get Test FAILED")


expected_dictionary["interuptions"] = 5

sleep = Rest(expected_dictionary["name"],\
    expected_dictionary["start"],\
    expected_dictionary["end"],\
    expected_dictionary["quality"],\
    expected_dictionary["location"],\
    expected_dictionary["interuptions"])

new_sleep = deepcopy(sleep)

new_values["interuptions"] = 32

new_sleep.name = new_values["name"]
new_sleep.startime = new_values["start"]
new_sleep.endtime = new_values["end"]
new_sleep.quality = new_values["quality"]
new_sleep.location = new_values["location"]
new_sleep.interuptions = new_values["interuptions"]

test_rest_values(sleep, expected_dictionary, "Sleep() copy case #2")
test_rest_values(new_sleep, new_values, "New Sleep() copy case #2")