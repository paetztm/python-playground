'''
>>> evens = evens_up_to(8)
>>> type(evens)
<type 'generator'>
>>> for even in evens:
...     print(even)
2
4
6
8

>>> squares = squares_up_to(16)
>>> type(squares)
<type 'generator'>
>>> for square in squares:
...     print(square)
1
4
9
16

>>> for square in squares_up_to(15):
...     print(square)
1
4
9

>>> counter = countdown(3)
>>> type(counter)
<type 'generator'>
>>> for count in countdown(3):
...     print(count)
3
2
1
BLASTOFF!

>>> for count in countdown(10):
...     print(count)
10
9
8
7
6
5
4
3
2
1
BLASTOFF!

'''

# Write your code here:


def evens_up_to(max):
    val = 2
    while val <= max:
        yield val
        val += 2


def squares_up_to(max):
    square, count = 1, 1
    while square <= max:
        yield square
        count += 1
        square = count**2



def countdown(max):
    for i in reversed(range(1, max+1)):
        yield i
    yield 'BLASTOFF!'
# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.