---
layout: code_smell
title: Long Function
---

# Long Function and Long Method
If the function is too long then it will often be difficult to read and understand. With a modern compiler then there is little performance impact to breaking out parts into subroutines. If those subroutines or private functions are named well, then it makes the original function much easier to read. A hint that you would do well to introduce a private function is the presence of a [comment](comments.html) explaining a block of code.