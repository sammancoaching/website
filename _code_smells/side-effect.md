---
layout: code_smell
title: Side Effect
---

# Side Effect
A function that does more than its name implies.
This is especially problematic when it involves unexpected state changes inside an object or its collaborators.

Example: if a method that looks like a query changes states which are not communicated through its name, it effectively is a command method.
