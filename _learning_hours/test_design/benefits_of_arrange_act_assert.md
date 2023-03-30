---
theme: test_design
title: Benefits of Arrange - Act - Assert
kata: encode_refactoring
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Benefits of Arrange - Act - Assert

This session is an intro to the topic for people who havn't written many test cases before and where the other [Arrange Act Assert](arrange_act_assert.html) learning hour is too big of a step from where they are.

## Learning Goals

* Recognize a test written with the Arrange - Act - Assert pattern
* Explain why the AAA pattern improves test maintainability
* Use the AAA pattern in an existing test case

## Session Outline

* 15 min connect: test design tips
* 5 min concept: Arrange - Act - Assert
* 30 min do: Encoding Refactoring Kata
* 5 min reflect: code review

### Connect - Test Design Tips
In your organization do you have test design guidelines? How would you advise someone new to your organization to design their unit tests? Discuss in pairs for a few minutes and share your best tips with the group. Gather notes and urls in a shared document.

The point of this part is to get them thinking about the issue, what they already know, and where to find out information. If the information they come with is questionable or bad in your opinion, that can help you to plan future sessions. A 'connect' activity is not the best time to have a big discussion or tell people they are wrong.

Note - this is a [Web Hunt](/activities/connect/webhunt.html).

### Concept - Arrange - Act - Assert
Explain the AAA structure, why it increases readability, and why that's important. If anything they found in the 'connect' activity references it, draw attention to that.

### Exercise
Show the test code for the [Encode Refactoring Kata](https://github.com/emilybache/Encode-Refactoring-Kata). Note that it does not follow the Arrange-Act-Assert structure. Introduce a bug in XyzTimer (change temp |= 0x1F to temp |= 0x1E for example) and show the test failure. The failure is ok, but doesn't pinpoint very well what's wrong. Revert the code so the test is passing again.

Ask them to refactor the code to use the AAA structure. When their refactoring is complete, they should be able to re-introduce the bug and see only one of three tests failing.

### Conclusions
In your own words, explain why using the Arrange - Act - Assert pattern improves test maintainability. Write a sentence or two on a note and share it with the group.
