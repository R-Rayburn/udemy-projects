class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    person_count = 0
    def create_person(self, name):
        person = Person(self.person_count, name)
        self.person_count += 1
        return person
        