from entry import *
class Node:
    """
    Node is a base parent class
    \nAttributes:
        \n\t_next (Node)
        \n\t_entry (Entry)
    """

    def __init__(self):
        self._entry = Entry()
        self._next = None

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
    def entry(self):
        """
        Returns a dictionary
        \n\t{
            \t"Sleep": value,
            \t"Habits": value,
            \t"Exercises": value
        }
        """
        entry_dict = {
            "Sleep" : self._entry.sleep,
            "Habits": self._entry.habits,
            "Exercises": self._entry.exercises
        }
        return entry_dict

    @entry.setter
    def entry(self,to_set):
        self._entry = to_set

    @entry.deleter
    def entry(self):
        del self._entry


