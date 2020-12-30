---
layout: learning_hour
title: The Dependency Inversion Principle
parent: Testable Design
grand_parent: Learning Hours
nav_order: 1
---


The Dependency Inversion Principle
-----------------------------------

This is one of the 5 SOLID principles outlined in Robert C. Martin's book "Agile Software Development Principles, Patterns and Practices". In this session we work on some code that breaks the principle and is also difficult to write unit tests for.

## Session Outline
 
* 5 min connect: pairs discuss design principles
* 10 min concept: present SOLID and DIP in particular
* 15 min do: TirePressure in pairs 
* 5 min concept: why is this hard to test?
* 15 min do: TirePressure in pairs
* 5 min conclusions: describe DIP in own words 

### Connect: Design Principles
The theme is design principles in software. Read the list of topics below. Add an upvote to those that refer to good design principles, add a downvote to those that are signs of bad design. Leave irrelevant topics without a vote.

- Travelling Salesman
- Barbara Liskov
- Polymorphism
- Dependency Inversion
- Arrange - Act - Assert
- Big Ball of Mud
- Single Responsibility
- Spaghetti code
- Loose Coupling
- Artificial Intelligence

### Concept
The focus today is the Dependency Inversion Principle. You could explain that Dependency Injection is a concrete strategy to achieve Dependency Inversion. You could show the [wikipedia page](https://en.wikipedia.org/wiki/Dependency_inversion_principle).

### Do
I have a collection of 5 exercises each of which has a problem with one or more design principle - the [Racing Car Katas](https://github.com/emilybache/Racing-Car-Katas). The one I would start with is Tire Pressure. It has an obvious Dependency Inversion Principle violation and is quite a small amount of code. Ask people to get it under test without changing the production code. In some languages this is well nigh impossible, in others it's just awkward.

### Concept
Stop the group when at least some pairs have discovered the problem and start asking you if they really are not allowed to change the code. Ask someone to explain the problem to the group. (The dependency on the Sensor is awkward since you can't control what pressure reading it gives). Ask if anyone can relate this to the Dependency Inversion Principle. Hopefully someone will explain it to the group. If not, go through it yourself. (The Alarm has a dependency on a detail - Sensor - rather than an abstraction).

### Do
Ask them to continue to work on the same exercise, but now they are allowed to change the code to solve the DIP violation. Let them create an abstraction for the TirePressureMonitor have the Alarm class depend on that instead of a concrete class. They should find it possible to write tests for the class now, using a stub implementation of the abstraction.

If that goes quickly, consider doing the TextConverter problem as well in a similar way.

### Conclusions
Ask everyone to note down in their own words what the Dependency Inversion Principle is and why it is important for testability.


