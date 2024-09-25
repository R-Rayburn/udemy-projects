from enum import Enum
from math import *

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     # Impossible, cannot re-declare init
#     # def __init__(self, rho, theta):

# If we want another coordinate system, we will have
#  to modify enum and class for new code (breaks open-close)
# class CoordinateSystem(Enum):
#     CARTESIAN = 1
#     POLAR = 2

# class Point:
#     # These a,b variable naming is poor and not understood easily
#     def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
#         if system == CoordinateSystem.CARTESIAN:
#             self.x = a
#             self.y = b
#         elif system == CoordinateSystem.POLAR:
#             self.x = a * cos(b)
#             self.y = a * sin(b)


# Allows better names for methods that make sense.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.new_polar_point(1,2)
    print(p)
    print(p2)