---
layout: refactoring
title: Peel
source: Emily Bache
code_smells: long_function
learning_hours: peel
---

# Peel
Emily Bache first learned this refactoring from [Llewellyn Falco]({% link society/contributors/isidore.md %}).

## Examine
Look for a long function that you want to get under test, which includes a statement or short paragraph that makes it hard to test. Usually it refers to a dependency you don't want to include in your unit test. If you can easily slide this function to the start or the end of the function then use Peel. Otherwise, try [Slice]({% link _refactorings/slice.md %}).

## Prepare
Isolate the smallest possible part that you want to be able to peel out of this function. This part will not be included in a subsequent unit test, so you want to make it as little logic as possible. You might want to extract a variable so it's separated from the surrounding code.

## Implement
* If the code you want to peel is not already on the first or last line of the function, use 'slide statement' to move it there. Note – if you can't achieve this, use [Slice]({% link _refactorings/slice.md %}) instead.
* Select the whole function body apart from the code you want to peel and do [Extract Function]({% link _refactorings/extract_function.md %}). You should get a new function that is easier to test than the original.

## Clear
Check the new function name is suitable and the visibility makes it possible to unit test.

## Follow up
* Move and/or create tests for the new function.
* Move the new function to another class where it fits better.
