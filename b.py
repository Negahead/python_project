def spam(text):
    print(text,'spam')


def _you_knwon(text):
    pass


class A:
    def __init__(self):
        print(self.__dict__)


class B:
    def __init__(self):
        self.name = 'will'

    def cast(self):
        return (A)(self)


b_obj = B()



