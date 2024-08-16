---
layout: code_smell
title: Case or Switch Statements
source: Martin Fowler
---

# Case or Switch Statements
Each language has a way of defining a nested block of code that controls what code is executed under certain conditions. They usually start with a `case` or `switch` keyword, but they could also be a list of `if/elif` conditions.

The problem is not necessarily with a case statement, switch statement, or a collection of if/else statements. **It's that these could hide duplication or an idea that wants to emerge.**  

Often, the same switch statement is scattered throughout a program in different places. If you add a new clause to the switch, you must find and change all these switch statements.
