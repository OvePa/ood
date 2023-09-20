"""
Static polymorphism
Static polymorphism is also known as compile-time polymorphism, and it is
achieved by method overloading or operator overloading.

Method overloading
Methods are said to be overloaded if a class has more than one method with the
same name, but either the number of arguments is different, or the type of
arguments is different. We have implemented method overloading using two
functions with the same name but with different numbers of arguments. You can
see this in the implementation below.
"""


class Sum:
    def addition(self, a, b, c=0):
        return a + b + c


sum = Sum()
print(sum.addition(14, 35))
print(sum.addition(31, 34, 43))

"""---------------------------------------"""


class Area:
    def calculateArea(self, length, breadth=-1):
        if breadth != -1:
            return length * breadth
        else:
            return length * length


area = Area()
print("Area of rectangle = " + str(area.calculateArea(3, 4)))
print("Area of square = " + str(area.calculateArea(6)))
