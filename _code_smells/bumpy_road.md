---
layout: code_smell
title: Bumpy Road
source: Adam Tornhill
---

# Bumpy Road
Code is easier to read if all the code in the same block has the same level of indentation. Most editors will automatically format code with indentation if you ask them to. You notice a bumpy road smell when the code has so many nested conditionals and loops that the indentation gets very deep, and/or varies a lot. 

Bumpy road is a sign that the [cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) of the code is high, and the code is difficult to read and comprehend. The human brain has a limit of how much complexity it can hold at once, and heavily indented code is very likely to be beyond human capabilities of comprehension just because there are so many things to keep in mind at once.

## Other names for this smell

This smell has many other names, for example **Heavy Indentation** or **Deep Nesting**. The name "Bumpy Road" comes from an article by Adam Tornhill [The Bumpy Road Code Smell: Measuring Code Complexity by its Shape and Distribution](https://codescene.com/blog/bumpy-road-code-complexity-in-context). 

In Michael Feathers book "Working Effectively with Legacy Code" he describes a similar smell: a **Snarled method** is one "dominated by a single large, indented section". It's a Bumpy Road with only one bump. Similarly the C2 wiki describes the [ArrowAntiPattern](http://wiki.c2.com/?ArrowAntiPattern).
