---
theme: test_design
title: Test a Bug
difficulty: 2
author: gregorriegler
tags: test_design
---

# Test a Bug

When a bug appears in our code, the common approach is to quickly identify and fix the problem in the production code. 
Although this may resolve the issue, it poses a certain degree of risk. 
Merely modifying the production code does not guarantee that we have fully comprehended the problem, nor does it assure that the issue will not reoccur. 
To mitigate these risks, it is crucial to validate and verify the changes made to the production code. 
One effective solution is to create a test-harness and reproduce the bug using a test. 
This approach enables us to confirm that the issue has been resolved correctly and helps us prevent the problem from occurring in the future.

## Session Outline
 
* 10 min connect: Discuss what the usual steps are to fix a code bug
* 5 min concept: Test a bug
* 35 min do: Write a test to reproduce a bug
* 10 min reflect: activity & code review

### Connect: Discuss what the typical steps are to fix a bug in the code
Have the participants discuss in small groups how they fix bugs.
This often involves analysis, using the debugger and manual testing.

### Concept: Test a bug
Explain the steps how to verifiably fix a bug in the way it stays fixed.

1. First we need to prove the bugs existence (often manually, by executing the program and observing its behavior).
2. Automate the proving of the bugs existence (the step we want to practice in this learning hour).
    Explain the value of writing a test for the bug.
3. Make the change that fixes the bug

### Do: Bug Hunter Kata
Practice the designing of test cases that reproduce a simple bug.
For this we use the [Bug-Hunter-Kata](https://github.com/gregorriegler/Bug-Hunter-Kata).

### Reflect: What did we do
Ask the participants what they did and collectively review their code.

For the test code, ask the following questions:

- Does it sufficiently reproduce the bug?
- Does the test fail when the bug exists?
- Does the test pass when the bug is fixed?
- Does the test fail for any other reason other than the bug (i.e. is it testing too much, and how could we fix that)?
