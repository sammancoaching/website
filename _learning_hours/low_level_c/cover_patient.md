---
theme: low_level_c
title: Cover the patient with tests
kata: grep_with_marketing
difficulty: 5
---

# Cover the patient with tests

Part 2 of 4 learning hours on this topic. All are specific for the C language.

### Learning Goals
- define a Stub
- recognize link-time substitution
- use stubs in unit tests

## Session Outline

* 5 min connect: When do you have enough tests?  
* 10 min concept: stubs and link-time substitution  
* 35 min concrete: cover the patient  
* 5 min conclusions: confidence in these tests?

### Connect - when do you have enough tests?

How do you know you have enough unit tests? Put a mark next to any you agree with.

- When the Architect is happy
- When coverage is 80%
- When I get fed up of writing tests 
- When I feel confident the code works  
- When I’ve written the tests on my test list 
- When Jupiter is in Ares and Saturn is in Scorpio
- When I no longer have the feeling there are bugs in the code I’m looking at 
- When I can run the code and it seems to work
- When I’m confident the tests will survive a refactoring of the code

### Concept: Break dependencies using stubs

Last time we identified one problem with adding tests to existing code is to break dependencies. In the exercise repo [Grep with Marketing](https://github.com/objarni/grep-with-marketing) there is a branch 'with_stubs_no_tests'. It has the patient in the surgery, and each of the three dependencies is replaced by a stub implementation. Review the stub code.

Explain what a stub is and what problem it solves. Show how the link-time substitution works.

### Concrete: add tests
Write tests for the patient, using the stubs. Aim for 100% code coverage.

### Conclusions
In your own words, write down what a stub is and when you might use one.
