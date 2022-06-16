---
layout: code_smell
title: Comments
source: Martin Fowler
---

# Comments
Comments are often not a smell at all - they can be very helpful. Particularly if they explain _why_ a piece of code is written like it is. However, sometimes people write comments instead of taking the time to make the actual code readable and self-explanatory. If you need a comment, it could be a sign you have a [primitive obsession](primitive_obsession.html) instead of using domain classes, or could do with better names for your classes and functions. Some comments would be better off as assert statements documenting your assumptions.
