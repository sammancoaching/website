# Fixture Object pattern

Avoiding duplication is one of the four rules of simple design. This is where the DRY principle and the "Once And Only Once" rule are founded on. This principle applies to all production code. And since test code is also code, which might be a complete revelation to some, the DRY principle also applies to test code as well. Other forces that are at play for test code are the DAMP principle (Descriptive and Meaningful Phrases) and loose coupling.

In this learning hour, we'll explore how to apply the Fixture Object pattern to not only reduce duplication of code in the Arrange step of tests, but also how to reduce coupling between the test code and production code.

## Learning Objective

Use the Fixture Object pattern to reduce coupling between test code and production code, especially for tests that use test doubles.

## Session Outline

* 5 min Connect: Rank test doubles from highest to lowest coupling.
* 20 min Concept: Fixture Object pattern.
* 30 min Concrete: Refactor test code to use the Fixture Object pattern and adding a new feature.
* 5 min Conclusions: Name a benefit of the Fixture Object pattern.

## Connect: Coupling introduced by type of Test Double

Rank the test doubles from highest to lowest coupling between test and production code.

## Concept: Fixture Object pattern

A Subject Under Test can receive two types of input from a test:
* Direct inputs (function or method parameters)
* Indirect inputs (collaborators providing values when queried)

Likewise, a Subject Under Test can provide two types of output to a test:
* Direct outputs (return value from a function or method)
* Indirect ouputs (values provided to a collaborator when asked to do something)

There are five common types of test doubles:
* Dummy
* Stub
* Spy
* Mock
* Fake

The type of test double being used affects the degree of coupling between the test and production code.

The Fixture Object pattern helps us setting up the Arrange phase of a test by providing a mini Domain-Specific Language (DSL). Like the Test Data Builder pattern, this pattern further decouples the test from the implementation of the Subject Under Test.

A Fixture Object:
* provides helper methods that enabled a test to configure values that can be queries by the Subject Under Test.
* creates an instance of the Subject Under Test when requested.
* captures indirect outputs passed to  the dependencies of the Subject Under Test and makes them available to the test.

## Concrete

The exercise is the [Expense Sheet Approval](https://git.sr.ht/~janvanryswyck/expense-sheet-approval) kata. This exercise is composed of two parts:
1. Ask the participants to refactor the tests to use a Test Fixture object for setting up the `ApproveExpenseSheetHandler`. The tests need to provide the indirect inputs (`ExpenseSheet` and `Approver`) and capture the output (the `ExpenseSheet` saved back in the repository).
2. When all the tests use the Fixture Object, implement a new feature. The employee who submitted the expense sheet should receive notifications when the expense sheet has been approved. This requires a new dependency (`EmployeeNotifier`) to be introduced for the `ApproveExpenseSheetHandler`.

## Conclusions

Note down, in your own words, the biggest benefit of using the Fixture Object pattern.

