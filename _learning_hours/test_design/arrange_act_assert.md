---
theme: test_design
title: Arrange - Act - Assert
kata: mars_rover
difficulty: 2
author: emilybache
---

# Arrange - Act - Assert

Famous quote from Brian Kernighan: "Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.". It's an exhortation to keep your code as simple as possible so you have a chance of being able to debug it.

Similarly you could say about test code - All code you write may contain bugs, and unit tests help you to find those bugs. If you write the test code as clever and complex as the production code, your test code will need tests too!

No-one wants buggy test code that could hide bugs in the production code. So what to do? We write our test code to be as simple and straightforward as possible. Nowhere for bugs to hide. Using a standard Arrange - Act - Assert structure helps.

## Session Outline
 
* 15 min connect: review test code samples   
* 5 min concept: Arrange - Act - Assert
* 30 min do: Mars Rover, Shopping Basket or Tennis
* 5 min reflect: code review

### Connect: Review sample code
Pin up some code samples around the room. For example [Mars Rover Kata Sample Tests](https://github.com/emilybache/MarsRover-Sample-Tests) or [ShoppingBasket Test Design Kata](https://github.com/emilybache/ShoppingBasket-Test-Design-Kata). Some follow Arrange-Act-Assert structure, some don't. Have them review the code and vote with their feet which is most and least likely to contain bugs.

### Concept: Arrange - Act - Assert
Bring up the code sample with the best AAA structure and go through it. Explain how it makes the test code easier to read and less likely to have bugs in. Explain why that's important.

### Do: Mars Rover, Shopping Basket or Tennis
Practice writing new test cases with an Arrange-Act-Assert structure.

Choose a kata where there is some setup and it's hard to write the whole test on one line. For example Mars Rover needs some kind of Rover class which you 'Arrange' into an initial state, before you 'Act' and call a method on it, then 'Assert' the state of the rover is correct.

If you've previously done a ['test list']({% link _learning_hours/small_steps/test_list.md %}) learning hour on this kata you could remind them of it and distribute the list you made that time.

### Reflect: Code Review
Review your test code and compare it with your production code. Are you clever enough to debug your production code? What about your test code? Look at aspects such as:

- Readability
- Cyclomatic Complexity
- Consistent Abstraction Levels

Hopefully the test code is readable, low complexity, and uses a consistent abstraction level throughout each test case. Your production code should also be readable and have consistent levels of abstraction within a method. It may have higher cyclomatic complexity though. Are there any other differences?
