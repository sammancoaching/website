---
theme: test_design
title: Test Desiderata
difficulty: 1
author: ronheywood
affiliation: Spektrix
tags: test_design
---

# Test Desiderata
Kent Beck described the concept that tests had a number of properties, and arranged them in a list.
Not all tests exhibit all properties, but Kent stated "No property should be given up without receiving a property of greater value in return."

## Learning Objectives
* Recognise the properies of different types of tests
* Optimize the value of your tests by choosing how to tradeoff among various valuable properties.

## Session Outline

* 5 min connect: What are some of the different types of tests?
* 20 min concept: What are the properties of tests, as mentioned in the Desiderata
* 30 min concrete: Split into groups assign the properties to the types of test
* 5 min conclusions: Think of the last test you wrote, or a test that you remember. What properties does it have? Which does it lack? Is that the tradeoff you want to make?

## Connect 

### On a post it note write the names of some types of tests that you know.

We would expect that many members of a team can come up with Unit Test and Integration Test. 

Would anyone think of Contract Test, Exploratory Test, Smoke Test, Beta Test?

* Can the team agree that there are lots of different types of test?
* Can the team agree that there are pros and cons to each type of test?

## Concept
Introduce the Test Desiderata

Desiderata – (Latin: "desired things").

![The Test Desiderata]({% link /assets/images/test-desiderata/Desiderata-map.png %})

[Image by Kent Beck](https://kentbeck.github.io/TestDesiderata/)

### Properties of the Desiderata
Kent Beck describes each of these properties:
* Isolated — tests should return the same results regardless of the order in which they are run.
* Composable — I should be able to test different dimensions of variability separately and combine the results.
* Deterministic — if nothing changes, the test result shouldn’t change.
* Fast — tests should run quickly.
* Writable — tests should be cheap to write relative to the cost of the code being tested.
* Readable — tests should be comprehensible for reader, invoking the motivation for writing this particular test.
* Behavioral — tests should be sensitive to changes in the behavior of the code under test. If the behavior changes, the test result should change.
* Structure-insensitive — tests should not change their result if the structure of the code changes.
* Automated — tests should run without human intervention.
* Specific — if a test fails, the cause of the failure should be obvious.
* Predictive — if the tests all pass, then the code under test should be suitable for production.
* Inspiring — passing the tests should inspire confidence

Show how a Unit Test meets many of the properties, although acknowledge that it lacks Predictive capabilities.

### A visual example of Unit Test lacking inspiration and prediction properties
A number of memes exist to demonstrate this:

![Unit Tests With No Integration Tests]({% link /assets/images/test-desiderata/unit-tests-no-integration-tests.png %})

Examine how the manual exploratory testing approach sacrifices almost all of the desired qualities, 
in return for greater confidence. (You may ask is that promise guaranteed?)

### Quote
A Quote from the article by Kent Beck is worthy of attention:

> Some properties support each other. Automating tests makes them faster to run.
> Some properties interfere with each other. Making tests more predictive of production behavior makes them slower.
> Sometimes (and this is the magic), properties only seem to interfere. You can use composability to make tests faster and more predictive.

## Concrete Practice
Take some of the types of tests from the post it notes and allocate one or two to pairs in the group.

Ask them to review each of the properties on the Desderata image and decide which of the properties apply to these types of tests.

## Conclusion
In [a 2019 article published on Medium.com](https://medium.com/@kentbeck_7670/test-desiderata-94150638a4b3) Kent Beck offers a great question to use as the conclusion to the Learning Hour:
> Look at the last test you wrote. Which properties does it have? Which does it lack? Is that the tradeoff you want to make?
