# Understanding the Visitor Design Pattern

The visitor pattern is one of the 40 patterns in the original Gang of Four book
Design Patterns: Elements of Reusable Object-Oriented Software (1994) 

It is a behavioural design pattern that lets you separate algorithms from the objects on which they operate.

## Learning Goals
Be able to recognize the Visitor pattern when you see it in a codebase
Understand what problems the pattern solves 
Be able to recognize where Visitor pattern can be used to refactor legacy code
Understand the Pros and Cons of this pattern

## Connect
What patterns do you already know for dealing with behaviour switches based on type? 
(e.g. Strategy, Command)

### Define a domain:
An airline flight departure process at an airport. 
Passengers have different behaviour based on their ticket:
First class; Business; Premium Economy and Economy

### Scenarios:
#### Checkin
Ticket class allows passenger to join different queues, and to check in different baggage weight


#### Departure Lounge
Passengers wait in different departure lounges - Access is allowed or denied

#### Boarding Gate
Passengers present for boarding in order of their ticket class 
The gate opens for first class and business,
The gate denies boarding to premium economy and economy, until they are called

Show the existing code and highlight the switch statements on passenger type handling 
over a queue of passengers. 
Explain that if new behaviour is required each switch statement must be changed.

## Concept

Identify code complexity using the [Airport code kata](https://github.com/ronheywood/patternsgroup-visitor/tree/master)

The Visitor pattern can be used when you are working with complex object structure (for example, an object tree) of abstract types.
As you iterate the list, you find that you are having to identify the concrete type of the object and apply different logic based on that type

You can use the Visitor to delegate the business logic that needs to apply to these types onto the type itself, or its domain.

The pattern lets you make the logic implementation of your app more focused on their main jobs by extracting all other behaviours into a set of visitor classes.

Use the pattern when a behaviour makes sense only in some classes of a class hierarchy, but not in others.

You can extract this behaviour into a separate visitor class and implement only those visiting methods that accept objects of relevant classes, leaving the rest empty.

Demonstrate the Airport Visitor, replacing the switch statement in `Airport.AddPassenger` so that passengers are directed to the correct check in desk.
(The speakers notes in the [Powerpoint file in the repository](https://github.com/ronheywood/patternsgroup-visitor/blob/master/Visitor%20Pattern.pptx) contain code examples)

## Concrete Practice
Split into Implementation groups and practice implementing the pattern on the check in algorithm. And, optionally the Boarding gate

## Conclusions
### Visual reminder: 
Show the UML for the pattern

### Ask about Solid principles
How clean is this pattern? What other patterns are alternatives
Maybe try a mentimeter poll for other patterns that might work
Does the baggage weight algorithm cause an issue with encapsulation

### Pros
Open/Closed Principle. You can introduce a new behaviour that can work with objects of different classes without changing these classes.

Single Responsibility Principle. You can move multiple versions of the same behaviour into the same class.
A visitor object can accumulate some useful information while working with various objects. This might be handy when you want to traverse some complex object structure, such as an object tree, and apply the visitor to each object of this structure.

### Cons
You need to update all visitors each time a class gets added to or removed from the element hierarchy.

Visitors might lack the necessary access to the private fields and methods of the elements that they’re supposed to work with, twisting our arm into breaking encapsulation.