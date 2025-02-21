---
layout: refactoring
title: Extract Function
source: Martin Fowler
source_url: https://refactoring.com/catalog/extractFunction.html
code_smells: long_function
learning_hours: refactoring_vocabulary
---

# Extract function / Extract method

## Examine
Identify a section of a function or method which you would like to extract to its own function.

## Prepare
Scan the section of code you plan to extract for variables that should become arguments to the method. Do 'Extract Variable' on them and move them to before the block of code you want to extract.
In a similar way, work out what variables are updated and will need to be returned from the new function. If there are more than one, consider either extracting more than one method, or creating a new type to encapsulate all the updated values in one return value. Even if your language supports multiple return values, it's wise to consider this, since a function with a single return value is simpler to understand and maintain.

* IDE: select the block of code and do 'Extract Method' straight away. It will do the analysis for you and tell you want arguments it thinks you need. Cancel the refactoring when you've learnt what you need to know.
* IDE: 'Extract Variable' may be called 'Introduce Variable'

## Implement
* IDE: select the block of code and do 'Extract Method'

If that doesn't work, these are some manual steps:
* Create and empty new method, name it for what it does, not for how it does it.
* Copy the block of code from the source method to the new method
* Add parameters for local variables needed by the new method. If this is hard to do, then probably you needed to do more preparation. Go back and fix that and try again.
* Return any local variables that are updated. If there are more than one, more preparation is needed - go back and fix that and try again.
* Compile. The new function will be unused but should otherwise compile.
* Comment out the copied block of code and add a call to the new method.
* Test.

## Clear
* Delete any commented-out code.
* Inline method parameters if the previously extracted variables no longer make sense. 

## Follow up
Consider if the new method has [Feature Envy]({% link _code_smells/feature_envy.md %}) and if it should be moved somewhere else.