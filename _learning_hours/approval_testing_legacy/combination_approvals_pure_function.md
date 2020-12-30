---
theme: approval_testing_legacy
title: Combination Approvals needs a Pure Function
kata: validate_add_product
difficulty: 3
---

# Combination Approvals needs a Pure Function

This is a technique for getting a complex piece of logic under test. You use coverage measurements to find combinations of input that exercise all the paths through the code. With a combination approvals tool you can do that with a very small amount of test code.

For combination approvals to work, you first have to come up with a a way to access the complex piece of logic as a pure function - that is, you can dictate all the inputs and examine all the outputs. There is no hidden state change or global variable access. Variables that are input to the function are not modified.

Before doing this session, they should have already done an exercise with ordinary approval testing. It would also help if you had demonstrated the technique previously so they've seen it before. For example on the Gilded Rose Refactoring Kata.

## Session Outline

* 5 min connect: pure functions identification  
* 10 min demo: extract a pure function to use in the tests
* 35 min do: pair on Validate And Add Product 
* 5 min reflect: pros and cons of combination approvals

### Connect: Pure functions
What are the rules for what functions count as 'pure'? Look at the examples in [Pure-Or-Not-Quizz](https://github.com/emilybache/Pure-Or-Not-Quizz) and mark which ones are pure and which ones aren't. If you get stuck, look at the [Wikipedia article](https://en.wikipedia.org/wiki/Pure_function) describing what a pure function is. 

### Demo: Combination Approvals on a Pure Function
The starting position for [ValidateAndAddProduct-Refactoring-Kata](https://github.com/emilybache/ValidateAndAddProduct-Refactoring-Kata) has an ordinary Approval test to start you off. The coverage is not great, and you'd like to increase it. Combination Approvals would be a good approach since it's one big piece of conditional logic with few side effects.

Demonstrate extracting a pure function to use with Combination Approvals. The function should take arguments which are all the things you need to vary in order to cover all the logic branches in the production code. The return type should be a string which contains all the important outputs and can be used to verify against.

Note: the branch 'with_tests' includes an example of how to write this function.

### Do: Use Combination Approvals
Have them complete the exercise in pairs. I recommend leaving your code up on the screen while they work on repeating what you just did. Then they should go on and increase the number of combinations until the coverage is 100%.

### Reflect
Hand round large sticky notes in different colours (red and green perhaps) and ask each pair to note:

- Advantages of Combination Approvals on one colour
- Disadvantages of Combination Approvals on the other colour
- stick them on a flipchart in two columns on your way out

If they have missed any important pros or cons, add them yourself. Display the flipchart in the team area or share a scanned image of it.