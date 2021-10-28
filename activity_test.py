# test file for activity Class and children
from copy import copy, deepcopy
from activity import Activity, Exercise, Habit, Rest


activity_name = "activity_name"
startime = 0
endtime = 2
quality = "Good"
location = "Home"

expected_diction = {
    "name" : activity_name,
    "start" : startime,
    "end" : endtime,
    "quality" : quality,
    "location" : location
}

def test_activity_values(activity_object, expected_values, test_name):


    print(f"--------------------------------------\nRunning Test {test_name}\n--------------------------------------\n")
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

    print()

    return 
    
# create initial instance of object
obj_activity = Activity(expected_diction["name"], expected_diction["start"], expected_diction["end"], expected_diction["quality"], expected_diction["location"])


# test getters
test_activity_values(obj_activity, expected_diction, "Activity() getters test")

# set new expected values values; test setters
expected_diction["name"] = "new_name"
expected_diction["start"] = 5
expected_diction["end"] = 7
expected_diction["quality"] = "Terrible"
expected_diction["location"] = "Gym"

obj_activity.name = expected_diction["name"]
obj_activity.startime = expected_diction["start"]
obj_activity.endtime = expected_diction["end"]
obj_activity.quality = expected_diction["quality"]
obj_activity.location = expected_diction["location"]

test_activity_values(obj_activity, expected_diction, "Activity() setters test" )

# copying test case 1: values in original and new object are the same
new_activity = deepcopy(obj_activity)
test_activity_values(obj_activity, expected_diction, "Activity copy test case #1")
test_activity_values(new_activity, expected_diction, "New Object copy test case #1")

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

test_activity_values(obj_activity, expected_diction, "Activity copy test case #2")
test_activity_values(new_activity, new_values, "New Object copy test case #2")


