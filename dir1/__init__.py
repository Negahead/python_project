print("hello in dir1 __init__")
name = "rookie"

from .python_in_1 import  A


__all__ = ['python_in_1', 'relative_in_1']

class B:
    pass