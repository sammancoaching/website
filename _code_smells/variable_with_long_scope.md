---
layout: code_smell
title: Variable with Long Scope
source: Emily Bache
---

# Variable with Long Scope
Within a [Long Function or method](long_function.html) you often find local variables which are used over a long section of code. Any local variable that is in scope for more than a handful of lines is going to tax your short-term memory, especially if it is updated in several places.

Even read-only variables can complicate code if they have a long scope. Just that it's being used in a lot of places will make it harder to extract smaller functions or subroutines from the long function.

A global variable, by definition, has too long a scope. It taxes your brain to keep track of what state it's in when it can be accessed and potentially updated from anywhere in your program. A singleton class which has mutable state can behave similarly to a global variable. Watch out for that too.
