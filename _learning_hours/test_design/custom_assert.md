---
theme: test_design
title: Custom Assertions
kata: todo
difficulty: 3
---

# Custom Assertions

Writing your own assertions is a way to reduce duplication in tests. The error message also needs to be informative. Approval testing is a different way to achieve that but we don't go into that here.

## Session outline

* 5 min connect: Failure messages
* 10 min concept: Custom Assertion
* 30 min do: Roadload or similar
* 10 min reflect: when should you write a custom assertion?

### Failure messages
Look at these [failure messages](/exercises/games/failure_messages.html). What do you expect to see in a good failure message?

### Custom Assertion
If you've used a custom assertion in a previous exercise, review that code now. Otherwise, show an example of a custom assertion for an exercise they are already familiar with.

### Extract a custom assertion
Roadload has a starting position with one test case with several assertions. Extract it to a custom assert in a test fixture. Write some more tests using the same custom assert.

### Conclusions
When should you write a custom assertion? What kinds of code smells would indicate it is a good idea?

Compare your answers with the list in [XUnit patterns](http://xunitpatterns.com/Custom%20Assertion.html)
