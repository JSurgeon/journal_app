# file containing classes Day() and Entry() 

from activity import *
from datetime import date, datetime

class Entry:
    """
    Day is a base parent class
    Attributes:
        Rest sleep
        Activity activities[]
        Habit habits[]
        Exercise workouts[]
        datetime date
        datetime time
    """
    def __init__(self, rest, acts, habs, works):
        self._sleep = rest
        self._activities = acts
        self._habits = habs
        self._workouts = works
        self._date = date.today()
        self._time = datetime.now()

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
