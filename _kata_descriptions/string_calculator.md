---
title: String Calculator
kata_name: string_calculator
---

# String Calculator

Let's write a calculator that takes a string and evaluates it as if it were a calculation. 
The idea is to implement it a bit at a time with tests, and see where the design ends up.
The kata description contains quite a detailed list of requirements and examples, written in the order you should implement them in. 

- Don't skip ahead or try to design more code than you need for the current tests. Your goal is to learn about incremental design and TDD from this exercise, not actually write a complete solution.
- The examples given are supposed to help you think about what's needed at each step of the solution. You can add more similar examples if you think the ones given aren't enough.


Note: if your language has a built-in 'eval' or another kind of runtime evaluation of string expressions - you're not allowed to use it in your solution to this exercise!


## Step 0 - Integers

Let’s start with the basics! If you give your String Calculator a single integer, just return that integer.

“1” -> 1
“456” -> 456
“-2” -> -2

## Step 1 - Addition

If you get two integers separated by a + sign, add them together.

“1+1” -> 2
“57+100” -> 157
“1000+0” -> 1000

## Step 2 - Subtraction

Also handle minus signs.

"-2" -> -2
“4-2” -> 2
"40-2" -> 38
“-2+2” -> 0
“-4-10” -> -14

## Step 3 - Whitespace

Whitespace should be ignored

"   1" -> 1
"1   " -> 1
"1 + 2" -> 3
"  45 - 60 " -> -15

## Further steps

I'm sure you can think of more steps to add here. Multiplication, floating point numbers, parentheses... Try to continue in the same style though. Add one small thing at a time with a test and just enough code to make it work, while all the existing tests also keep working.  

