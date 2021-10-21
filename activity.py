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

class Habit(Activity):
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



sleep = Activity()
smoking = Habit()

print(f'smoking truth value is {smoking.occured}')

smoking.occured = True

print(f'smoking truth value is {smoking.occured}')