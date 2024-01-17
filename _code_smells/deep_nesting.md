---
layout: code_smell
title: Deep Nesting
source: Emily Bache
---

# Deep Nesting
If code has many conditionals and loops nested inside one another, perhaps more than about 3 levels, then you'd say it has "deep nesting". It is a sign that the [cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) of the code is high, and the code is difficult to read and comprehend. The human brain has a limit of how much complexity it can hold at once, and deeply nested code is very likely to be beyond human capabilities of comprehension just because there are so many things to keep in mind at once.

If a method or function has several sections each with deep nesting then you would call it a [Bumpy Road]({% link _code_smells/bumpy_road.md %}) smell.

Most editors will automatically format code with indentation if you ask them to. You easily notice a deep nesting smell when the code has so many nested conditionals and loops that the indentation gets very deep.

## Other names for this smell

This smell is also known as **Heavy Indentation** because of the shape it makes on the page. In Michael Feathers book "Working Effectively with Legacy Code" he describes a **Snarled method** is one "dominated by a single large, indented section". The C2 wiki describes the [ArrowAntiPattern](http://wiki.c2.com/?ArrowAntiPattern).
