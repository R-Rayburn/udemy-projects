import copy

class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return f'{self.name} lives at {self.address}'


if __name__ == '__main__':
    john = Person('John', Address('123 Main St', 'Nashville', 'USA'))
    print(john)

    jane = john
    jane.name = 'Jane'
    print('---')
    # these will print exactly the same due to reference assignment
    print(john)
    print(jane)

    # We want to make use of a 'copy'
    # Can do it by setting address as a separate value, and then do
    # jane = Person('Jane', address)

    # Does a recursive copy of values
    john = Person('John', Address('123 Main St', 'Nashville', 'USA'))
    jane = copy.deepcopy(john)
    # Now chagnes to Jane or John will not modify the other.

    # The goal of this is to be able to use a single
    #  object. Duplication is reduced.