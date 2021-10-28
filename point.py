class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return "({0}, {1})".format(self._x, self._y)

    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, new_y):
        self._y = new_y

p1 = Point(2, 3)
print(p1.y)

diction = {
    "a" : "a string",
    "b" : 5
}

# print(type(str(diction)))
# print(str(diction))

# print(type(diction))
# print(diction)

str_d = str(diction)
print(type(str_d))
print(str_d)
dict_d = dict(str_d)