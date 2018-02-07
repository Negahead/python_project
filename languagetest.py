import b
from dir1.python_in_1 import *

a = 100


class Person:
    age = 23

    def __init__(self,name):
        print("init Person class")
        print(self)
        self.name = name
        self.origin = "china"

    def greeting(self, greet="hello"):
        print(self.name + " says " + greet)


class Faker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        print(self)
        print("init Faker class")
        self.game = "overwatch"

    def LOL(self):
        print(self)

    def greeting(self, greet="hello"):
        print("fuck you!")


class Overloaded:
    def __init__(self, start):
        self.data = start

    def __add__(self, other):
        print(other)
        return Overloaded(self.data + other)

    def __radd__(self, other):
        print(other)
        return Overloaded(self.data + other)

    def __del__(self):
        print("deleting object")

    def __getitem__(self, i):
        print("item is ")
        print(i)
        return "invoking __getitem__"


class Squares:
    # __slots__ means no __dict__ by default
    # to allow __dict__ creation while subclassing slotted Objects,just add '__dict__' the the __slots__
    # attributes no exist in __slots__ will only be find in __dict__
    # dir(obj) ,only include attr name in __slots__ besides the basic
    #__slots__ = ['value', 'stop', 'no', '__dict__']

    # _Squares__x
    __x = 'shame'

    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        print("invoking __iter__")
        return self

    def __next__(self):
        print("invoking __next__")
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

    def __getattr__(self, attrName):
        if attrName == 'age':
            print("invoking __getattr__")
            return 40
        else:
            pass

    def getage(self):
        print("get age...")
        return 40

    def setage(self, val):
        print("setting age...")
        print("value is " + val)
        pass

    # Squares.foo(1) will raise a TypeError
    def foo(self, x):
        print("executing foo %s,%s" % (self, x))

    # you intend to call it from the class rather than from a class instance
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo %s,%s" % (cls, x))

    # obj.static_foo(1) or Squares.static_foo(1) will both be ok
    @staticmethod
    def static_foo(x):
        print("executing static_foo %s" % x)

    age = property(getage, setage, None, '')

    @property
    def my_property(self):
        print("getting my_property")
        return 100000

    @my_property.setter
    def my_property(self,value):
        print("setting my_property")

    @my_property.deleter
    def my_property(self):
        print("deleting my_property")


if __name__ == "__main__":

    print(Person.__members__)

