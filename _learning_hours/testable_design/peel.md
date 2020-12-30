---
layout: learning_hour
title: Strategy - Peel
parent: Testable Design
grand_parent: Learning Hours
nav_order: 4
---

# Peel - a strategy for difficult to test code

This strategy is useful when you have code that is easy to test sandwiched in the middle of hard-to-test code.

## Session Outline
 
* 5 min connect: recap Extract Function
* 10 min concept: Peel   
* 40 min do Peel on a couple of functions 
* 5 min reflect: When to Peel
 

### Connect - recap Extract Function
These are some steps you can follow in a ‘extract function’ refactoring. What order should you do the steps in? Re-order them in your own copy of the list.

1. Compile and run tests
1. Declare a new function with a suitable name
1. Define the return type of the new function
1. Identify the section of code you want to extract and copy it
1. Replace the section of code with a call to the new function
1. Define the arguments of the new function
1. Compile
1. Paste the section of code as the body of the new function
1. Compile and run tests


### Concept: Peel
This picture visualizes the Peel strategy:
![Peel](/assets/images/peel.png)

The function you're trying to test begins and/or ends with a line that is difficult to test. You want to peel that part away to get to the testable middle. Use an 'Extract Function' 

### Concrete: Peel
One way to solve [TirePressure](https://github.com/emilybache/custom-start-points/tree/master/start-points/TirePressure) is using Peel. You can also do it on 'getScore' in [IceCreamScores](https://github.com/emilybache/custom-start-points/tree/master/start-points/IceCreamScores/)

### Reflect - when to Peel
When should you use the ‘peel’ strategy? Are there any disadvantages to using it?
