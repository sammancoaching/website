---
theme: surgery
title: Move the patient into the surgery
kata: grep_with_marketing
difficulty: 1
---

# Move the Patient into the Surgery

Part 1 of 4 learning hours on this topic. All are specific for the C language.

### Learning Goals
- list the steps needed to get a piece of C code into a surgery.
- explain when to use a surgery.
- distinguish between a patient successfully moved to a surgery and changes that broke the main build.

## Session Outline

* 5 min connect: What stops you writing tests?  
* 10 min concept: demo moving the patient  
* 30 min concrete: move the patient  
* 10 min conclusions: summarize the steps


### Connect - what stops you writing tests?

From this list, pick your top three reasons for not writing unit tests: 

- It’s boring: I don’t enjoy writing tests.
- The code has loads of dependencies that make it hard to test.
- We have testers so I don’t have to write unit tests.
- I usually plan to write the tests later, then forget or don’t get around to it.
- I don’t know any good test tools suitable for my situation.
- Unit tests would be unnecessary for the kind of high quality code I write.
- There’s no policy in our organization that says we should write unit tests. 
- It’s more profitable to invest in other kinds of testing.
- The code is not structured into small units so you can’t write unit tests for it.
- My manager told me not to spend too much time on testing, the focus should be on adding functionality.
- I add tests for all the easy cases and leave it at that.
- Add your ideas here…

### Concept: Surgery

Hopefully in the connect part someone mentioned that they struggle with dependencies that make the code hard to test. In my experience with C code, it often comes up. You can just say that if nobody picked it :-)

The 'surgery' technique is a concrete way to identify and get control of dependencies using link-time substitution. 

Show the starting code for [Grep with Marketing](https://github.com/objarni/grep-with-marketing). There are _two_ CMake projects. One for the main (production) code, and the other for the surgery. The idea is to keep the main production build running and able to be deployed, while moving the part of the code we want to test into the surgery. This is the code we call the 'patient'. In the surgery we can work on writing tests for the patient and refactoring it to be testable. When everything is ready we can move it back into the main build along with the new unit tests.

In this learning hour we're just going to practice moving a patient into the surgery while keeping the main build passing.

### Concrete: Move the patient

Follow the steps in the README file. You'll know you've succeeded when the main build passes and the surgery build also passes.

### Conclusions: What are the steps?

In pairs, copy the list of steps you used to take to get a patient into the surgery from the README. Edit as necessary so you understand what is meant. Put a star by the most important step(s). Put a question mark by any that you think could be done in a different order or which you think might be optional. Put a cross by any step you made a mistake in when you did it today.