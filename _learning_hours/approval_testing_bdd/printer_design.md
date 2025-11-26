---
theme: approval_testing_bdd
title: Printer Design
kata: vending_machine
difficulty: 2
author: emilybache
affiliation: ProAgile
tags: approvals bdd
---

# Printer Design

Redesigning asserts as a printer.

* 2 min connect: What do you look for in an error message
* 5 min concept: What is a Storyboard in Approval testing
* 40 min concrete: Design a printer
* 5 min conclusions: Note down what you learnt

### Connect - What do you look for in an error message?

When a test case fails, what kinds of things help you to work out what's happened? Note down some ideas.

### Concept - What is a printer, what is a storyboard

Explain what a printer is in the context of approval testing. Perhaps show the ones for [Supermarket Receipt](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) or [TicTacToe](https://github.com/emilybache/TicTacToe-Kata). 

Explain the idea of a storyboard - where a test prints the state after 'arrange', then print out what the 'act' step is, as well as printing the final state. Some tests will have multiple 'act' steps and print the state after each one.

### Concrete - Design a printer

There is a [starting position](https://github.com/emilybache/VendingMachine-Approval-Kata) for the [Vending Machine Kata]({% link _kata_descriptions/vending_machine.md %}) with one test case. First convert the assertions to an approval test. (Do this as a demo, then ask them to do the same for themselves). Then introduce new functionality into the vending machine feature by feature. Either do this for yourself or merge in the feature branches provided. As you develop the code, extend your printer to test the new functionality.

### Conclusions - printer design

What have you learnt about printer design? How much detail should you include?
