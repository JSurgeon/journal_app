# file containing classes Day() and Entry() 

from copy import deepcopy
from activity import Habit, Rest, Exercise, Activity
from datetime import date, datetime


class Entry:
    """
    Entry is a base parent class
    Attributes:
        _date (date)
        _time (datetime)
        _sleep (Rest)
        _habits (Habit[])
        _exercises (Exercise[])

    """
    QUALITIES = ["Terrible", "Bad", "Okay", "Good", "Great"]
    exercise_list = ["Basketball", "Run", "Walk", "Yoga", "Other"] # NEED TO MAKE DYNAMIC VIA ALL PAST ENTRIES; 
                                                                #REORDER SO 'OTHER' IS AT THE END ALWAYS

    def __init__(self):
        # initialize necessary instance attributes
        self._date = date.today()
        self._time = datetime.now()

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"\
              "~~ Creating new journal entry ~~\n"\
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        # Sleep Data
        self._sleep = self.sleep_menu()
        
        # Habit Data
        self._habits = self.habit_menu()
    
        # Exercise Data
        self._exercises = self.exercise_menu()

    def __deepcopy__(self, memo):
        new_entry = Entry()
        new_entry._sleep = self._sleep
        
    def __str__(self):
        
        string = f"{type(self)}(\
            \n\tDate: {self._date}\
            \n\tTime: {self._time}\n\
            \n\tSleep Object: {self._sleep}\n\
            \n\t{len(self._habits)} Habit Object(s):\n"

        for i, element in enumerate(self._habits):
            string += f"\n\t\t({i+1}) " + str(element)

        string += f"\n\n\t{len(self._exercises)} Exercise Object(s):\n"

        for i, element in enumerate(self._exercises):
            string += f"\n\t\t({i+1}) " + str(element)


        return string
        
    ##########################
    # Entry class decorators #
    ##########################

    # sleep attribute get, set, delete
    @property
    def sleep(self):
        """
        Returns a dictionary object
        Keys:
            name (string)
            startime 
            endtime
            quality (string)
            location (string)
            interuptions (int)        
        """
        dict = {}
        for key, value in vars(self._sleep).items():
                dict[key.replace("_", "", 1)] = value
        return dict
    
    @sleep.setter
    def sleep(self, rest):
        """
        Expects a Rest object
        """
        # NEED TO implement object type check 

        self._sleep = deepcopy(rest)
    
    @sleep.deleter
    def sleep(self):
        del self._sleep

    # habits attribute get, set, delete
    @property
    def habits(self):
        """
        Returns a list of dictionary items
        Key:
            name (string)
            startime 
            endtime
            quality (string)
            location (string)
            amount (int)       
        """
        habs = []
        for element in self._habits:
            dict = {}
            for key, value in vars(element).items():
                dict[key.replace("_", "", 1)] = value
            habs.append(dict)
            
        return habs


    @habits.setter
    def habits(self, habs):
        """
        Expects a list
        """
        # NEED TO implement object type check 
        habit_arry = []
        for element in habs:
            habit_arry.append(deepcopy(element))
    
    @habits.deleter
    def habits(self):
        del self._habits

    # exercises attribute get, set, delete
    @property
    def exercises(self):
        """
        Returns a list of dictionary items
        Key:
            name (string)
            startime 
            endtime
            quality (string)
            location (string)
            intensity (int)
        """
        exercises = []
        for element in self._exercises:
            dict = {}
            for key, value in vars(element).items():
                dict[key.replace("_", "", 1)] = value
            exercises.append(dict)
            
        return exercises

    @exercises.setter
    def exercises(self, exers):
        """
        Expects a list of Exercise objects
        """
        # NEED TO implement object type check 
        exercise_array = []
        for element in exers:
            exercise_array.append(deepcopy(element))
    
    @exercises.deleter
    def exercises(self):
        del self._exercises

    @classmethod
    def quality_options(self):
        """
        Returns string 
        """
        for i, value in enumerate(self.QUALITIES):
            print(f'{i+1}) {value}')
        return self.QUALITIES[ int( input() ) -1 ]   

    @classmethod
    def sleep_menu(self):
        """
        Returns a Rest object
        """
        print("\nCollecting data about last night's sleep\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        sleep_location = input("\nWhere did you sleep?\n").capitalize()
        start_time = input("\nAbout when did you fall asleep last night?\n")  # NEED TO MAKE TIME OBJECT

        sleep_interuptions = int( input("\nHow many times were you woken up?\n") )
        
        print("\nHow well did you sleep?")
        sleep_quality = self.quality_options()

        end_time = input("\nWhat time did you wake up this morning?\n") # NEED TO MAKE TIME OBJECT

        return Rest("Sleep", start_time, end_time, sleep_quality, sleep_location, sleep_interuptions)

    @classmethod
    def habit_menu(self):
        """
        Returns a list of Habit objects or an empty list
        """
        print("\nCollecting data about today's Tobacco and Alcohol use\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        habit_list = list()
        for element in [("Tobacco", "cigs"), ("Alcohol", "drinks")]:
            response = input(f"\nDid you use {element[0]} today? (Y/N)\n").capitalize()

            if (response == "Y" or response == "Yes"):
                occured = int( input(f"\nWhat time did the {element[0]} use start?\n") )   # NEED TO MAKE  TIME OBJECT
                use_location = input(f"\nWhere did the {element[0]} use occur?\n").capitalize()
                amount = int( input(f"\nAmount of {element[1]}: ") )
                print(f"\nHow do you feel about the {element[0]} use?")
                use_quality = self.quality_options()

                habit_list.append(Habit(f"{element[0]} Use", occured, use_quality, use_location, amount))

        return habit_list

    @classmethod
    def exercise_menu(self):
        """
        Returns a list of Exercise objects or an empty list
        """
        print("Collecting data about today's Exercise\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        exercises = list()
        
        response = input("Did you exercise today? (Y/N)\n").capitalize()
        
        while (response == "Yes" or response == "Y"):
            exercises.append(self.create_exercise())
            response = input("\nAdd another exercise for today? (Y/N)\n").capitalize()
        
        return exercises
        
    @classmethod
    def create_exercise(self):
        """
        Returns an Exercise objects
        """
        print("Which exercise did you perform?")
        for i, value in enumerate(self.exercise_list):
            print(f'{i+1}) {value}')
        exercise_name = self.exercise_list[ int( input() ) -1 ]
        
        # if "Other", prompt user to input new exercise name
        if exercise_name == "Other":
            exercise_name = input("\nAwesome, you did something new! What exercise did you do?\n").capitalize()
        
        exercise_location = input(f"\nWhere did '{exercise_name}' occur?\n").capitalize()
        exercise_start = input(f"\nWhat time of day did '{exercise_name}' begin?\n")  # TIME!
        exercise_end = input(f"\nWhat time of day did '{exercise_name}' end?\n")  # TIME!
        exercise_intensity = input(f"\nOn a scale from 1-5, 5 being the greatest, how intense was '{exercise_name}'?\n")
        
        print(f"\nHow do you feel about today's '{exercise_name}'?")
        exercise_quality = self.quality_options()

        return Exercise(exercise_name, exercise_start, exercise_end, exercise_quality, exercise_location, exercise_intensity)
