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
    
def create_exercise():
    """
    Returns Activity
    """
    print("Which exercise did you perform?")
    for i, value in enumerate(exercises):
        print(f'{i+1}) {value}')
    exercise_name = exercises[ int( input() ) -1 ]
    # if "Other", add prompt user to input new exercise name
    if exercise_name == "Other":
        exercise_name = input("\nAwesome, you did something new! What exercise did you do?\n")
    
    exercise_start = input(f"What time of day did {exercise_name} begin?")
    exercise_end = input(f"What time of day did {exercise_name} end?")
    

        
        
        
        
        
    return response
            

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
        self._exercise = list()

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
        for element in [("Tobacco", "cigs"), ("Alcohol", "drinks")]:
            response = input(f"\nDid you use {element[0]} today? (Y/N)").capitalize()

            if (response == "Y" or response == "Yes"):
                occured = int( input(f"\nWhat time did the {element[0]} use start?") )   # NEED TO MAKE  TIME OBJECT
                use_location = input(f"\nWhere did the {element[0]} use occur?").capitalize()
                amount = int( input(f"\n{element[0]} ({element[1]}): ") )
                print(f"\nHow do you feel about the {element[0]} use?")
                use_quality = quality_options()

                self._habits.append(Habit(f"{element[0]} Use", occured, use_quality, use_location, amount))
    

        # Exercise Data
        response = input("Did you exercise today? (Y/N)\n").capitalize()
        if (response == "Yes" or response == "Y"):
            exercise_name = exercise_menu()




        
        # self._activities = acts
        # self._habits = habs
        # self._workouts = works


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
