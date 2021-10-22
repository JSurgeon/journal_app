# file containing classes Day() and Entry() 

from activity import *
from datetime import date, datetime

QUALITIES = ["Terrible", "Bad", "Okay", "Good", "Great"]
exercises = ["Basketball", "Run", "Walk", "Yoga", "Other"] # NEED TO MAKE DYNAMIC VIA ALL PAST ENTRIES; 
                                                            #REORDER SO OTHER IS AT THE END ALWAYS
def quality_options():
    """
    Returns string 
    """
    for i, value in enumerate(QUALITIES):
        print(f'{i+1}) {value}')
    return QUALITIES[ int( input() ) -1 ]   

def habit_menu():
    """
    Returns a list of Habit objects or an empty list
    """
    habit_list = list()
    for element in [("Tobacco", "cigs"), ("Alcohol", "drinks")]:
        response = input(f"\nDid you use {element[0]} today? (Y/N)\n").capitalize()

        if (response == "Y" or response == "Yes"):
            occured = int( input(f"\nWhat time did the {element[0]} use start?\n") )   # NEED TO MAKE  TIME OBJECT
            use_location = input(f"\nWhere did the {element[0]} use occur?\n").capitalize()
            amount = int( input(f"\nAmount of {element[1]}: ") )
            print(f"\nHow do you feel about the {element[0]} use?")
            use_quality = quality_options()

            habit_list.append(Habit(f"{element[0]} Use", occured, use_quality, use_location, amount))

    return habit_list

    
def exercise_menu():
    """
    Returns a list of Exercise objects or an empty list
    """
    exercises = list()
    
    response = input("Did you exercise today? (Y/N)\n").capitalize()
    
    while (response == "Yes" or response == "Y"):
        exercises.append(create_exercise())
        response = input("\nAdd another exercise for today? (Y/N)\n").capitalize()
    
    return exercises
    
def create_exercise():
    """
    Returns an Exercise objects
    """
    print("Which exercise did you perform?")
    for i, value in enumerate(exercises):
        print(f'{i+1}) {value}')
    exercise_name = exercises[ int( input() ) -1 ]
    
    # if "Other", prompt user to input new exercise name
    if exercise_name == "Other":
        exercise_name = input("\nAwesome, you did something new! What exercise did you do?\n").capitalize()
    
    exercise_location = input(f"\nWhere did {exercise_name} occur?\n").capitalize()
    exercise_start = input(f"\nWhat time of day did {exercise_name} begin?\n")  # TIME!
    exercise_end = input(f"\nWhat time of day did {exercise_name} end?\n")  # TIME!
    exercise_intensity = input(f"\nOn a scale from 1-5, 5 being the greatest, how intense was {exercise_name}?\n")
    
    print(f"\nHow do you feel about today's {exercise_name}?")
    exercise_quality = quality_options()

    return Exercise(exercise_name, exercise_start, exercise_end, exercise_quality, exercise_location, exercise_intensity)

class Entry:
    """
    Entry is a base parent class
    Attributes:
        Rest sleep
        Activity activities[]
        Habit habits[]
        Exercise workouts[]
        datetime date
        datetime time
    """

    def __init__(self):
        # initialize necessary instance attributes
        self._date = date.today()
        self._time = datetime.now()

        self._habits = list()
        self._activities = list()
        self._exercises = list()

        print("Creating new journal entry\n- - - - - - - - - - - - - -")
        
        # Sleep Data #
        print("Collecting data about last night's sleep\n- - - - - - - - - - - - - - - - - - - -")
        sleep_location = input("\nWhere did you sleep?\n").capitalize()
        start_time = input("\nAbout when did you fall asleep last night?\n")  # NEED TO MAKE TIME OBJECT

        sleep_interuptions = int( input("\nHow many times were you woken up?\n") )
        
        print("\nHow well did you sleep?")
        sleep_quality = quality_options()

        end_time = input("\nWhat time did you wake up this morning?\n") # NEED TO MAKE TIME OBJECT

        self._sleep = Rest("Sleep", start_time, end_time, sleep_quality, sleep_location, sleep_interuptions)
        
        
        # Habit data
        self._habits = habit_menu()
    
        # Exercise Data
        self._exercises = exercise_menu()
        




        


    ####
    # Entry class decorators
    ####

    # sleep attribute get, set, delete
    @property
    def sleep(self):
        return self._sleep
    
    @sleep.setter
    def sleep(self, rest):
        self._sleep = rest
    
    @sleep.deleter
    def sleep(self):
        del self._sleep

    # activities attribute get, set, delete
    @property
    def activities(self):
        return self._activities
    
    @activities.setter
    def activities(self, acts):
        self._activities = acts
    
    @activities.deleter
    def activities(self):
        del self._activities
    
    # habits attribute get, set, delete
    @property
    def habits(self):
        return self._habits
    
    @habits.setter
    def habits(self, habs):
        self._habits = habs
    
    @habits.deleter
    def habits(self):
        del self._habits

    # workouts attribute get, set, delete
    @property
    def workouts(self):
        return self._workouts
    
    @workouts.setter
    def workouts(self, works):
        self._workouts = works
    
    @workouts.deleter
    def workouts(self):
        del self._workouts
