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

    Instance Attributes:

        _date (date)

        _time (datetime)

        _sleep (Rest)

        _habits (list)

        _exercises (list)

        _activities (list)

    """
    
    def __init__(self, *args):

        # initialize parent Node
        super().__init__()

        # initialize instance attributes to default values
        self._date = None
        self._time = None
        self._sleep = None
        self._habits = list()
        self._exercises = list()
        self._activites = list()

    #     if(len(args) > 0):
    #         self._date = args[0]
    #         self._time = args[1]
    #         self._sleep = args[2]
    #         self._habits = deepcopy(args[3])
    #         self._exercises = deepcopy(args[4])

    # # alternative "constructor" Entry.filled()
    # @classmethod
    # def filled(cls, date, time, rest_obj, habits_lst, exercises_lst):
    #     """
    #     Returns a filled Entry object
    #     """
    #     return cls(date, time, rest_obj, habits_lst, exercises_lst)

    # # alternative "constructor" Entry.new()
    # @classmethod
    # def new(cls):
    #     return cls(date.today(), datetime.now(), cls.sleep_menu(), cls.habit_menu(), cls.exercise_menu())

    # def add_activity(self, added_activity):
    #     """
    #     Adds activity to appropriate instance attribute
    #     Return True if successful, False otherwise
    #     """
    #     if added_activity:

    #         if isinstance(added_activity, date):
    #             self._date = deepcopy(added_activity)
    #             return True

    #         elif isinstance(added_activity, datetime):
    #             self._time = deepcopy(added_activity)
    #             return True

    #         elif isinstance(added_activity, Rest):
    #             self._sleep = deepcopy(added_activity)
    #             return True

    #         elif isinstance(added_activity, Habit):
    #             habit = deepcopy(added_activity)
    #             self._habits.append(habit)
    #             return True

    #         elif isinstance(added_activity, Exercise):
    #             exercise = deepcopy(added_activity)
    #             self._habits.append(exercise)
    #             return True

    #         elif isinstance(added_activity, Activity):
    #             activity = deepcopy(added_activity)
    #             self._habits.append(activity)     
    #             return True

    #     return False

    def create_sleep(self, start, end, quality, location, interuptions):
        return Rest("Sleep", start, end, quality, location, interuptions)  

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, to_set):
        self._date = to_set
        
    @date.deleter
    def date(self):
        del self._date

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, to_set):
        self._time = to_set
        
    @time.deleter
    def time(self):
        del self._time

    @property
    def sleep(self):
        return self._sleep

    @sleep.setter
    def sleep(self, to_set):
        self._sleep = to_set
        
    @sleep.deleter
    def sleep(self):
        del self._sleep

    @property
    def activities(self):
        return self._activities

    @activities.setter
    def activities(self, to_set):
        self._activities = to_set
        
    @activities.deleter
    def activities(self):
        del self._activities

    @property
    def habits(self):
        return self._habits

    @habits.setter
    def habits(self, to_set):
        self._habits = to_set
        
    @habits.deleter
    def habits(self):
        del self._habits

    @property
    def exercises(self):
        return self._exercises

    @exercises.setter
    def exercises(self, to_set):
        self._exercises = to_set
        
    @exercises.deleter
    def exercises(self):
        del self._exercises