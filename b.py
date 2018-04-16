def spam(text):
    print(text, 'spam')


name1 = "Just another perl hacker"


def _you_known(text):
    pass


class A1:
    name_a1 = 'faker'

    def __init__(self, **kwargs):
        self._chaplin = 1000
        self.time = ''

    def greeting(self, age):
        raise NotImplementedError

    def new(self):
        pass


class A(A1):
    name = 'dopa'

    def __init__(self, *args, **kwargs):
        self.age = 200
        self._chaplin = 100
        # print(self)
        super(A1, self).__init__()

    def __str__(self):
        return 'age is {0},chaplin is {1}'.format(self.age, self._chaplin)

    def __repr__(self):
        return "represent"

    def _bitty_boppy_betty(self):
        print("Siri is so stupid!")

    def greeting(self, age=0, n=''):

        print("hello world")


class B:
    def __init__(self):
        self.name = 'will'

    def cast(self):
        return (A)(self)


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        self.i = 0

    def __call__(self, *args, **kwargs):
        print("why you are calling me ?")

    def __setitem__(self, key, value):  # p[0] = 100, key is 0,value is 100
        print(key)
        print(value)

    def __getitem__(self, item):  # p[0]
        print(item)

    def __iter__(self):
        print("you sure you want to iterate me ?")  # only called once
        return self

    def __next__(self):
        print("next me is always the same")
        if self.i == 10:
            raise StopIteration
        self.i += 1
        return self.i

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = self.pay * (1 + percent)

    def _can_you_access(self):  # you can still access this method
        print("can you?")  # yes

    def __can_you(self):
        print("can you really?")  # no

    def __str__(self):
        return '[Person: {0},{1:.2f}]'.format(self.name, self.pay)

    def greeting(self, data_file):
        if not hasattr(data_file, 'read'):
            raise ValueError("expecting a file-like object")
        print("Hello World")

    @staticmethod
    def foo():  # access via Person.foo() only
        print("static method foo")

    @classmethod
    def class_method(cls, name):  # Person.class_method('faker')
        print(cls)  # <class '__main__.Person'>
        print("this is a class method")
        faker = cls('faker', 'gamer', 2000000000)
        print(faker.last_name())
        print(name)


class Manager(Person):
    def __init__(self, name, job=None, pay=0):
        self._prop = 'hhgh'
        super().__init__(name, job, pay)
        #   super(Manager, self).__init__(name, job, pay) ,  super(Person, self).__init__()  in python 2
        print(self.last_name())

    def __getattr__(self, item):  # undefined attribute,those attributes not stored on an instance or not inherited
        if item == 'bar':         # __getattribute__ will intercept ALL attribute retrieve,avoid possible infinite loop
            return 'bar attr'
        else:
            print('getattr not bar')

    # def __getattribute__(self, item):
    #     super().__getattribute__(item)                              #   x = self.other,LOOP!

    def ___setattr__(self, key, value):  # when any attribute is set
        print("setting attr using __dict__")
        self.__dict__[key] = value  # try to avoid infinite loop

    @property  # second choice besides __setattr__
    def prop(self):
        print("fetching")
        return self._prop

    @prop.setter
    def prop(self, value):
        print("changing")
        self._prop = value

    @prop.deleter
    def prop(self):
        print("deleting")
        del self._prop

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent)


if __name__ == '__main__':
    m = Manager('Tom', 'Mgr', 50000)
    m.give_raise(0.1)
    print(m)

    p = Person("Me", "employee", 10000)
    Person.class_method('faker')
    print("==============================")
    print(m.prop)
    m.prop = 'new property'
    print(m.prop)
    try:
        m.asdaf()
    except (TypeError):
        print()
    if hasattr(p, 'job1'):
        print("has attr")





