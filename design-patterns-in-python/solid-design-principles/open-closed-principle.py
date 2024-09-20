# OPC
# - Open for extension, closed for modification
# - Can keep growing and cause issues with future additions
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    
    # violates open-close
    # - We modified this class instead of extending it
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p

# Number of criteria causes these filters to grow

# Specification (Enterprise Pattern)

class Specification:
    def is_satisified(self, item):
        pass
    
    def __and__(self, other):
        return AndSpecification(self, other)

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    def is_satisified(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    def is_satisified(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    def is_satisified(self, item):
        return all(map(
            lambda spec: spec.is_satisified(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisified(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Old approach of ProductFilter
    pf = ProductFilter()
    print('Green products (old)')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'\t{p.name} is green')

    # New Specification Approach
    bf = BetterFilter()
    print('Green products (new)')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'\t{p.name} is green')

    print('Large products:')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f'\t{p.name} is large')

    print('Large blue items:')
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    # OVERRIDE & EXAMPLE IN BASE CLASS
    # large_blue = large & ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f'\t{p.name} is large and blue')

# This allows us to create new crieteria that will not break old