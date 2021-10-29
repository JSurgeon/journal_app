# File containing activity class and it's children
from copy import copy, deepcopy
class Activity:
    def __init__(self, name, start, end, quality, location):
        self._name = name
        self._startime = int(start)
        self._endtime = int(end)
        self._quality = quality
        self._location = location

    def __deepcopy__(self, memo):
        return Activity(\
            deepcopy(self._name, memo),\
            deepcopy(self._startime, memo),\
            deepcopy(self._endtime, memo),\
            deepcopy(self._quality, memo),\
            deepcopy(self._location, memo)\
            )

    def __str__(self):
        return f"{type(self)}(name = {self._name}, startime = {self._startime}, endtime = {self._endtime}, quality = {self._quality}, location = {self._location})"
            
    # name attribute get, set, delete
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, n):
        # NEED TO implement object type check and deep copy
        self._name = copy(n)
    
    @name.deleter
    def name(self):
        del self._name

    # startime attribute get, set, delete
    @property
    def startime(self):
        return self._startime
    
    @startime.setter
    def startime(self, time):
        self._startime = copy(time)
    
    @startime.deleter
    def startime(self):
        del self._startime
    
    # endtime attribute get, set, delete
    @property
    def endtime(self):
        return self._endtime
    
    @endtime.setter
    def endtime(self, time):
        self._endtime = copy(time)
    
    @endtime.deleter
    def endtime(self):
        del self._endtime
    
    # quality attribute get, set, delete
    @property
    def quality(self):
        return self._quality
    
    @quality.setter
    def quality(self, qual):
        self._quality = copy(qual)
    
    @quality.deleter
    def quality(self):
        del self._quality
    
    # location attribute get, set, delete
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, loc):
        self._location = copy(loc)
    
    @location.deleter
    def location(self):
        del self._location
#-------------------------#

class Habit(Activity):
    def __init__(self, name, start, quality, location, amount):
        end = 0
        super().__init__(name,start,end,quality,location)
        self._amount = amount

    def __deepcopy__(self, memo):
        return Habit(\
            deepcopy(self._name, memo),\
            deepcopy(self._startime, memo),\
            deepcopy(self._quality, memo),\
            deepcopy(self._location, memo),\
            deepcopy(self._amount)\
            )

    def __str__(self):
        return super().__str__() + f", amount = {self._amount}"


    # amount attribute get, set, delete
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amt):
        self._amount = copy(amt)
    
    @amount.deleter
    def amount(self):
        del self._amount

    

#-------------------------#

class Rest(Activity):
    def __init__(self, name, start, end, quality, location, interuptions):
        super().__init__(name, start, end, quality, location)
        self._interuptions = interuptions
    
    def __deepcopy__(self, memo):
        return Rest(\
            deepcopy(self._name, memo),\
            deepcopy(self._startime, memo),\
            deepcopy(self._endtime, memo),\
            deepcopy(self._quality, memo),\
            deepcopy(self._location, memo),\
            deepcopy(self._interuptions)\
            )
    
    def __str__(self):
        return super().__str__() + f", interuptions = {self._interuptions}"

    # interuptions attribute get, set, delete
    @property
    def interuptions(self):
        return self._interuptions

    @interuptions.setter
    def interuptions(self, amount):
        self._interuptions = copy(amount)

    @interuptions.deleter
    def interuptions(self):
        del self._interuptions

#-------------------------#

class Exercise(Activity):
    def __init__(self, name, start, end, quality, location, intensity):
        super().__init__(name, start, end, quality, location)
        self._intensity = intensity

    def __deepcopy__(self, memo):
        return Exercise(\
            deepcopy(self._name, memo),\
            deepcopy(self._startime, memo),\
            deepcopy(self._endtime, memo),\
            deepcopy(self._quality, memo),\
            deepcopy(self._location, memo),\
            deepcopy(self.intensity)\
            )

    def __str__(self):
        return super().__str__() + f", intensity = {self._intensity}"

    # intensity attribute get, set, delete
    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, intens):
        self._intensity = copy(intens)

    @intensity.deleter
    def intensity(self):
        del self._intensity    