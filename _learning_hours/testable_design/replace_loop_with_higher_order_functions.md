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

* Get to know common Higher-Order Functions in Functional Programming
* Learn how to apply them in the place of loops

Describe the three common filter, map, and reduce
Use those three to convert a loop ...

## Session Outline

* 5 min connect: Higher-order functions
* 10 min concept: Common higher-order functions in various programming languages
* 30 min do: Apply common higher-order functions
* 10 min reflect: Typical use cases

### Connect: Higher-Order Functions

Ask these questions in the group, and give them some time to write down some answers on sticky notes etc.

* Do you know this term? Explain it briefly.
* Do you know any common higher-order functions?

The kinds of answers you are looking for are:
1) A higher-order function is a function that takes another function/method as argument or that
returns another function/method.

2) See "Concept".


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


### Do: Applying Common Higher-Order Functions

Implement the following functions, either using a text editor or IDE or by writing (pseudo) code on post-it's.
Also write unit tests for them.

* Apply filter / Where / select:

A function *even* that takes a list of integers and returns a list that only contains the even 
numbers from the original list, in the same order.
_Example:_ even([1, 2, 3, 4, 5, 6, 7]) = [2, 4, 6]

* map / Select / collect:

A function *plusOne* that takes a list of integers and returns a list where each element of the original ist is incremented by one, retaining the order.
_Example:_ plusOne([1, 2, 3]) = 6

* fold or reduce / Aggregate / inject:

A function *sum* that takes a list of integers and returns the sum of its elements. _Example:_ sum([1, 2, 3]) = 6
A function *reverse* that takes a list of integers and returns the reverse of that list. _Example:_ reverse([1, 2, 3]) = [3, 2, 1]


### Reflect: What are typical use cases for these functions?

Ask the following questions in the group. First let them reflect silently for a minute or two, then discuss.

* Now that you have learned about the three common Higher-Order Functions filter, map, and reduce:
Do you have typical use cases in your production code where you could apply one of the three functions? Which are they?

<link to template>