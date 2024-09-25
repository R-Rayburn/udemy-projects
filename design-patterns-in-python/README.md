## SOLID Principles
### Single Responsibilty Principle
- A class should only have one reason to change.
- _Separation of concerns_ - different classes handling different, idempotent tasks/problems
### Open-Closed Principle
- Classes should be open for extension, but closed for modification.
- Specification Pattern
- Already written and tested classes should not be modified. New code should be written to inherit from.
### Liskov Substitution Principle
- You should be able to substitute a base type for a subtype
### Interface Segregation Principle
- Don't put too much into an interface; split into separate interfaces
- YAGNI - You Ain't Going to Need It
### Dependency Inversion Principle
- high-level modules should not depend on low level ones; use abstractions.

## Gamma Categorization
- Design Patters are typically split into three categories
- named after Erich Gamma, one of GoF authors
### Creational Patterns
- Deal with creation (construction) of objects
- Explicit (constructor) vs implicit (DI, reflection, etc)
- Wholesale (single statement) vs piecewise (step-by-step)

### Structural Pattern
- Concerned with structure (eg class members)
- Many patterns are wrappers that mimic underlying class' interface
- Stress the importance of good API design

### Behavioral Patterns
- They are all different; no central theme
- Solve a particular problem in a particular way.

## Builder Design Pattern
### Motivation
- Some objects are simple and can be created in a single initializer call
- Other objects require a lot of ceremony to create
- Having an object with 10 initializer arguments is not productive
- Instead, opt for piecewise construction
- Builder provides an API for constructing an object step-by-step

_When piecewise object construction is complicated, provide an API for doing it succinctly_
### Summary
- A builder is a separate component for building an object
- Can either give builder an initializer or return it via a static function
- To make builder fluent, return self in every method
- Different facets of an object can be built with different builders working in tandem via a base class

## Factories
### Motivation
- Object creation logic becomes too confoluted
- Initializer is not descriptive
  - name is always `__init__`
  - cannot overload with same sets of arguments with different names
  - can turn into 'optional parameter hell'
- Wholesale object creation (non-pieccewise, unlike Builder) can be outsourced to
  - a separate method (factory method)
  - that may exist in a separate class (factory)
  - can create hierarchy of factories with abstract factory
- Factory: A component rewponsible solely for the wholesale (not piecewise) creation of objects.
### Summary
- A _factory method_ is a static method that creates objects
- A factory is an entity that can take care of object creation
- A factory can be external or reside in the object as an inner class
- Hierarchies of factories can be used to create related objects.