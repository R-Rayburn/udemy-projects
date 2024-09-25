from math import *

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    
# # Can move this into the class
# class PointFactory:
#     @staticmethod
#     def new_cartesian_point(x, y):
#         return Point(x, y)
    
#     @staticmethod
#     def new_polar_point(rho, theta):
#         return Point(rho * cos(theta), rho * sin(theta))
    
    # Good to have if there is other state info we want to store
    #  other types of factories that have non-static elements in it
    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)
        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))
    
    factory = PointFactory()

if __name__ == '__main__':
    p = Point(2, 3)
    # when factory is outside of class
    # p2 = PointFactory.new_polar_point(1,2)
    p2 = Point.factory.new_polar_point(1,2)
    print(p)
    print(p2)