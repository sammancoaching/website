---
theme: testable_design
name: law_of_demeter
title: Law of Demeter
kata: fantasy_battle
difficulty: 3
author: gregorriegler
---

# Law of Demeter

In legacy code we often see code that is strongly coupled and has a low cohesion.
There, information hiding is not applied and we see lots of unnecessary dependencies and violations of the Law of Demeter.
This sort of code is usually hard to understand and test.
Understanding LoD and being able to apply it and make refactorings to resolve violations of LoD helps to make code less complex, easier to read and test. 

## Learning Goals

* Understand the Law of Demeter
* Be able to recognize a violation of the LoD
* Apply refactorings to fix a violation of the LoD

## Session Outline
 
* 5 min connect: WebHunt for three facts about LoD.
* 5 min concept: Explain the LoD based on the found facts
* 10 min concrete practice: Recognize violations of LoD
* 2 min: conclusion: Follow up and emphasize solutions you liked
* 8 min concept: Demo a refactoring of resolving a LoD violation
* 25 min concrete practice: Practice the same refactoring
* 5 min conclusion: Discuss the advantages of LoD

### Connect: WebHunt for three facts about LoD

Group participants in pairs and have them research the Law of Demeter to come up with three facts.
Ask them to put the found facts on a shared board so everybody can see it.

### Concept: Explain LoD based on the found facts

Explain what the Law of Demeter says, but not necessarily why it says that. The advantages of LoD will be discussed in the final conclusion.
Explain that the Law of Demeter is about hiding information. 
You may use a phrase along the lines of: "a software module or an object should not have the knowledge of the internal working of other objects or modules".
It can be useful to mention the alternate name of "Principle of Least Knowledge".
In the following concrete practice the participants will have to look at code and recognize a violation of the LoD.
So explain what a neighbor is, and that we consider a neighbor of a neighbor a stranger, as it is internal detail of said neighbor that we should not know about.

### Concrete Practice: Recognize violations of LoD

Use simple code examples that either show a violation of LoD or don't. Have the participants work in pairs to draw the objects and dependencies they see in the code using boxes and arrows. When they see a dependency that is a violation they should paint the arrow red. Make sure they will notice that it is not just about dot counting. [Here](https://github.com/gregorriegler/law-of-demeter-examples) are some small code examples you may use.

### Conclusion: Follow up and emphasize solutions you liked

Use a few minutes to present the solutions of participants of the previous exercise you liked in particular. This helps other participants verify their own conclusions.

### Concept: Demo a refactoring of resolving a LoD violation

Demo how to resolve a small LoD violation by moving the code to the neighbor. You may have to first use "extract method" in some occasions. Finally you want to do a "move method" refactoring.
Rely on automated, tool-assisted refactorings in your demo.
A nice kata for this purpose is the [FantasyBattle-Refactoring-Kata](https://github.com/Neppord/FantasyBattle-Refactoring-Kata).

### Concrete Practice: Practice the same Refactoring

Have the participants practice the same refactoring in pairs. In the FantasyBattle-Refactoring-Kata they will find many more violations of LoD they can further try and resolve through refactoring.

### Conclusion: Discuss the advantages of LoD

Ask the participants what they think are advantages of adhering to the Law of Demeter and put those on a wall for everybody to see.


## Further Links

[Object-Oriented Programming: An Objective Sense of Style (Paper where LoD was first published)](https://www2.ccs.neu.edu/research/demeter/papers/law-of-demeter/oopsla88-law-of-demeter.pdf)
[The Paper boy example](https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/)


