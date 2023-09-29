"""
Operator overloading
Operators can be overloaded to operate in a certain user-defined way. Its
corresponding method is invoked to perform its predefined function whenever an
operator is used. For example, when the + operator is called, it invokes the
special function, add, but this operator acts differently for different data
types. The + operator adds the numbers when it is used between two int data
types and merges two strings when used between string data types.
"""


class ComplexNumber:
    # Constructor
    def __init__(self):
        self.real = 0
        self.imaginary = 0
        # Set value function

    def set_value(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        # Overloading function for + operator

    def __add__(self, c):
        result = ComplexNumber()
        result.real = self.real + c.real
        result.imaginary = self.imaginary + c.imaginary
        return result
        # display results

    def display(self):
        print("(", self.real, "+", self.imaginary, "i)")


c1 = ComplexNumber()
c1.set_value(11, 5)
c2 = ComplexNumber()
c2.set_value(2, 6)
c3 = ComplexNumber()
c3 = c1 + c2
c3.display()

"""
->Static Polymorphism
1.-Polymorphism that is resolved during compile-time is known as static polymorphism.

2.-Method overloading is used in static polymorphism.

3.-Mostly used to increase the readability of the code.

4.-Arguments must be different in the case of overloading.

5.-Return type of the method does not matter.

6.-Private and sealed methods can be overloaded.

7.-Gives better performance because the binding is being done at compile-time.



->Dynamic Polymorphism

1.-Polymorphism that is resolved during runtime is known as dynamic polymorphism.

2.-Method overriding is used in dynamic polymorphism.

3.-Mostly used to have a separate implementation for a method that is already 
    defined in the base class.

4.-Arguments must be the same in the case of overriding.

5.-Return type of the method must be the same.

6.-Private and sealed methods cannot be overridden.

7.-Gives worse performance because the binding is being done at runtime.





"""
