# The Saff Squeeze

From time to time, we encounter bugs in the software systems that we work on. That's part of the life as a software developer. Often, we don't know the root cause of the defect. So, in order to uncover what is going on we typically start a debugging session.

However, when we take a step back and think about defects from a higher level, we can conclude that every bug in the system actually corresponds to a missing test in the code base.

In this learning hour, we'll explore the Saff Squeeze technique. The goal of this technique is to find that missing test.

## Learning Objective

Using the Saff Squeeze technique to find bugs, by starting with a high-level end-to-end test and working towards a small, unambiguous test that clearly demonstrates the defect.

## Session Outline

* 5 min Connect: Name three debugging techniques.
* 20 min Concept: Introduce the Saff Squeeze technique.
* 30 min Concrete: Apply the Saff Squeeze technique to find the bug in the Shopping Cart Calculator.
* 5 min Conclusions: Share a benefit of the Saff Squeeze technique.

## Connect: Name three debugging techniques

* You've discovered a defect in the production environment, but you don’t know what’s causing it. What now? Name three techniques that you could use to find the root cause of the bug.

## Concept: The Saff Squeeze technique

The Saff Squeeze in one sentence:
> "Inline parts of a failing test until the reason for the failure becomes obvious.”

Explain how the technique works by following these steps:
1. Start with a failing high-level test that reproduces the defect.
2. Inline the method(s) called on the system under test. (Breaking encapsulation is acceptable at this stage)
3. Add assertions at the beginning of the test, gradually moving towards the failure while verifying all assumptions.
4. Tidy up the test code and remove all irrelevant parts.
5. Repeat until the test is minimal and the defect becomes obvious.

Some advantages of using this technique:
* Leaves behind clear, reusable unit tests.
* Turn defects into focused insights.
* Encourages debugging through testing rather than relying on breakpoints or stepping through code.
* Allows a steady pace from failure to fix.

References:
* [J.B. Rainsberger - The Saff Squeeze](https://blog.thecodewhisperer.com/permalink/the-saff-squeeze)
* [Kent Beck - The Saff Squeeze](https://tidyfirst.substack.com/p/the-saff-squeeze)

## Concrete

The exercise is the [Shopping Cart Calculator](https://git.sr.ht/~janvanryswyck/shopping-cart-calculator) kata. The final test verifies the calculation of the total amount of the shopping cart with a large bulk discount. This test, which already fails, serves as the starting point for the exercise.

## Conclusions

Ask participants to write down their takeaways. You can ask the following questions:

* What is the most important thing you learned about the Saff Squeeze?
* What facts or ideas are most important to remember?
* What would you tell a colleague about this training? What would be important to mention?
