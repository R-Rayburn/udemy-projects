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