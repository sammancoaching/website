---
layout: code_smell
title: Mutable Data
---

# Mutable Data
Data is changed during runtime, and other parts of the program keep a reference to it. When you update an existing data structure, all the clients that have a reference to it will be affected. Sometimes it's hard to predict what will happen, or it leads to synchronization problems in threaded code. An alternative to updating the data in-place is to return a copy of the whole data structure containing the updates. Functional programming often works this way. Even in object-oriented contexts you find immutable data structures though. Often a string is immutable - if you append something to one, you get back a new string.

Code that uses immutable datastructures if often easier to understand and reason about.

