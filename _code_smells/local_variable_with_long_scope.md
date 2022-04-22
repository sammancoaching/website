---
layout: code_smell
title: Local Variable with Long Scope
---

# Local Variable with Long Scope
Within a [Long Function or method](long_function.html) you often find local variables which are used over a long section of code. Any local variable that is in scope for more than a handful of lines is going to tax your short-term memory, especially if it is updated in several places.

Even read-only variables can complicate code if they have a long scope. Just that it's being used in a lot of places will make it harder to extract smaller functions or subroutines from the long function.