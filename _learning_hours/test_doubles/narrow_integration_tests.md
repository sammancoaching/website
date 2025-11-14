---
theme: test_doubles
title: Narrow Integration Tests for Outbound Ports
kata: enterprise_phonebook
difficulty: 5
author: emilybache
tags: test_doubles test_design architecture
---

# Narrow Integration Tests for Outbound Ports
This learning hour assumes people are familiar with Hexagonal architecture already, as well as Spy Test Doubles. We use both those concepts as a basis for explaining Narrow Integration Tests. It will also help if they understand web servers and test fixtures.

## Learning Objectives

* Describe 'Narrow Integration Test'.
* Use a test double to create a Narrow Integration Test for an outbound port in a hexagonal architecture.

## Session Outline
* 5 min connect: Hexagonal architecture
* 15 min concept: Code review & classify
* 5 min demo: Narrow Integration Test
* 25 min do: Write a Narrow Integration Test
* 5 min reflect: Most important takeaway

### Connect - Hexagonal architecture
Draw a hexagon with a space around it for the ports and adapters layer. Give people labels and arrows for the following and ask them to place them on this diagram:

* Ports and Adapters Layer
* Domain Layer
* Outside World
* Dependency Direction Arrow 

This last one should be an actual arrow with the label 'depends on'. You could give them more than one of it.

You are hoping they will correctly label the layers and also know that the dependency arrows all point towards the domain layer in the center. These are the bare bones of a Hexagonal architecture. If they don't already know this then the rest of this session won't work very well.

### Concept - Code review & classify
Ask them to review the classes in the production code of the [Enterprise Phonebook Test Design Kata](https://github.com/emilybache/EnterprisePhonebook-TestDesign-Kata.git). Give them a pile of sticky notes with the name of these classes on and ask them to classify them two ways.

Firstly - Which layer does each class belong to assuming a Hexagonal architecture?
Secondly - Classify each class in one category:

* No unit test needed
* Can unit test it without mocks
* Will need to mock something to test it - specify which class(es) to mock

You are hoping they will be able to spot the port interfaces and value objects which don't need tests, the pure domain object (Phonebook) which can be tested without mocks, and the rest which will. 

They should spot the EnterprisePhonebook is in the Domain layer but unit tests will need mocks for the two ports it uses. The two adapters for those ports will also need mocks to test. This is your lead in for the next section to discuss that you don't really want to write pure unit tests for these classes.

### Demo: Narrow Integration Test
Unit tests generally replace the parts that do I/O with test doubles, because I/O would slow them down and make them less reliable. However there can be bugs in those parts of the code that do I/O, which your unit tests then won't find.

Integration tests are supposed to find these kinds of issues by including more of your system and mocking fewer parts. This makes them slower and less reliable, but capable of finding integration bugs. To minimize the cost and maximize the bug-finding potential, we prefer 'Narrow' integration tests.

Martin Fowler has a good article about this - [Integration Test](https://martinfowler.com/bliki/IntegrationTest.html), as does James Shore - [Narrow Integration Tests](https://www.jamesshore.com/v2/projects/nullables/testing-without-mocks#narrow-integration-tests).

Briefly explain the concept, just enough that they will understand your demo. Write narrow integration tests for the Authorizer adapter class. Be sure to show these tests can find the bug in this class.

This test will use the lightweight http server included with the test code, and configure the TestDoubleHandler. They will need to understand web servers, test fixtures and test doubles already for this code to make sense. If they can't grasp this code quickly, they will probably not be able to do the concrete practice without assistance.

### Concrete
Ask them to write a narrow integration test for the Alert adapter and expose the bugs in this code.

### Conclusions
What is the most important thing you learnt today about integration testing?
