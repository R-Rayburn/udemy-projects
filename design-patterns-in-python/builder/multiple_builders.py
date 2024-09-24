class Person:
    def __init__(self):
        # address info
        self.street_address = None
        self.postcode = None
        self.city = None
        #employment
        self.company_name = None
        self.position = None
        self.annual_gross = None

    def __str__(self):
        return f'Address: {self.street_address}, '\
        f'{self.postcode}, {self.city}\n'\
        f'Employed at {self.company_name} as a '\
        f'{self.position} earning {self.annual_gross}.'


class PersonBuilder:
    # Adding the default allows sub-builders to work with an existing object.
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self
    def as_a(self, position):
        self.person.position = position
        return self
    def earning(self, annual_gross):
        self.person.annual_gross = annual_gross
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)
    def at(self, street_address):
        self.person.street_address = street_address
        return self
    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self
    def in_city(self, city):
        self.person.city = city
        return self

pb = PersonBuilder()
person = pb\
    .lives\
        .at('123 London Road')\
        .in_city('london')\
        .with_postcode('swi43ad')\
    .works\
        .at('Fab')\
        .as_a('Engineer')\
        .earning(10000)\
    .build()
print(person)