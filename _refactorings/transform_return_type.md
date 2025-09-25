---
layout: refactoring
title: Transform Return Type
source: Emily Bache
source_url: 
code_smells: variable_with_long_scope, primitive_obsession
learning_hours:
---

# Transform Return Type aka Wrap Return Value

Some tools have this, Resharper includes it in the "Transform Parameters" refactoring. IntelliJ has an additional plugin that offers to [Wrap Return Value](https://www.jetbrains.com/help/idea/wrap-return-value.html#wrap_return_value_example). If you don't have those tools then these steps achieve the same thing with only 'Extract Function' and 'Inline Function.'

## Identify
Usually you want this refactoring when a method has multiple return values that and either you're only getting one of them, or you're putting them in an awkward collection type before returning them.

## Prepare
I usually find this one goes easier if I inline the method first (provided it's not called from too many places).

## Implement
* Identify which local variables will be combined into the new wrapper type, eg `var a; var b; var c;`. 
* Identify a position in the code after these local variables have all been declared and where you can create a new variable of the new type to wrap them.
* Pretend you already have the new class, declare a variable for it. Call its constructor with the arguments you want to put in the new type, eg `var wrapper = ReturnTypeWrapper(a, b, c)`.
* Use your tools to create that class `ReturnTypeWrapper`.
* Store all the constructor arguments in public fields.
* change all the references to these variables to use the fields of your new class, eg `a` becomes `wrapper.a`. (Use search and replace within a selection).
* 'Extract method' on all the code that uses `wrapper`. The method should have the signature you wanted.

## Clear


## Follow up

