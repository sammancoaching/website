---
theme: approval_testing_texttest
title: Filtering output that varies
kata: quizz
difficulty: 3
author: emilybache
---

# Filtering output that varies

You don't want your tests to fail every time the date or time changes. Before comparing against the approved output, you can filter out the parts that vary.

## Learning Goals

- recognize when you have output that varies and needs to be filtered
- use 'run_dependent_text' to filter dates and times
- evaluate when regular expressions will and won't help with handling varying output

## Session Outline

* 10 min connect: Text-Based Approval problems
* 15 min do and demo: Dates in Supermarket Receipt
* 20 min do: dates in Quizz  
* 10 min reflect: when might you need more than a regex?


### Connect: problems

Spend 2 minutes individually writing down problems you anticipate or aspects you don't understand about using a Text-Based Approval testing approach on your application. Share them with the group.

Hopefully someone will mention things like dates and process IDs in the output. (File away other problems they raise for another occasion.)

### Do and Demo Dates
Give them the [Supermarket-Receipt-Refactoring-Kata](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) on the 'with_date' branch. Show them all the failing tests and give them a few minutes to come up with strategies to fix the problem.

Demo filtering the dates by adding run_dependent_text in the config file.

### Exercise: dates in Quizz
Give them the [Approvals Puzzles](https://github.com/emilybache/Approvals-Puzzles.git) repo and point them at the 'quizz' application (puzzle 1). Ask them to write a test for it that passes consistently.

### Discussion: Regular Expressions
Today we needed to write some regular expressions to filter out unwanted dates and times. Is this a viable solution to any of the problems you came up with in the connect part of today's learning hour? Can you think of any situations where output varies but a regular expression is totally the wrong tool for the job?

Discuss in pairs or whole group if it is small.

Some ideas to inject if they can't think of any situations when regexes dont work well:
	 - Output is unsorted but otherwise consistent
	 - Output is structured as xml and you want to remove a particular tag only when it appears in a particular part of the xml tag hierarchy. 


