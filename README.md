# solid_principles_python
Refresher of SOLID Principles implemented with Python 

## SOLID

### 1. Single Responsibility Principle
A class should have only one job to reduce coupling. More responsibility means more coupling. 


### 2. Open-Closed Principle
Entities should be **Open** for **Extension** and **Closed** for **Modification**.

Code should be organized such that new modules can be added without the need to modify existing code to work.

### 3. Liskov Substitution Principle
If an entity S is a subtype of Entity T, then objects of type T should be replaceable by entities of 
type S without breaking functionality.


### 4. Interface Segregation Principle
A client should not be forced to depend on functions it does not use

Interface segregation principle is about making reasonable choices about how code will be
interfaced with.

### 5. Dependency Inversion Principle
* High level modules should not depend on Low level modules.
* High level modules should depend on abstractions.
* Abstractions should not depend on details.
* Details should depend on Abstractions.