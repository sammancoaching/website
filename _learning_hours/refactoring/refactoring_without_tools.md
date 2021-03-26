---
theme: refactoring
title: Refactoring Without Tools
kata: tennis
difficulty: 1
---

# Refactoring without tools

You don't always have the tools you'd like to have, and they don't always work totally reliably. How do you handle that?

## Session Outline
 
* 5 min connect: what can go wrong?   
* 10 min concept: Steps of Extract Function
* 30 min do: pairs refactor Tennis1 
* 5 min reflect: what difference does fast, good tests make?

### Connect
Ask the group - What can go wrong when refactoring? How do you know if your refactoring was safe? Gather comments from the whole group and note them in a shared document or whiteboard.

Hopefully people will know that refactoring can be dangerous and the compiler and tests can protect you from mistakes.


### Concept - Refactoring steps
Sometimes refactoring tools don't have the refactoring you want. Sometimes they fail. It's useful to be able to plan and do refactorings without making mistakes even without much tool support. The classic "Refactoring" book to a large extent comprises checklists to break down a bigger change into short, safe steps, even when you have no refactoring tools. You rely on your compiler and your unit tests. You can summarize the way you work as:

"only be 1-3 undo steps away from passing tests"

That means that if the tests fail unexpectedly, you can always get back to a green state by doing 1-3 undo steps in your editor. You won't lose much work, and you can try again in a better way.

Explain this idea. As a group, come up with the steps for "Extract Method" or similar. (Use "Extract Function" if that is idiomatic for your language)

Imagine you are looking at a page of code from a long method and you've identified a block within it that you want to do "Extract Method" on.

1. Copy the block of code into the clipboard.
1. Declare a new empty, void method with no arguments. Call it 'foo' or something. 
1. Paste the code into it from the clipboard.
1. Work out what the method should be called and rename it.
1. Work out what the return type should be and fix up the method body to return it.
1. Work out what the arguments should be and fix up the method body to use them.
1. Compile and test.
1. Replace the original block with a call to the method.
1. Compile and test.

Your list will probably vary in details from this one, that is fine! The only rule is to be a few undo steps away from working code. If you like, compare whatever you come up with against the steps Martin Fowler has in his book.

If you think the group needs it, you can demo using the steps to perform the refactoring on the exercise code. Then reset the code so they can do it again for themselves.

### Exercise
Work on a refactoring exercise that needs that refactoring, for example Tennis. Have people use the steps you came up with earlier.

Choose an exercise that already has good, fast tests.

### Conclusions
Ask people to think about whether what they did was safe. How did it feel to have fast, reliable tests? Would you work differently if you didn't have that?

