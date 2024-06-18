---
layout: code_smell
title: Paragraph of Code
source: Emily Bache
---

# Paragraph of Code

A paragraph is a section of code within a longer function or method that belongs together, does something specific, and might make sense to extract and name as a method. Giving the section of code a name and explicitly stating the arguments, dependencies and return value would almost certainly be easier to read and reason about than an unnamed section of code.

You can spot code paragraphs without reading the code in any detail, they have one or more of these visual characteristics:

* begin with a short comment explaining what the next lines of code do
* are in a code block (ie they are between a pair of curly braces or at the same indentation level)
* begin with a for, if, try, switch or while statement
* have a line of whitespace before and after
* a cluster of statements using the same variable name or recurring word

