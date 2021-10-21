# File containing activity class and it's children

class Activity:
    def __init__(self, name, start, end, quality, location):
        self._name = name
        self._startime = start
        self._endtime = end
        self._quality = quality
        self._location = location

    # name attribute get, set, delete
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, bool):
        self._name = bool
    
    @name.deleter
    def name(self):
        del self._name

    # startime attribute get, set, delete
    @property
    def startime(self):
        return self._startime
    
    @startime.setter
    def startime(self, bool):
        self._startime = bool
    
    @startime.deleter
    def startime(self):
        del self._startime
    
    # endtime attribute get, set, delete
    @property
    def endtime(self):
        return self._endtime
    
    @endtime.setter
    def endtime(self, bool):
        self._endtime = bool
    
    @endtime.deleter
    def endtime(self):
        del self._endtime
    
    # quality attribute get, set, delete
    @property
    def quality(self):
        return self._quality
    
    @quality.setter
    def quality(self, bool):
        self._quality = bool
    
    @quality.deleter
    def quality(self):
        del self._quality
    
    # location attribute get, set, delete
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, bool):
        self._location = bool
    
    @location.deleter
    def location(self):
        del self._location
#-------------------------#

class Habit(Activity):
    def __init__(self, name, start, end, quality, location, amount):
        Activity.__init__(self, name, start, end, quality, location)
        self._amount = amount

    # amount attribute get, set, delete
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amt):
        self._amount = amt
    
    @amount.deleter
    def amount(self):
        del self._amount



#-------------------------#

class Rest(Activity):
    def __init__(self, name, start, end, quality, location, interuptions):
        Activity.__init__(self, name, start, end, quality, location)
        self._interuptions = interuptions

    # interuptions attribute get, set, delete
    @property
    def interuptions(self):
        return self._interuptions

    @interuptions.setter
    def interuptions(self, amount):
        self._interuptions = amount

    @interuptions.deleter
    def interuptions(self):
        del self._interuptions

#-------------------------#

class Exercise(Activity):
    def __init__(self, name, start, end, quality, location, intensity):
        Activity.__init__(self, name, start, end, quality, location)
        self._intensity = intensity

    # intensity attribute get, set, delete
    @property
    def intensity(self):
        return self._intensity

    @intensity.setter
    def intensity(self, amount):
        self._intensity = amount

    @intensity.deleter
    def intensity(self):
        del self._intensity    