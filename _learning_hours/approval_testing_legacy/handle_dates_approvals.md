---
theme: approval_testing_legacy
title: Design for Approval Testing
kata: supermarket_receipt
---

# Design for Approval Testing

Extra challenge with dates, process ids, things in random order.

* 2 min connect: is testability an architectural concern?
* 10 min concrete: analyse the problem
* 10 min concrete: Demo pre-comparison processing
* 20 min concrete: fix the problem your own way
* 10 min concept: Pre-comparison processing
* 5 min conclusions: Strategies for testability

### Connect - is testability an architectural concern?

Is it acceptable to re-design your production code to make it more testable? What kinds of things might you want to change in your architecture? Have you changed anything in your architecture purely for the sake of testing?

Hopefully they will mention controlling the current time.

### Concrete - analyse why the tests are failing and how to fix them

Use the java, C++ or python version of [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) starting on the 'with_date' branch. All the tests are currently failing. 

* Why are the tests failing?
* Come up with two or three strategies for how to make them pass again.

Don't implement the strategy straight away. Discuss in a group the best solution.

### Demo - pre-comparison processing

Demo a solution that fixes the problem by setting the date in receipt to be a fixed, known date. 

### Concrete - fix the problem in your own way

Look again at the strategies you came up with. Pick one and implement it. Alternatively implement the same one that was demoed.

### Concept - pre-comparison processing

There are several points you can fix the output to make it suitable to use for approval.

* Just before comparison. Use a regex or similar to modify the string.
* In the printer. Have it configurable so it doesn't print every field
* Before you hand the complex object to the printer, remove or modify problematic fields.

For documentation for using Scrubbers:

* [Java](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/Scrubbers.md)
* [C++](https://approvaltestscpp.readthedocs.io/en/latest/generated_docs/explanations/Scrubbers.html)
* Python doesn't support it yet

### Conclusions

Which strategy do you prefer? Is it acceptable to change the production code to improve testability?
