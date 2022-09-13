---
layout: code_smell
name: global_data
title: Global Data
source: Martin Fowler
---

# Global Data
Data that can be modified from anywhere in the codebase. It's difficult to reason about and difficult to unit test. It's particularly bad if you can't easily find all the pieces of code that change the global data. A Singleton is a kind of global, as are class variables. Global data that you can guarantee remains unchanged after the program starts is less problematic.