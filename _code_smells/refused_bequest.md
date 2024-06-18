---
layout: code_smell
title: Refused Bequest
source: Martin Fowler
---

# Refused Bequest
When a subclass inherits methods and fields from their parents, but doesn't need them. It's often a sign that the subclass is not substitutable for its parent class. In that case it's a breach of the Liskov Substitution Principle.

