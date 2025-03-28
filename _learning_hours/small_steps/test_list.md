---
theme: small_steps
title: Make a test list
kata: mars_rover
difficulty: 2
author: emilybache
tags:  small_steps
---

# Make a test list

In agile, Big Design Up Front (BDUF) is something to be avoided, but that doesn't mean we don't do any design at all. Before starting to code with TDD it really helps to spend a few minutes on Little Design Up Front. Part of that is  making a list of test cases we will work on. In this learning hour we learn why this is important but will not necessarily become skilled enough to actually do it.

## Learning Goals

* Identify the difference between a test list and a problem description
* Recognize the role of a test list in TDD
* Understand why they would benefit from learning how to create a test list from a problem description

## Session Outline
 
* 5 min connect: what to do before you start coding?
* 10 min concept: Test List
* 30 min do: Mars Rover
* 10 min reflect: Correlate test list with TDD cycles

### Connect
Go to the [choose your own adventure page]({% link exercises/warm_up_questions/tdd_overview_what_would_you_do.md %}) and review the options A,B,C,D.
Choose an option and read the suggested consequences. Read any other consequences you feel like. Turn your camera off while you’re doing the exercise, turn it back on when you’re done. (Alternatively, raise and lower a hand)

Share with the group which option you first chose.

Note - encourage people to be honest, not just give the answer they think you want.

### Concept: Test List
Before writing your first test, you should do a little analysis and identify scenarios that you'll want to make into test cases. Remind people of the test lists you used for previous katas you did in other sessions. When you have reviewed two or three test lists, ask them what the characteristics are for a good test list. You're looking for things like:

- Each case has example input and expected result
- A rule or a name to describe each case
- Not too many cases, you will add to the list when you start programming
- Since the list will be thrown away once you are done programming, don't gold-plate it

Write these characteristics up on a whiteboard. 

### Concrete: Write test lists
Ask them to work in pairs to come up with a test list. 

- Give them a requirements document to work from, like [MarsRover]({% link _kata_descriptions/mars_rover.md %}).
- After they have had time to read it, ask if there are any questions about the requirements. Take the role of business expert and answer their questions.
- Ask them to write a list of 4-6 test case ideas, give them 10-15 minutes
- Everyone should share their lists with the whole group and read through everyone else's ideas.
- Spend a few more minutes working in pairs improving the lists - steal the best ideas from the other groups.

Repeat with a second problem if there is time, for example [Fractions]({% link _kata_descriptions/fractions.md %}) or [MontyHall]({% link _kata_descriptions/monty_hall.md %}) or [BankAccount]({% link _kata_descriptions/bank_account.md %}).

### Conclusions: how can we use this?
If you didn’t choose option B in the warmup:
* Do you think writing this kind of test list before starting coding would be helpful to you personally?

If you did choose B in the warmup:
* Is this the kind of test list you would have normally written before beginning coding? Will you change anything about the way you write your test lists now?

Discuss in pairs.


