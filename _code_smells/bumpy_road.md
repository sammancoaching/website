---
layout: code_smell
title: Bumpy Road
source: Adam Tornhill
---

# Bumpy Road
If a method or function has several sections each with a [Deep nesting]({% link _code_smells/deep_nesting.md %}) smell, then the indentation will form a lumpy pattern with several 'bumps'. Each section with deep nesting probably represents a different responsibility or action that could usefully be separated out into its own function.

## More information

The name "Bumpy Road" comes from an article by Adam Tornhill [The Bumpy Road Code Smell: Measuring Code Complexity by its Shape and Distribution](https://codescene.com/blog/bumpy-road-code-complexity-in-context). 
