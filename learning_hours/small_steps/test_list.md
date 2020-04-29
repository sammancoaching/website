---
layout: default
title: Make a test list
parent: Working in Small Steps
grand_parent: Learning Hours
nav_order: 5
---

# Make a test list

In agile, Big Design Up Front (BDUF) is something to be avoided, but that doesn't mean we don't do any design at all. Before starting to code with TDD it really helps to spend a few minutes on Little Design Up Front. Part of that is  making a list of test cases we will work on.

## Session Outline
 
* 5 min connect: what to do before you start coding?
* 10 min concept: Test List
* 30 min do: shopping basket or similar
* 10 min reflect: Correlate test list with TDD cycles

### Connect
In pairs, discuss these question and make notes:

- When starting a new feature or exercise using Test-Driven Development what are the first things to think about? 
- Make a note of anything you should do before you start coding.

Ask a few pairs to share what they have noted down and make a list of things for everyone to do. Make sure to add 'test list' if no-one mentions it.

### Concept: Test List
Before writing your first test, you should do a little analysis and identify scenarios that you'll want to make into test cases. Remind people of the test lists you made for previous katas you did in other sessions. Ask them to work in pairs to come up with a test list for today's problem. 

After 5 minutes or so, have pairs report the scenarios they came up with. Write them on a whiteboard and synthesize all the suggestions into a single list.

Shopping Basket is a good problem for this. There are perhaps half a dozen scenarios to think about and make into a list. FizzBuzz would also work, or WordWrap.

### Do: TDD from a test list
Work from the common test list that we created as a group on the whiteboard. Each pair can decide what order to tackle them in.

### Reflect: connect TDD cycles to test list
Review the code and TDD cycles. A tool like cyber-dojo makes test cycles visible, but you can also use the local history in your IDE, or git history. 

- Did you have one TDD cycle per test on your list?
- Were the cycles even in length, did you get a good TDD rhythm going?
- Did you add additional tests to your list during development?
- Did you remove tests from your list that you decided not to implement?
- What kind of test list supports TDD best?
