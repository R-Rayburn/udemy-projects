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
_Builder_ | When piecewise object construction is complicated, provide an API for doing it succinctly
### Motivation
- Some objects are simple and can be created in a single initializer call
- Other objects require a lot of ceremony to create
- Having an object with 10 initializer arguments is not productive
- Instead, opt for piecewise construction
- Builder provides an API for constructing an object step-by-step


### Summary
- A builder is a separate component for building an object
- Can either give builder an initializer or return it via a static function
- To make builder fluent, return self in every method
- Different facets of an object can be built with different builders working in tandem via a base class

## Factories
_Factory_ | A component rewponsible solely for the wholesale (not piecewise) creation of objects.
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
### Summary
- A _factory method_ is a static method that creates objects
- A factory is an entity that can take care of object creation
- A factory can be external or reside in the object as an inner class
- Hierarchies of factories can be used to create related objects.

## Prototype
_Prototype_ | A partially or fully initialized object that you copy (clone) and make use of.
### Motivation
- Complicated objects (eg. cars) arent' designed from scratch
  - They reiterate existing designs
- An existing (partially or fully constructed) design is a Prototype
- We make a copy (clone) the prototype and customize
  - requires 'deep copy' support
- We make the cloning convenient (e.g., via a Factory)


### Summary
- To implement a prototype, partially construct an object and store it somewhere
- Deep copy the prototype
- Customize the resulting instance
- A factory provides a convenient API for using prototypes

## Singleton
_Singleton_ | A component which is instantiated only once.
### Motivation
- For some components, it only makes sense to have one in the system
  - Database repository
  - Object factory
- E.g., the initializer call is expensive
  - We only do it once
  - We provide everyone with the same instance
- Want to prevent anyone creating additional copies
- Need to take care of lazy instantiation
### Summary
- Different realizations of Singleton: custom allocation, decorator, metaclass
- Laziness is easy, just initialize first request
- Monostate variation
- Testability issues
  - Solved by crating mocks and injecting data

## Adapter
_Adapter_ | A construct which adapts an existing interface X to conform to the required interface Y.
### Motivation
- We have devices that require different interface requirements
- We cannot modify our devices to support every possible interface
- Thus we use an adapter to give us the interface we need from the interface we have

### Summary
- Implementing an Adapter is easy
- Determine the API you have and the API you need
- Create a component which aggregates (has a reference to) the adaptee
- Intermediate representations can pile up: use caching and other optimizations.

## Bridge
_Bridge_ | A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
### Motivation
- Bridge prevents a 'Cartesian product' complexity explosion
- Eample:
  - Base calss ThreadScheduler
  - Can be preemptive or cooperative
  - Can run on Windows or Unix
  - End up wiht aa 2x2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS
- Bridge pattern avoids the entity explosion

#### Before
ThreadScheduler <- PreemptiveThreadScheduler
ThreadScheduler <- CooperativeThreadScheduler
PreemptiveThreadScheduler <- WindowsPTS
PreemptiveThreadScheduler <- UnixPTS
CooperativeThreadScheduler <- WindowsCTS
CooperativeThreadScheduler <- UnixCTS

#### after
IPlatformScheduler <- ThreadScheduler.platformScheduler
IPlatformScheduler <- UnixScheduler
IPlatformScheduler <- WindowsScheduler
ThreadScheduler <- PreemptiveThreadScheduler
ThreadScheduler <- CooperativeThreadScheduler

### Summary
- Decouple abstraction from implementation
- Both can exist as hierarchies
- A stronger form of encapsulation


## Composite
_Composite_ | A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.
### Motivation
- Objects use other objects' properties/members through inheritance and composition
- Composition lets up make compound objects
  - E.g., a mathematical expression composed of simple expressions; or
  - A grouping of shapes that consists of several shapes
- Composite design pattern is used to treat both single (scalar) and composite objects uniformly
  - I.e., Foo and Sequence (yielding Foo's) have common APIs
### Summary
- Objects can use other objects via inheritance/composition
- Soome composed and singular objects need similar/identical behaviors
- Composite design pattern lets us treat both types of objects uniformly
- Python supports iteration with `__iter__` and the `Iterable` ABC
- A single object can make itself iterable yileding self from `__iter__`

## Decorator
_Decorator_ | Facilitates the addition of behaviors to individual objects without inheriting from them.
### Motivation
- Want to augment an object with additional functionality/features
- Do not want to rewrite or alter existing code (OCP)
- Want to keep the new functionality separate (SRP)
- Need to be able to interact with existing structures
- Two options:
  - inherit from required object (if possible)
  - build a Decorator, which simply references the decorated object(s)