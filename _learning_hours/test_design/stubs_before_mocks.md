---
theme: test_design
title: Stubs before Mocks
kata: mars_rover
difficulty: 3
author: emilybache
affiliation: ProAgile
---

# Stubs before Mocks

## Outline


### Connect - mark the true statements
Mark the true statements and not the other ones
- A stub is a piece of code that doesn’t work yet
- A stub replaces a function that does something that is difficult to test
- A stub behaves differently depending on the situation and the arguments it’s passed
- A stub is configured by a unit test to set up a specific situation
- When you’re developing an API which another team will consume, you might give them a stub implementation of the API to work against.
- Stubs are not used in system testing, only unit testing
- Stubs are re-used in several test cases
- You normally use a mocking framework to create stubs

### Concept - Test Doubles
Go through Meszaros' definitions of Test Double, Mock, Stub, Fake. Difference between a mock and a stub - mocks can fail the test if they don't get an expected call. Prefer to use stubs, they are simpler. Demo creating a stub with their preferred mocking framework. Point out you don't need to replace a ValueObject with a stub.

### Concrete 

### Conclusions

