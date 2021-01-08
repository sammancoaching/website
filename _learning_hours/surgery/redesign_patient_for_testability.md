---
theme: surgery
title: Refactor for testability
kata: grep_with_marketing
difficulty: 3
---

# Refactor the patient for testability

part 3 of 4 learning hours on this theme.

### Learning Goals
- define a 'seam'
- explain why we want to refactor to function pointers
- use refactoring to change the way a test inserts a stub
- analyse when to use link-time substitution and when a #define or function pointer is a better choice

## Session Outline

* 5 min connect: How to substitute behaviours in C  
* 10 min concept: Using function pointers to insert stubs  
* 35 min concrete: Refactor to function pointers  
* 5 min conclusions: confidence in these tests?

### Connect

In C, which of these allow you to substitute a different behaviour at: 

- 🐝 runtime 
- 🐙 compile time 
- 🍄 link time  
- ☕ does not allow you to substitute behaviour

- #define 
- typedef
- Function pointer
- Makefile

There are four symbols and four proposals. Pair them up.

### Using function pointers to insert a stub

In the exercise repo [Grep with Marketing](https://github.com/objarni/grep-with-marketing) there is a branch 'with_coverage'. The patient is in the surgery and fully covered with unit tests. We are ready to refactor it for testability. Explain that we need better seams so we can introduce stubs without using link-time substitution. 

### Refactor to function pointers
There are three stubs - it might be best to demo the first one. Introduce function pointers for each stub. This will also mean changes in the production code. 

### Conclusions
Go through the code listing for your final code. Write a comment // SEAM on any line of code you think is a seam. If you're not finished with the refactoring, note there is a branch 'with_abstractions' which you can examine and annotate with SEAM comments.

Compare your answers with someone else and discuss any differences. Explain to the other person how you'd define a Seam.
