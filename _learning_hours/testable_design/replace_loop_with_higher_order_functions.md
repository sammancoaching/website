---
theme: functional_programming
title: Replace Loop with Higher-Order Functions
difficulty: 2
author: nicolerauch
tags: functional_programming streams higher_order_functions design
code_smell: loops
name: replace_loop_with_higher_order_functions
---

# Replace Loop with Higher-Order Functions

Having a look at other programming paradigms broadens the horizon, and maybe you can even find
something that's useful in your daily work as a programmer, even while using a different paradigm.

Higher-order functions are at the core of functional programming, and other programming languages
also introduced this feature, where it may be called "lambda", "functional interface", "anonymous function" or
the like. Therefore it is worthwhile to find out more about them.


## Learning Objectives

* Learn to describe the three common higher-order functions filter, map, and reduce
* Learn how to apply them by converting a given piece of code that contains a loop.

## Session Outline

* 5 min connect: Higher-order functions
* 10 min concept: Common higher-order functions in various programming languages
* 30 min do: Apply common higher-order functions
* 10 min reflect: Typical use cases

### Connect

Ask these questions in the group, and give them some time to write down some answers on sticky notes etc.

* What do you call a function that takes a function as an argument or that returns a function?
* Have you ever done this in your code? What was the use-case?


The kinds of answers you are looking for are:
1) These functions are called higher-order functions.

2) - various applications related to the Java streaming API
   - callback functions
   - event listeners
   - decorators
   - middleware pipelines
   - function composition (i.e. building more complex functions from simple ones)
   - strategy pattern (passing a specific algorithm to a function that implements the general structure)

### Concept: Common Higher-Order Functions

Common higher-order functions are:

1. filter
2. map
3. fold / reduce

That is their name in many programming languages.

C# LinQ calls them:

1. Where
2. Select
3. Aggregate

while Ruby and Smalltalk call them:

1. select
2. collect
3. inject

Explain how these work. Maybe draw some images to illustrate the flow of data.

* filter / Where / select:

Array -> Function -> Array

Takes an array and a boolean function, returns a new array that contains only those entries where the function returns true.

* map / Select / collect:

Array -> Function -> Array

Takes an array and a function, returns a new array that contains the results of the function applied to the values of the original array in the same order.

* fold or reduce / Aggregate / inject:

Array<V> -> (V,A)->A -> A -> A

Takes an array of values, an aggregator function that aggregates the array's values one by one into an output value, 
and an initial output value, and returns the final output value (after all array values have been aggregated).

Here are [some tips on how to run this]({% link _activities/concept/lecture.md %}).

### Concrete: Applying Common Higher-Order Functions instead of Using Loops

Give the participants some loops that they can refactor to use filter, map, and reduce.

There are some examples with tests in [Replace Loop](https://github.com/NicoleRauch/Learning_Hour_Replace_Loop) You can pick some or all of the provided examples.
Make sure to set a time box for each of the functions (~5 min for filter, ~5 min for map, 
~10 min for reduce, with some grace time) so that everybody can work at their own pace.
Not everybody will be able to finish all of the exercises, which is totally fine.

Let them work in pairs - either pair up more experienced with less experienced participants, or build pairs of
similarly (in-)experienced participants. You can [find some more suggestions and details here]({% link _activities/concrete/work_in_pairs.md %}).


### Conclusions: What are typical use cases for these functions?

Ask the following question in the group. First let them reflect silently for a minute or two, then discuss.

* Now that you have learned about the three common Higher-Order Functions filter, map, and reduce:
Do you have typical use cases in your production code where you could apply one of the three functions? Which are they?

Another [idea of running this can be found here]({% link _activities/conclusions/how_to_apply_here.md %}).
