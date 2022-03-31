---
theme: test_doubles
title: Test Doubles Intro
kata: tire_pressure
difficulty: 1
author: emilybache
affiliation: Praqma
---

# Test Doubles Intro
I think it's important to learn the basic concepts and how to create test doubles by hand before launching into the details of a specific mocking framework.

### Concept - Test Doubles
Go through [Meszaros' definitions](http://xunitpatterns.com/Mocks,%20Fakes,%20Stubs%20and%20Dummies.html) of Test Double, Mock, Stub, Fake. Focus on the Stub to begin with - this is the simplest kind of test double. 

Explain that a stub is useful when the real object would

* make your test slow
* be difficult to construct
* make your test unreliable
* be difficult to get into a particular (error) state

Note that we don't want the object being tested to know that it got a test double instead of a real collaborator, so we need an abstraction or interface that both objects implement. We also need some kind of Dependency Injection so we can substitute the collaborator.

### Concrete
[Tire Pressure](https://github.com/emilybache/TirePressure-Kata). First ask them to review the code and work out which collaborator we want to replace with a test double. When everyone has spent 5-10 minutes reading the code, go through how you should introduce the abstraction/interface for Sensor and how to inject this dependency. Then ask them to write the unit tests for the Alarm class including the 'check' method.

If they finish this task quickly, ask them to work on [Turn Ticket](https://github.com/emilybache/TurnTicket-Kata).

### Conclusions
In what situations should you use a stub? Note down some answers and share them with the group.