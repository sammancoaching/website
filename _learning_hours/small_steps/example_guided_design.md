---
theme: small_steps
title: Example-guided design
kata: shopping_basket
difficulty: 1
author: emilybache
tags:  small_steps bdd
---

# Example-guided design

This can make a good follow up after [Design in the red step](design_with_a_test.html).

There is a video and other materials available for this learning hour as part of a [Technical Coaching Programme]({% link training/full_package.md %})

## Learning Objectives

* Recognize the difference between a specification and an example
* Turn a detailed example into a test case

## Session Outline

* 5 min connect: Spec vs Example
* 10 min concept exercise: Turn an example into a test case
* 5 min concept: Example-guided design
* 30 min concrete: shopping basket
* 5 min conclusions: How does it work and why would you?

### Connect - Spec vs Example
Write these items on notes or cards. Ask people to sort them into two sections - is it a specification or is it an example?

- If the total value of your basket is over $200, give a 10% discount.
- The maximum number of items allowed in your basket is 100.
- If your basket contains 3 printer cartridges ($50 each), 5 pens ($2 each), 5 notepads ($10 each), you should get a 10% discount.
- If your basket contains 1 printer cartridge ($50 each), 5 pens ($2 each), 3 notepads ($10 each), you should pay a total of $90.
- If your basket contains 1 printer cartridge ($50 each), 5 pens ($2 each), 5 notepads ($10 each), you should get a 5% discount.
- The total price is the sum of the unit price multiplied by the quantity for each kind of item.
- The basket report should list all the items in your basket.
- When your basket is empty the basket report should not be available.
- When your basket contains a printer cartridge and some pens then the report should show these items: printer cartridge, pens.

### Concept exercise: Convert Example to Test Case
Show the description of the [Shopping Basket Kata]({% link _kata_descriptions/shopping_basket.md %}). The description includes an example. This example can be turned into a test case. You can do that without implementing the code that will make the test pass. Split into pairs and ask people to turn that specific example into code in a test case. Ask them not to implement the code - just leave everything red and not compiling.

Give people about 10 minutes for this part, or until you can see that they've created a test case. Ask them to take a screenshot and share their test with the group via a shared online document or whiteboard.

Review all the code and comment on any differences. Hopefully you'll have got a wide variety of designs from the different pairs. Learning point - there is more than one way to design code, given the same example!

If they use a float to represent money then don't stress too much. You could just show them how to do an approximate comparison with an assertEquals that has a tolerance. You could also explain that floats are not a good way to model money and suggest they use an integer and have all the prices in cents instead of dollars.

### Concept explanation: Example-guided design
Working from a concrete example can help you to come up with a better design. Use the thing before you implement it. It helps you focus on the interface and making it easy to use, rather than how you'll write the detailed code inside.

You will probably need several examples to show all the various situations the new code might need to be used in. Start with simpler examples.

### Concrete: Shopping Basket
Practice using examples to build up functionality. Go back and write some more code on the [Shopping Basket Kata]({% link _kata_descriptions/shopping_basket.md %}). However, don't start with implementing the test you just came up with. Comment it out for the moment.

Before you split into pairs to work on the kata, spend a few minutes in the whole group coming up with a test list with simple examples to do first. Something like:

- empty basket, $0
- one item, $50
- two items, both $20
- one item $50, one item $20
- one item $160 - 5% discount
- one item $250 - 10% discount

When they are doing the kata, try to stop them from creating a ShoppingBasket class or Product class or calculatePrice function without first creating a test case. Have them practice using things in the test _before_ they exist in the production code.

### Conclusions: How does it work and why would you?
How do you use examples to guide design? Are there advantages to doing it this way? Discuss in pairs. 

