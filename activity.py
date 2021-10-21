# File containing activity class and it's children

class Activity:
    def __init__(self):
        self._duration = 0
    
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, time):
        self._duration = time

    @duration.deleter
    def duration(self):
        del self._duration

#-------------------------#

class Practice(Activity):
    def __init__(self):
        Activity.__init__(self)
        self._occured = False

    @property
    def occured(self):
        return self._occured
    
    @occured.setter
    def occured(self, bool):
        self._occured = bool
    
    @occured.deleter
    def occured(self):
        del self._occured



#-------------------------#

class Daily(Activity):
    def __init__(self, quality):
        Activity.__init__(self)
        self._quality = quality

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, expression):
        self._quality = expression

    @quality.deleter
    def quality(self):
        del self._quality

