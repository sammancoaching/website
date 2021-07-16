---
theme: small_steps
title: Selecting and ordering test cases
kata: fizzbuzz
difficulty: 1
---

Selecting and ordering test cases 
----------------------------------

[FizzBuzz](/kata_descriptions/fizzbuzz.html) is one step up in difficulty from Leap Years. The problem description asks you to design a console application. You need to do a small amount of analysis to realize the heart of it is a pure function similar to the one for Leap Years. This one takes an integer and returns a String. You can use this Kata to talk about how to plan and select test cases, and why you spend a few minutes analyzing the problem to look for a pure function to test drive. Note - this is part of the general strategy for ['inside-out' TDD](https://8thlight.com/blog/georgina-mcfadyen/2016/06/27/inside-out-tdd-vs-outside-in.html). 

### Learning goals
The theme is the same as the first session: "Small steps". 

* Explain why we look for a pure function to test-drive in TDD
* Use a 'test case list' during TDD
* Use TDD to build a pure function and associated tests

## Session Outline

* 5 min connect: pairs discuss what is easiest to test  
* 10 min explain & elaborate test cases for FizzBuzz 
* 5 min demo FizzBuzz  
* 25 min FizzBuzz in pairs  
* 5 min reflect: pairs discuss what they learnt today

### Connect
Introduce yourself to a person near you and discuss. (Use the internet to research if you are unsure what those things are.)

Which is easiest to write automated tests for:

- a whole system with a database
- a pure function
- a user interface
- a void function
- a method in a Controller class (as in Model-View-Controller)

The reason for asking about what is easy to test is to get them prepared for designing a pure function or static method for calculating FizzBuzz. These kinds of functions are easier to test since all the outcomes are visible in the return value, the input value is not modified and there are no side effects.

### Explain and elaborate test cases
Starting at a whiteboard, explain the purpose of the [FizzBuzz](/kata_descriptions/fizzbuzz.html) kata. Read the description to the group, or put it on a screen they can see. Ask the group to suggest test cases we will need for this kata. Write up whatever they say. 

What they come up with might include this - an impure function that prints a multi-line string: 

	() -> print("1\n2\nFizz\n4\nBuzz\n...")


Explain that they could usefully write a pure function that takes an integer and returns a string. This function could be called by the other one, and will be easier to test, while still giving us good coverage of the business rules. 

You might then end up with test cases on the whiteboard looking something like this:

	1 -> "1"
	3 -> "Fizz"
	5 -> "Buzz"
	6 -> "Fizz"
	15 -> "FizzBuzz"


When you have half a dozen or so of those kinds of cases, ask them to prioritize/sort them. Which is the easiest to implement? Which order should we take them in? Hopefully they will notice you should take a number that is not divisible by 3 or 5 to begin with. Write numbers next to the examples (in a different colour pen) which order to implement them as test cases.

### Demonstrate TDD
If you think they need this, demonstrate how to TDD the first few test cases. If they handled LeapYears well in a previous session, you could skip this. If I do a demo, I often use cyber-dojo to make the TDD cycles more visible.

### Do
Have the group work in pairs or a mob to do the Kata, starting from no code, just the examples written on the whiteboard. Every 4 minutes, remind them to swap the driver.

When it comes to the test for the impure function that prints to the console, I suggest you point out this is harder to test with a unit test and we will leave automating that test for another day. For today it's enough to automate the test for the pure function, and do a manual test of printing to the console.

### Reflect
How did TDD feel? What was difficult and what was easier compared with tests you've written before? Tell us the most useful thing you learnt so far.

