---
layout: code_smell
title: Heavy Indentation
---

# Heavy Indentation
Most code is easier to read if all the code in the same block has the same level of indentation, and most editors will automatically format code with indentation if you ask them to. You notice a heavy indentation smell when the code has so many nested conditionals and loops that the indentation gets very deep, or varies a lot.

Heavy indentation is a sign that the cyclomatic complexity of the code is high, and the code is difficult to read and comprehend. The human brain has a limit of how much complexity it can hold at once, and heavily indented code is very likely to be beyond human capabilities of comprehension just because there are so many things to keep in mind at once.