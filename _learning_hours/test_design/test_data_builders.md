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

* 3 to 7 min [connect activity](#connect)
* 13 min concept: 4 rules of a Test Data Builder + demo
* 35 to 39 min concrete practice: refactor test data creation with test data builders  
* 5 min reflect: does our code have this issue?

## Connect
Pick one of the following connect activities, depending on the trainee's knowledge:
- 3 facts and a question about arranging inputs test
- 3 facts about the builder pattern
- map code examples with pattern names

### Map code examples with pattern names

#### Preparation

- Write notes with the name of some following patterns which can be used to create test inputs: 
  - a class constructor
  - a class constructor with default values
  - a factory method
  - object mother
- For each pattern, provide a note with an example
- Randomize names and patterns

#### Activity
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
- remove usage of overriding method when the value set is not relevant for the test case 
  (you can change the argument value with no side effect on the test execution)

#### Tips
- You can use the [test-data-builders-kata](https://github.com/katalogs/BookInvoicing-TestDesign-Kata), choosing the language of your choice, refactoring the Country object construction in tests.
- You may use the [generate code from usage](https://xtrem-tdd.netlify.app/Flavours/generate-code-from-usage) method to focus on writing the code as you need to use it, and keep the demo short and clear.

## Concrete Practice

Ask attendees to:
- reproduce the demo on the same test data, working in pair or mob programming
- apply the same technique to all objects created in the `Arrange` part of the tests

## Conclusion

Does our code have this issue?

Ask the team to find part of their tests where they could have applied the test data builder pattern
