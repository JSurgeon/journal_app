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
        acts = []
        for activity in self._activities:
            acts.append(vars(activity))
        
        return acts
    
    @activities.setter
    def activities(self, acts):
        self._activities = acts
    
    @activities.deleter
    def activities(self):
        del self._activities
    
    # habits attribute get, set, delete
    @property
    def habits(self):
        """
        Returns a list of dictionary items
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
