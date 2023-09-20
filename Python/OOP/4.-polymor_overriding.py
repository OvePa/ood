"""
Method overriding
In object-oriented programming, if a subclass provides a specific implementation
of a method that had already been defined in one of its parent classes, it is
known as method overriding.
"""


class Animal:
    def __init__(self):
        pass

    def print_animal(self):
        print("I am from the animal class!")

    def print_animal_two(self):
        print("I am from the Animal class!")


class Lion(Animal):
    def print_animal(self):  # method overriding
        print("I am from the Lion class!")


if __name__ == "__main__":
    lion = Lion()
    lion.print_animal()
    lion.print_animal_two()
    print(Lion.__mro__)
