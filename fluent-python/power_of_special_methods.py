from collections import namedtuple

import math

import itertools

Card = namedtuple('Card', ['rank', 'suit'])

beer_card = Card('7', 'diamonds')
print(dir(beer_card))
my_copy = eval(repr(beer_card))
print(my_copy == beer_card)
print(my_copy is beer_card)
print(id(my_copy))
print(id(beer_card))


class FrenchDeck:
    ranks = [str(rank) for rank in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

print(len(deck))

print(deck[0])
print(deck[:3])
print(deck[12::13])
print(Card('Q', 'hearts') in deck)
print(Card('Z', 'clubs') in deck)

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)


print(sorted(deck))


def spades_high(my_card):
    rank_value = FrenchDeck.ranks.index(my_card.rank)
    return rank_value, my_card.suit

print(sorted(deck, key=spades_high))

import random
print(random.choice(deck))

try:
    random.shuffle(deck)
except TypeError as e:
    print(repr(e))
else:
    print('The deck was shuffled!')

def put(deck, index, card):
    deck._cards[index] = card

FrenchDeck.__setitem__ = put

try:
    random.shuffle(deck)
except TypeError as e:
    print(repr(e))
else:
    print('The deck was shuffled!')

#del FrenchDeck.__setitem__
#random.shuffle(deck)

from array import array


class Vector:
    def __init__(self, components):
        self._components = array('d', components)

    def __repr__(self):
        components_str = ', '.join(str(x) for x in self._components)
        return '{}([{}])'.format(self.__class__.__name__, components_str)

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __mul__(self, other):
        try:
            return Vector(x * other for x in self)
        except TypeError:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0)
            return Vector(x + y for x, y in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

v1 = Vector([2, 4, 6])
print(v1)
x, y, z = v1  # tuple unpacking
list(v1), set(v1)  # seed collection constructors

for label, value in zip('xyz', v1):
    print(label, '=', value)

