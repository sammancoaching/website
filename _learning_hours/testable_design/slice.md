---
theme: testable_design
title: Strategy - Slice
kata: tire_pressure
difficulty: 3
---

# Strategy - Slice
For when 'Peel' strategy doesn't work, like when the difficult-to-test code is in the middle of the testable code, not at the beginning or end.

## Session Outline
 
* 5 min connect: identify testability problems
* 10 min concept: Slice   
* 40 min do Slice on a function
* 5 min reflect: When to Slice

### Connect - identify testability problems
Copy a symbol next to the items on this list which might make a function difficult to test:
- Function is void ie no return value
- Function name is more than 20 characters
- Function has only one statement
- Function gives different return values for same input parameters 
- Function has an empty parameter list
- Function contains log statements using printf
- Function is called from many places in the system


### Concept: Slice
This picture visualizes the Slice strategy:
![Slice](/assets/images/slice.png)

The function you're trying to test has a line that is difficult to test in the middle. You can't easily use Peel to remove it. You need to slice away the depencency and replace the hard to test call with a call to a stub or a fake.

### Concrete: Slice
One way to solve [TirePressure](https://github.com/emilybache/custom-start-points/tree/master/start-points/TirePressure) is using Slice. You can also do it on 'getScoreboard' in [IceCreamScores](https://github.com/emilybache/custom-start-points/tree/master/start-points/IceCreamScores/)

### Reflect - when to Peel, when to Slice
What is important to remember when you add tests to code containing a call to a difficult-to-test function?

