# DIP
# Not related to dependency injection
# High level modules should not depend on low-level modules, just abstractions
# Depend on interfaces
from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

# Part of fix
#  Can be used to help with unit testing
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


# Storing relationships between people
# added RelationshpBrowser as fix
# Low level module
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.extend([
            (parent, Relationship.PARENT, child),
            (child, Relationship.CHILD, parent)]
        )
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# High level module
# - uses functionality lower to hardware
class Research:
    # def __init__(self, relationships):
    #     # Relationships is what stores the relationship, and if we change
    #     #  our storage mechanism in the lower module, we will break this
    #     #  higher level module.
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child named {r[2].name}.')
    # Fix would be creating a search method
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child named {p}.')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
