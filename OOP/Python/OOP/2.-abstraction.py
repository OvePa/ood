class Circle:
    def __init__(self):
        self.radius = 0
        self.pi = 3.142

    def __init__(self, r):
        self.radius = r
        self.pi = 3.142

    def area(self):
        return self.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.pi * self.radius


def main():
    circle = Circle(5)
    print("Area {:.2f}".format(circle.area()))
    print("Perimeter {:.2f}".format(circle.perimeter()))


if __name__ == "__main__":
    main()

"""
->Abstraction

1.-It focuses on the design level of the system.

2.-It hides unnecessary data to simplify the structure.

3.-It highlights the work that the object performs.

4.-Abstraction means to hide implementation using interface and abstract classes.


->Encapsulation

1.-It focuses on the application level of the system.

2.-It restricts access to data to prevent its misuse.

3.-It deals with the internal working of the object.

4.-Encapsulation means to hide data using getter and setter functions.


"""
