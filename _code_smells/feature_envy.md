---
layout: code_smell
name: feature_envy
title: Feature Envy
source: Martin Fowler
---

# Feature Envy
When a function in one class or module makes extensive use of functions and/or data from another class or module, so much so that it probably belongs there. Usually in an object-oriented design you want functions to live on the same class as the data they work with. Put together things that change together.
