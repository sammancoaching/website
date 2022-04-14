---
layout: code_smell
title: Repeated Switches
---

# Repeated Switches
If you see the same `switch` statement in several places, it's a sign that you could be using a more flexible and dynamic structure like polymorphism. One switch statement by itself perhaps isn't too dangerous, but if you have several then it's annoying duplication. If you add a new clause to one switch statement, you probably have to remember to update all of them.
