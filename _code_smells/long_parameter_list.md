---
layout: code_smell
title: Long Parameter List
---

# Long Parameter List
If the argument list is long, then your function or method is probably difficult to understand and reason about. Sometimes a group of the arguments form a [Data Clump](data_clumps.html), which gives you a clue about how to fix it. (Move them all onto a class and just pass that class). It's usually not a good idea to reduce the size of an argument list by introducing [Global Data](global_data.html).