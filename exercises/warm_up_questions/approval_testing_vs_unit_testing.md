---
layout: default
title: Differences between unit tests and other tests
parent: Warm-up Questions
grand_parent: Exercises
nav_order: 5
---

# Differences between unit tests and other tests

Which of these practices are recommended for:

* only unit tests
* all kinds of automated tests (unit, system, component)
* tests that aren't unit tests (system, component)
* never

## Practices:

1. Only _one_ assertion in each test case
2. An expert should check the test result is correct every time you execute it
3. You should have 100% line coverage when you run the tests
4. Test against a public api not a private api
5. Avoid overspecifying. Check only certain properties and details, not the whole output.
6. Write the tests only after the code to be tested is implemented and design is stable.
7. Use a white-box testing approach, you will find more bugs.
8. Use a black-box testing approach, your test will be less fragile.
9. Use Exploratory testing.
10. Use Capture-replay testing.
11. Use Pairwise (all-pairs) testing.
12. Use Data-driven testing.

