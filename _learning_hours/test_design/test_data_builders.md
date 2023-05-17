---
theme: test_design
title: Test data builders
difficulty: 1
author: julienvitte
---

# Refactoring test inputs with Test Data Builders

[Test data builders](http://www.natpryce.com/articles/000714.html) is a pattern you can use to easily arrange test data, 
while improving their readability and reducing coupling between tests and source code. 

## Learning Goals

- Name the 4 rules of the test data builder pattern
- Use test data builders to create test inputs

## Session outline

* 7 min connect: Map patterns with code examples
* 13 min concept: 4 rules of a Test Data Builder + demo
* 35 min concrete practice: refactor test data creation with test data builders  
* 5 min reflect: explain the main idea

## Connect

- Write notes with the name of some following patterns which can be used to create test inputs: 
  - a class constructor
  - a class constructor with default values
  - a factory method
  - object mother
  - test data builder
  - test data builder + object mother combination
- For each pattern, provide a note with an example
- Randomize names and patterns

### Map code examples with pattern names

- Ask attendees to map code examples of test inputs construction with the corresponding patterns. (3 min)
- Discuss pros and cons of each pattern usage in a unit test suite context. (4 min)

## Concepts

### Presentation: 4 rules of a Test Data Builder (3 min)
Explain the [4 rules of test data builders](http://www.natpryce.com/articles/000714.html):
1. Has an instance variable for each constructor parameter
2. Initialises its instance variables to commonly used or safe values
3. Has a *build* method that creates a new object using the values in its instance variables
4. Has *chainable* public methods for overriding the values in its instance variables (aka *with...() methods*).

### Demo (10 min)
Demo the refactoring of test inputs using a test data builder on an existing test.
- use only with...() method names in a first time
- remove usage of overriding methods when the value set is not relevant for the test case

#### Tips
- You can use the [test-data-builders-kata](https://github.com/katalogs/test-data-builders-kata), choosing the language of your choice, refactoring the Country creation.
- Use the [generate code from usage](https://xtrem-tdd.netlify.app/Flavours/generate-code-from-usage) method to focus on writing the code as you need to use it, and keep the demo short and clear.

## Concrete Practice

Ask attendees to:
- reproduce the demo on the same test data, working in pair or mob programming
- apply the same technique to all objects created in the `Arrange` part of the tests

## Conclusion
If you had to explain the main idea of test data builders usefulness to someone else, what would you say ?