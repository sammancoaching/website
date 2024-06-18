---
layout: code_smell
title: Large Class
source: Martin Fowler
---

# Large Class
When a class is doing too much. It has too many fields and/or too many methods. It is a prime breeding ground for duplicated code, redundancy and confusion. You may want to find subsets of the methods and fields that are used together, and extract them into their own classes.