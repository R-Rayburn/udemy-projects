# LSP
# - idea is an interface that takes a base class can allow a derived class to be inserted

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
    
    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected} got {rc.area}')

rc = Rectangle(2,3)
use_it(rc)

# Breaks the Principle
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.width.setter
    def height(self, value):
        self._width = self._height = value

sq = Square(5)
use_it(sq)
# use_it now only works on Rectangle
# rc.height = 10 also changes the width, and the function uses a
#  previous version of the width
#  To correct, we can remove the Square class, have a factory_method
# The setters in these examples are what violate the principle