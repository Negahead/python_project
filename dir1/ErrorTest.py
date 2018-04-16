import sys

class A:
    pass


def value_error():
    try:
        int('as')    #  it's getting the right type, but it's still not a value that it can convert.
    except ValueError:
        print("value error")
        print("unicode_decode_error_handler must be a string ")
    if not 'self.parent':
        raise ValueError(
            "Cannot replace an element with its contents when that"
            "element is not part of a tree.")


def import_error():
    try:
        import simplejson as json
    except ImportError:
        import json


def type_error(parameter, *args):
    try:
        int({})
    except TypeError:
        print("type error")
        print("tzinfo must be an instance of datetime.tzinfo")
        print("$numberInt must be string: %s")

    if not isinstance(parameter, int):
        raise TypeError("parameter is not a int type")
    if len(args) > 1:
        raise TypeError("pop expected at most 2 arguments, got " \
                        + repr(1 + len(args)))


def run_time_error():
    raise RuntimeError("run time error")



def key_error():
    d = {}
    try:
        x = d['not_exist']
    except KeyError:
        print("key is not found in the dictionary")
        # raise KeyError("key is not found in the dictionary")


def index_error():
    d = []
    try:
        x = d['s']
    except IndexError:
        print("index error")
    except TypeError:
        print("you should use an integer key")


def zero_division_error():
    try:
        1 / 0
    except ZeroDivisionError:
        print("divided by zero")


def abstract_method():
    raise NotImplementedError("this method is not implemented")


def attribute_error():
    a = A()
    if hasattr(a,'dopa'):
        print("I have this attr")
    try:
        n = a.name
    except AttributeError:
        print("a has no attribute")


def IO_error():
    try:
        sys.stdout.write('.')
        sys.stdout.flush()
    except IOError as e:
        # sys.stdout.flush doesn't work in pythonw
        print(e.errno)
        pass


if __name__ == '__main__':
    IO_error()