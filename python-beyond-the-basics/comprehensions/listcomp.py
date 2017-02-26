'''To start, define a few number lists. Be sure to create each one
with a list comprehension; don't use a for loop. Use range() for the
base sequence.

>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64]

>>> cubes
[0, 1, 8, 27, 64, 125]

>>> squares_of_evens
[0, 4, 16, 36, 64]

Next, define a function called "palindromes" that takes a list of
strings as input, and (using a list comprehension) constructs and
returns a list of palindromes.  (A palindrome is a string that is the
same backwords and forwards, like "abccba". Hint: in Python, the
reverse of a string "s" is written "s[::-1]".)

>>> palindromes(["foo", "bar"])
['foooof', 'barrab']

>>> palindromes(["ab", "cat", "q", "qq"])
['abba', 'cattac', 'qq', 'qqqq']

>>> palindromes(["abc", "xyz"])
['abccba', 'xyzzyx']

Here are some name lists:

>>> names = ["Albert", "Fred", "Amanda", "Tim", "Joe", "Aaron"]
>>> names2 = ["George", "Gus", "Aaron", "Ted", "Gina"]

Write a function "starting_with" that gives you names starting with a
certain letter. Its body should just have a return statement,
returning a list comprehension.

>>> starting_with("A", names)
['Albert', 'Amanda', 'Aaron']
>>> starting_with("F", names)
['Fred']
>>> starting_with("G", names2)
['George', 'Gus', 'Gina']
>>> starting_with("A", names2)
['Aaron']

Make it case-insensitive too:
>>> starting_with("a", names)
['Albert', 'Amanda', 'Aaron']
>>> starting_with("g", names2)
['George', 'Gus', 'Gina']

'''

# Write your code here:
# [ EXPRESSION for VARIABLE in SEQUENCE if CONDITION]
import datetime
import numpy

squares = [x**2 for x in range(9)]

cubes = [x**3 for x in range(6)]

squares_of_evens = [x**2 for x in range(9) if x % 2 == 0]


def palindromes(items):
    return [x + x[::-1] for x in items]


def starting_with(char, names):
    return [name for name in names if name[0].lower() == char.lower()]



def squares_up_to(max):
    square, count = 1, 1
    while square <= max:
        yield square
        count += 1
        square = count**2


def max_square(val):
    return int(numpy.sqrt(val))

import math
def perfect_square_generator(max_square):
    if math.sqrt(max_square) == 1:
        pass

def next_value(area, perfect_square):
    print("{} - {} ** 2 = {} = {}".format(area, perfect_square, perfect_square**2, (area-(perfect_square**2))))
    return area - (perfect_square**2)


def answer2(area):
    solution = []

    while area > 0:
        x = max_square(area)
        squared = x**2
        while area - squared >= 0:
            area -= squared
            solution.append(squared)
    return solution

import time
total_time = 0
def answer(area):
    # your code here

    if area == 1:
        return [1]

    squares = [x ** 2
           for x in range(1, area)
           if x ** 2 <= area]
    solution = []

    for x in sqs[::-1]:
        while area - x >= 0:
            area -= x
            solution.append(x)

    return solution

start_time = time.time()
#for i in range(55):
print(answer(999999))
total_time += time.time() - start_time
print(total_time)
#print(answer2(1200))
#print (time_dict)
# print(int(max_square(1000000-1)))
# print(next_value(1000000-1, max_square(1000000-1)))
# print(max_square(1998))
# print(numpy.sqrt(1936))
# print(answer2(1000000))
# for i in range(100):
#     val = answer(i)
#     print(val)
# Do not edit any code below this line!


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
