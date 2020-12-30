---
layout: learning_hour
title: Approval Testing Intro
parent: Approval Testing Legacy Code
grand_parent: Learning Hours
nav_order: 1
---

# Approval Testing Intro

One reason to use approval testing is to avoid writing a lot of repetitive assertion code. When you have legacy code often the units you can isolate are larger than the units you get with ordinary TDD. This means the unit tests could have a lot of assertions in them, to check every aspect of the unit under test. Instead of writing a lot of assertions, approval testing gives you another approach. You print the state of the object you want to check, and pass it to a verify function. In today's exercise, SupermarketReceipt, a Printer already exists as part of the production code so you don't need to write your own.

This is an introduction to Approval testing and the aim is people will come away understanding the basic mechanism. They should understand that the test fails the first time because there is nothing approved to compare against. They should understand that one 'verify' can replace many assertions.

## Session Outline

* 10 min connect: test code review
* 5 min demo: Convert several Asserts to one Verify
* 30 min do: pair on Supermarket Receipt Refactoring Kata  
* 10 min reflect: differences with Approval testing

### Connect

In the starting position for this exercise, [Supermarket-Receipt-Refactoring-Kata](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata), (on the main/default branch), there is a test that contains quite a few assert statements to check the contents of the Receipt object. Everyone should review this test case. Discuss in pairs for 5 minutes and note down anything you like about the test and anything you don't like about it. Use two different colours of sticky note. Share your notes with the group and put your common list of 'like' and 'dont like' on a flipchart.

For a remote meeting: use a shared google doc to make your group lists.


### Demo Supermarket Receipt first approval test
In this demo, explain that this is legacy code and you'd like to write some tests for it so you can refactor it. Briefly show the nasty code in the 'handleOffers' method. The aim is to test all the different kinds of discount so we can be confident to refactor this code later on.

Take the existing test and add a call to 'verify' from an approval testing library. Use the ReceiptPrinter class to print the receipt to a string that you can use as the argument.

Show that all the information that is checked in individual assert statements are present in the printed receipt. This means that the approval test will catch any errors the assertions would have caught. Delete the assertions. 

Note that you can re-use the same printer in many tests, so overall it is not going to be more code. Note that test failures are relatively easy to understand when you use a diff tool.

### Do Supermarket Receipt
Have people work in pairs to repeat what you demonstrated, then add further tests for different discounts. Point out the enumeration class 'SpecialOfferType' that contains all the different varieties of discount.

### Reflect - Differences with Approval testing
Look at your new tests and compare them with the list of things you liked and didn't like at the start of the session. Which are still valid for your new tests? Make a new list of things you like and don't like by writing new stickies on a new list.

