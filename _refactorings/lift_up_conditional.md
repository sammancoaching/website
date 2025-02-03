---
layout: refactoring
title: Lift Up Conditional
source: Emily Bache
code_smells: duplication
learning_hours: lift_up_conditional_intro
---

# Lift-up Conditional
This refactoring was named by Emily Bache. She first learned it from Llewellyn Falco.

## Examine
Look for a complex conditional that has a condition that is duplicated in more than one place. This is the conditional you will 'lift up' to be only in one place at the top. Note - in this process another conditional might become duplicated instead, so it doesn't always help.

## Prepare
Copy the section of code containing the conditional.

## Implement

* Tests all passing
* Select the whole piece of code with the duplicated conditional in, copy to clipboard
* Surround with if/else
* Ensure you have the whole piece of code duplicated in both if and else clause
* Put the conditional you want to 'lift up' into the if condition
* All tests passing
* In the 'if' section, carefully replace the condition with 'true'. In 'else' section, carefully replace it with 'false'.
* All tests passing
* Simplify 'true' and 'false' conditionals
* All tests passing

## Clear
Check whether the conditional really is simpler now, if not revert.

## Follow up
Once the conditional is clearer, consider extracting and naming parts of it.
