---
theme: small_steps
title: Triangulation
difficulty: 3
author: jolod
affiliation: Jolod AB
---

# Triangulation

## Session outline

* 10 min connect: what to test?
* 20 min concept: triangulation demo and explanation.
* 20 min concrete practice: kata, e.g. mars rover.
* 10 min conclusions: when to use.

### Connect

Discuss in pairs:

* How do you decide which tests to write/keep?
* How do you decide where a test belongs?

### Concept - Just-in-time generalization

Triangulation is about helping you to generalize "just in time". The currently red test focuses your attention to a particular pieces of the code, and when it grows in an "uninteresting way" (e.g. just adding special cases), it is an indication that you have pinpointed a point in the code where a more general property perhaps would be appropriate.

Start with a demo of fizzbuzz showing the following steps:

```python
# 1 -> '1'
def fizzbuzz(n):
    return '1'

# 4 -> '4'
def fizzbuzz(n):
    if n == 4:
        return '4'
    return '1'

# Generalise
def fizzbuzz(n):
    return str(n)

# 3 -> 'Fizz'
def fizzbuzz(n):
    if n == 3:
        return 'Fizz'
    return str(n)

# 9 -> 'Fizz'
def fizzbuzz(n):
    if n == 3 or n == 9:
        return 'Fizz'
    return str(n)

# Generalise
def fizzbuzz(n):
    if n % 3 == 0:
        return 'Fizz'
    return str(n)

# 5 -> 'Buzz'
# 10 -> 'Buzz'
# Generalise

# 15 -> 'FizzBuzz'
def fizzbuzz(n):
    if n == 15:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return str(n)

# 30 -> 'FizzBuzz'
def fizzbuzz(n):
    if n == 15 or n == 30:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return str(n)

# Generalise
def fizzbuzz(n):
    if n % 15 == 0:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return str(n)
```

Point out how triangulation "forces" you to write at least two tests per "Fizz", "Buzz", and "FizzBuzz" output respectively.

Triangulation is about generalizing "just in time". The goal is to avoid:

* Under testing: Exposes accidental repetition in tests.
* Over testing: Avoids retesting already tested behaviour in dependencies.
* Unnecessary generalization: Avoids solving a problem not needing to be solved.

### Concrete practice

Do a kata, for example the mars rover kata but focus on movements (and not on rotations).

### Conclusion

Ask the participants "In what situations do you think triangulation is particularly useful? And not so useful?".
