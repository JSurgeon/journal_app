# file containing classes Day() and Entry() 

from entry_helpers import *

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

    def __init__(self):
        # initialize necessary instance attributes
        self._date = date.today()
        self._time = datetime.now()

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"\
              "~~ Creating new journal entry ~~\n"\
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        # Sleep Data
        self._sleep = sleep_menu()
        
        # Habit Data
        self._habits = habit_menu()
    
        # Exercise Data
        self._exercises = exercise_menu()

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
        return self._sleep
    
    @sleep.setter
    
    def sleep(self, rest):
        """
        Expects a Rest object
        """
        # NEED TO implement object type check

        self._sleep = rest
    
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
        Expects a list of Habit objects
        """
        # NEED TO implement object type check
        self._habits = habs
    
    @habits.deleter
    def habits(self):
        del self._habits

    # workouts attribute get, set, delete
    @property
    def workouts(self):
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
        workouts = []
        for element in self._exercises:
            dict = {}
            for key, value in vars(element).items():
                dict[key.replace("_", "", 1)] = value
            workouts.append(dict)
            
        return workouts

    @workouts.setter
    def workouts(self, works):
        """
        Expects a list of Exercise objects
        """
        # NEED TO implement object type check
        self._workouts = works
    
    @workouts.deleter
    def workouts(self):
        del self._workouts
