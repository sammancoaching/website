---
layout: default
title: Selecting and ordering test cases with FizzBuzz
parent: Working in Small Steps
grand_parent: Learning Hours
nav_order: 2
---

Selecting and ordering test cases with FizzBuzz
-----------------------------------------------

FizzBuzz is one step up in difficulty from Leap Years. Again, you are designing a function, this time one that takes an integer and returns a String. You can use this Kata to talk about how to plan and select test cases, and the purpose of adding additional cases in order to do triangulation. 

The first time you do this kata, I suggest focussing on the core business logic for converting one number at a time, and leave out the part where you print the full 100 lines to the console. That part is a little harder to test-drive.

## Session Outline

* 2 min connect: pairs discuss what is easiest to test  
* 10 min explain & elaborate test cases for fizzbuzz 
* 10 min demo fizzbuzz with triangulation 
* 2 min reflect: summarize triangulation in own words  
* 30 min fizzbuzz in pairs  
* 5 min reflect: pairs discuss what they learnt today

### Connect
Introduce yourself to a person near you and discuss. (Use the internet to research if you are unsure what those things are.)

Is it easier to unit test:

	- a static method
	- pure function
	- method that modifies object state
	- method that modifies its parameters

Note: you can modify this list to fit the programming language they know.

The reason for asking about what is easy to test is to get them prepared for designing a pure function or  static method for calculating FizzBuzz. These kinds of functions are easier to test since all the outcomes are visible in the return value, the input value is not modified and there are no side effects.

### Demonstrate
Starting at a whiteboard, explain the purpose of the kata. Read the description to the group, or put it on a screen they can see. Ask the group to suggest test cases we will need for this kata. Write up whatever they say. 

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

Demonstrate how to TDD the first few test cases. Add extra cases for triangulation purposes - eg if they only wrote up '1 - > "1"' you may end up doing '2 -> "2"' as well. Explain the extra examples are useful to force you to generalize the code. Add the new test cases to the whiteboard.

When it comes to the test for the impure function that prints to the console, I suggest you point out this is harder to test with a unit test and we will leave automating that test for another day. For today it's enough to check the pure function.

I often use cyber-dojo for the demo, to make the TDD cycles more visible.

### Reflect
What is triangulation? Describe it in your own words in your notebook, or make a sketch.

### Do
Have the group work in pairs or a mob to do the Kata again, starting from no code, just the examples written on the whiteboard. Every 4 minutes, remind them to swap the driver. They should do it the same way you demonstrated, test by test in small steps. If some people are really on the ball and complete the FizzBuzz exercise before the time runs out, give them some additional rules (write them on the whiteboard). 

- Multiples of 7 are "Whizz"
- Multiples of 11 are "Bang"

If they ask you for more details, explain:

- Multiples of 3 & 7 are "FizzWhizz"
- Multiples of 5 & 11 are "BuzzBang"
- Multiples of 3 & 11 are "FizzBang"
- ... etc ...
- Multiples of all of 3,5,7,11 are "FizzBuzzWhizzBang"

Ask them to refactor first to make adding the new rules straightforward.

### Reflect
- In pairs, discuss how TDD felt, what was difficult and what was easier.
- Tell the other person the most useful thing you learnt so far.

