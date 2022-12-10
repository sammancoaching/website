---
theme: test_design
title: Test Names
kata: gilded_rose
difficulty: 1
author: emilybache
affiliation: ProAgile
---

# Test Names - the Osherove pattern
Roy Osherove has some advice about test name format which is widely followed.

### Learning Goals

- recognize the Osherove test naming pattern.
- use the Osherove test naming pattern.
- assess how the Osherove test naming pattern compares with however they normally name tests.

## Session Outline

* 5 min connect: What is the purpose of a test name?  
* 10 min concept: Osherove test name pattern  
* 35 min concrete: Write some tests 
* 5 min conclusions: How does this compare to what we usually do?

### Connect
What is the purpose of a test name? Give me [three facts](/activities/connect/three_facts.html) about it.

### Concept
Roy Osherove has [this advice](https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html) about test name format:

		UnitOfWork_StateUnderTest_ExpectedBehavior

That is, the test name has three parts. In many frameworks the ‘UnitOfWork’ part is the same for every test in the file, and is the name of the test suite. So focus on the other two.

_StateUnderTest_ - essentially, what kind of test data are we passing to the function? Don’t give the actual values - what is the general rule?

_ExpectedBehaviour_ - essentially, what result do we assert on in this test? Don’t give the actual value - what is the general rule?

Other test frameworks change the order of the three name parts. First they say the expected behaviour, then a qualifier for which situations it is expected in.

		ExpectedBehavior_WhenStateUnderTest

Does your organization have a naming standard like this?

### Concrete
Look at the requirements for [the Gilded Rose Refactoring Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata). First - read the requirements to understand what's going on. Make some notes on the business rules for update_quality. What are the invariants? What should happen with different kinds of items?
 
Second - write some test cases to illustrate the rules. Can you name them using Roy Osherove’s advice? For each test, think carefully how to name it. If you have time, think of a name with both Osherove's pattern, with the alternative pattern and also according to your own organization's standard. Put the alternative names in a comment so we can all review them later.

Note - this code works. It’s in production. Whatever it does is correct. If you write a test that fails that you think should pass - you should change your test. You have either misunderstood the business rules or they are documented badly :-)

### Conclusions
Review all the test names you've come up with. Which do people like best? Check back the purposes of unit tests we wrote at the beginning of the session. Do our test names fulfil these purposes? If all your tests followed this naming convention, would it help you to read and understand your tests more easily? 

