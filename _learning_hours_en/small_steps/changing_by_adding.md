---
theme: small_steps
title: Adding Behavior Instead Of Breaking Behavior
difficulty: 4
author: jolod
affiliation: Jolod AB
---

# Adding behavior instead of breaking behavior

## Session outline

* 5 min connect: retroactively create tests
* 25 min concept: adding new behavior
* 25 min concrete practice: fizzbuzz-like exercise
* 5 min conclusions: applicability to production code

### Connect

Let the participants retroactively create test cases for the following function:

```python
def remove_prefix(pattern, string):
    """Removes the given regular expression pattern
    from the beginning of the string."""
    
    return re.sub(r"^" + pattern, "", string)
```

Before moving on, point out the logic contained in the function: _Removes the given **regular expression pattern** from the **beginning** of the string._

You want to test:

* That the prefix is removed.
* That the rest of the string is left intact.
* That the regex engine is in fact used.

You do not want to

* retest all of the regex engine.

Compare: If the function was written using strict TDD, which tests would you end up with?

### Concept: Keeping tests green

Highlight the following [quote](https://www.infoq.com/articles/API-Design-Joshua-Bloch/) from Joshua Bloch: "Public APIs, like diamonds, are forever."

Present the following principles:

* Write new code instead of breaking existing code.
* Remove "end-point" usages of the old code piece by piece.

This approach relies on the code being cohesive and decoupled ("well refactored").

Use **red-green-refactor** (and triangulation) to get tests that test the **new/changed behavior**. Avoids testing already tested behavior from reused functions. Just as with the Connect exercise, you do not want to retest reused functionality.

Do not blindly copy the old tests and code.

* Either the unit is sufficiently different to make it a completely new unit
* or the common pieces of the original unit can be refactored and reused.

Will generally keep the code well refactored.

Might seem like a lot of work for large systems, but the payoff is greater the larger the system.

### Concrete

You have an existing fizzbuzz-like program, with a main file that gives the desired output.

Example:

```text
1: One
2: Two
3: Fizz
4: Four
5: Buzz
6: Fizz
7: Whazz
8: Eight
...
105: FizzBuzzWhazz
```

A new rule should be added: every prime number should be shouted (i.e. all caps). A prime number is a positive integer evenly divisible by only two numbers (only by 1 and itself; one is not a prime number).

Example:

```text
1: One
2: TWO
3: FIZZ
4: Four
5: BUZZ
6: Fizz
7: WHAZZ
8: Eight
...
105: FizzBuzzWhazz
```

Implement this change without breaking or rewriting any existing unit tests, by first creating a function `shouting_fizzbuzzwhazz`, and then swapping out `fizzbuzzwhazz` in main.

#### Setup

The main program should contain the following functions and corresponding tests:

* `fizzbuzzwhazz` (like fizzbuzz, but also "Whazz" for numbers divisible by 7 and combinations, e.g. 3\*5\*7=105 gives "FizzBuzzWhazz").
  * The reason for adding more fizzbuzz factors is to get more combination, and to drive home the point about not retesting the underlying behavior.
* `is_prime`: returns true if the argument is a prime number, else false.
  * Optionally, let the participants practice TDD by implementing it themselves.
* `main`: prints the output, using `fizzbuzzwhazz`.
  * Optionally, have an approval test for main. If so, illustrate how the unit tests provide confidence that the number-by-number behavior is correct, and when approving the approval test you essentially scan the head and tail of the file to check that some lines have gotten capitalized. You do not need to re-check every prime number.

### Conclusions

Compare the tests for `shouting_fizzbuzzwhazz` with `fizzbuzzwhazz` and `is_prime` respectively. How well does the tests align with the functionality that the respective function provides? Is `shouting_fizzbuzzwhazz` retesting the fizzbuzz logic or prime checks?
