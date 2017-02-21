'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says: 

'''

# Write your code here:

class Animal:
    def __init__(self, name, pet, sound):
        self.name = name
        self.pet = pet
        self.sound = sound

    def description(self):
        return "{} the {}".format(self.name, self.pet)

    def speak(self):
        return '{}'.format(self.sound)

    def emote(self):
        print("{} says: {}".format(self.description(), self.speak()))


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog", "Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat", "Meow!")


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, "Fish", "")

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
