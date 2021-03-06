'''
>>> f(3,4)
7

>>> f(4,3)
Traceback (most recent call last):
...
TypeError: Incorrect return type

>>> a_to_upper("alpha")
'ALPHA'
>>> a_to_upper("Andrew")
'ANDREW'

>>> a_to_upper("Bart")
Traceback (most recent call last):
...
TypeError: Incorrect return type

>>> a_to_upper("Zed")
Traceback (most recent call last):
...
TypeError: Incorrect return type


'''

# Implement your returns decorator here:

def returns(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret_val = func(*args, **kwargs)
            if not isinstance(ret_val, type):
                raise TypeError('Incorrect return type')
            return ret_val
        return wrapper
    return decorator




# Do not edit any code below this line!

@returns(int)
def f(x, y):
    if x > 3:
        return -1.5
    return x + y

@returns(str)
def a_to_upper(s):
    if s.startswith('a') or s.startswith('A'):
        return s.upper()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.
