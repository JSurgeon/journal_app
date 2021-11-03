# file containing class Entry() 

from copy import deepcopy
from activity import Habit, Rest, Exercise, Activity
from datetime import date, datetime

class Node:
    """
    Node is a base parent class

    Instance Attributes:  

        next (Node)
        prev (Node)
    """

    def __init__(self):
        self._next = None
        self._prev = None
    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, to_set):
        self._next = to_set
        
    @next.deleter
    def next(self):
        del self._next

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, to_set):
        self._prev = to_set
        
    @prev.deleter
    def prev(self):
        del self._prev

class Entry(Node):
    """
    Entry is a child of Node

    Class Attributes:
        
        QUALITIES (list of strings)
        
        exercise_list (list of strings)

    Instance Attributes:

        _date (date)

        _time (datetime)

        _sleep (Rest)

        _habits (Habit[])

        _exercises (Exercise[])

    """
    QUALITIES = ["Terrible", "Bad", "Okay", "Good", "Great"]
    exercise_list = ["Basketball", "Run", "Walk", "Yoga", "Other"] # NEED TO MAKE DYNAMIC VIA ALL PAST ENTRIES; 
    
    def __init__(self, *args):

        # initialize parent Node
        super().__init__()

        # initialize instance attributes to default values
        self._date = None
        self._time = None
        self._sleep = None
        self._habits = []
        self._exercises = []

        if(len(args) > 0):
            self._date = args[0]
            self._time = args[1]
            self._sleep = args[2]
            # for element in args[3]:
            #     print("got here")
            #     self._habits = self.habits = element
            self._habits = deepcopy(args[3])
            self._exercises = deepcopy(args[4])

    # alternative "constructor" Entry.filled()
    @classmethod
    def filled(cls, date, time, rest_obj, habits_lst, exercises_lst):
        print("filled() called")
        """
        Returns a filled Entry object
        """
        return cls(date, time, rest_obj, habits_lst, exercises_lst)

    # alternative "constructor" Entry.new()
    @classmethod
    def new(cls):
        return cls(date.today(), datetime.now(), cls.sleep_menu(), cls.habit_menu(), cls.exercise_menu())
        
        

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
    # Entry class properties #
    ##########################

    # sleep attribute get, set, delete
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, to_set):
        self._time = deepcopy(to_set)
    
    @time.deleter
    def time(self):
        del self._time

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, to_set):
        self._date = deepcopy(to_set)
    
    @date.deleter
    def date(self):
        del self._date
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
        if self._sleep == None:
            return None
        
        else:
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
        Keys:
            name (string)
            startime 
            endtime
            quality (string)
            location (string)
            amount (int)       
        """
        if self._habits == None:
            return None
        
        else:
            habs = []
            dict = {}
            for element in self._habits:
                for key, value in vars(element).items():
                    dict[key.replace("_", "", 1)] = value
                habs.append(dict)
                
            return habs


    @habits.setter
    def habits(self, habit):
        """
        Expects a Habit object, append it to habits list
        """
        print("SETTER CALLED")
        # NEED TO implement object type check 
        self._habits.append(habit)
    
    @habits.deleter
    def habits(self):
        del self._habits

    # exercises attribute get, set, delete
    @property
    def exercises(self):
        return self._exercises


    @exercises.setter
    def exercises(self, exercise_obj):
        """
        Expects an Exercise object, appends it to exercise list
        """
  
        # NEED TO implement object type check 
        self._exercises.append(exercise_obj)

    
    @exercises.deleter
    def exercises(self):
        del self._exercises

###########
    # Class Methods
    @classmethod
    def quality_options(cls):
        """
        Returns string 
        """
        for i, value in enumerate(cls.QUALITIES):
            print(f'{i+1}) {value}')
        return cls.QUALITIES[ int( input() ) -1 ]   

    @classmethod
    def sleep_menu(cls):
        """
        Returns a Rest object
        """
        print("\nCollecting data about last night's sleep\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        sleep_location = input("\nWhere did you sleep?\n").capitalize()
        start_time = input("\nAbout when did you fall asleep last night?\n")  # NEED TO MAKE TIME OBJECT

        sleep_interuptions = int( input("\nHow many times were you woken up?\n") )
        
        print("\nHow well did you sleep?")
        sleep_quality = cls.quality_options()

        end_time = input("\nWhat time did you wake up this morning?\n") # NEED TO MAKE TIME OBJECT

        return Rest("Sleep", start_time, end_time, sleep_quality, sleep_location, sleep_interuptions)

    @classmethod
    def habit_menu(cls):
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
                use_quality = cls.quality_options()

                habit_list.append(Habit(f"{element[0]} Use", occured, use_quality, use_location, amount))

        return habit_list

    @classmethod
    def exercise_menu(cls):
        """
        Returns a list of Exercise objects or an empty list
        """
        print("Collecting data about today's Exercise\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        exercises = list()
        
        response = input("Did you exercise today? (Y/N)\n").capitalize()
        
        while (response == "Yes" or response == "Y"):
            exercises.append(cls.create_exercise())
            response = input("\nAdd another exercise for today? (Y/N)\n").capitalize()
        
        return exercises
        
    @classmethod
    def create_exercise(cls):
        """
        Returns an Exercise objects
        """
        print("Which exercise did you perform?")
        for i, value in enumerate(cls.exercise_list):
            print(f'{i+1}) {value}')
        exercise_name = cls.exercise_list[ int( input() ) -1 ]
        
        # if "Other", prompt user to input new exercise name
        if exercise_name == "Other":
            exercise_name = input("\nAwesome, you did something new! What exercise did you do?\n").capitalize()
        
        exercise_location = input(f"\nWhere did '{exercise_name}' occur?\n").capitalize()
        exercise_start = input(f"\nWhat time of day did '{exercise_name}' begin?\n")  # TIME!
        exercise_end = input(f"\nWhat time of day did '{exercise_name}' end?\n")  # TIME!
        exercise_intensity = input(f"\nOn a scale from 1-5, 5 being the greatest, how intense was '{exercise_name}'?\n")
        
        print(f"\nHow do you feel about today's '{exercise_name}'?")
        exercise_quality = cls.quality_options()

        return Exercise(exercise_name, exercise_start, exercise_end, exercise_quality, exercise_location, exercise_intensity)

