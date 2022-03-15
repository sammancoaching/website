---
theme: test_design
title: Test Doubles
kata: tire_pressure
difficulty: 3
author: emilybache
affiliation: ProAgile
---

# Test Doubles
Introduce the various kinds and how to create them in the relevant test framework.

### Connect
[Mark the true statements](/activities/connect/pick_the_correct_items_on_the_list.html) and not the other ones:
- A stub is a piece of code that doesn’t work yet
- A test double replaces a dependency of the class or function under test
- A stub behaves differently depending on the situation and the arguments it’s passed
- A mock is configured by a unit test to set up a specific situation for the class under test
- When you’re developing an API which another team will consume, you might give them a stub implementation of the API to work against.
- Mocks are not used in system testing, only unit testing
- Stubs are re-used in several test cases
- You can use a mocking framework to create both mocks and stubs

### Concept - Test Doubles
Go through Meszaros' definitions of Test Double, Mock, Stub, Fake. Difference between a mock and a stub - mocks can fail the test if they don't get an expected call. Prefer to use stubs, they are simpler. Demonstrate how to create a stub and a mock in the test framework the participants are using.

### Concrete
Tire Pressure from the [Racing Car Katas](https://github.com/emilybache/Racing-Car-Katas). Write the unit tests for the Alarm class. Use a test double in place of the Sensor.

If that goes quickly, follow it up with the TelemetrySystem exercise: write the unit tests for the TelemetryDiagnosticControls class. Use a test double in place of the TelemetryClient.

### Conclusions
[When should you use](/activities/conclusions/when_to_use_this.html) a Test Double? In particular, when should you use a Stub? Make some notes and share with the group.
