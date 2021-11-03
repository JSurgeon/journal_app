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

        _habits (Habit[])

        _exercises (Exercise[])

    """

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
            for element in args[3]:
                self._habits = self._habits = element
            for element in args[4]:
                self._exercise = self.exercises = element 

    @classmethod
    def filled(cls, date, time, rest_obj, habits_lst, exercises_lst):
        """
        Returns a filled Entry object
        """
        return cls(date, time, rest_obj, habits_lst, exercises_lst)


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
            for element in self._habits:
                dict = {}
                for key, value in vars(element).items():
                    dict[key.replace("_", "", 1)] = value
                habs.append(dict)
                
            return habs


    @habits.setter
    def habits(self, habit):
        """
        Expects a Habit object, append it to habits list
        """
        # NEED TO implement object type check 
        self._habits.append(habit)
    
    @habits.deleter
    def habits(self):
        del self._habits

    # exercises attribute get, set, delete
    @property
    def exercises(self):
        """
        Returns a list of dictionary items
        Keys:
            name (string)
            startime 
            endtime
            quality (string)
            location (string)
            intensity (int)
        """

        if self._exercises == None:
            return None

        else:
            exercises = []
            for element in self._exercises:
                dict = {}
                for key, value in vars(element).items():
                    dict[key.replace("_", "", 1)] = value
                exercises.append(dict)
                
            return exercises


    @exercises.setter
    def exercises(self, exercise_obj):
        """
        Expects an Exercise object, appends it to exercise list
        """
        print("SETTER CALLED")
        # NEED TO implement object type check 
        self._exercises.append(exercise_obj)

    
    @exercises.deleter
    def exercises(self):
        del self._exercises

