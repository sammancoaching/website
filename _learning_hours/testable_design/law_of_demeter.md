---
theme: testable_design
name: identify_and_resolve_law_of_demeter_violations
title: Identify and resolve Law of Demeter Violations
kata: fantasy_battle
difficulty: 3
author: gregorriegler
---

# Law of Demeter

The "Principle of Least Knowledge" is not a law, but rather a principle closely related to "Tell, Don't Ask". 
It advises against unnecessary communication with unfamiliar entities to avoid excessive coupling. 
Although it originates from object-oriented programming (OO), it is applicable beyond that paradigm. 
Violations of this principle are frequently observed in legacy code, making it difficult to comprehend and test. 
By understanding the principle, and being able to identify and resolve violations through refactoring, one can improve the design and make the code more testable.

## Learning Goals

* Understand the Law of Demeter
* Be able to recognize a violation of the LoD
* Apply refactorings to fix a violation of the LoD

## Session Outline
 
* 5 min connect: WebHunt for three facts about LoD.
* 5 min concept: Explain the LoD based on the found facts.
* 10 min concrete practice: Recognize violations of LoD
* 2 min: conclusion: Follow up and emphasize the solutions you liked
* 8 min concept: Demo a refactoring of resolving a LoD violation
* 25 min concrete practice: Practice the same refactoring
* 5 min conclusion: Discuss the advantages of LoD

## Connect: WebHunt for three facts about LoD

Group participants in pairs and have them research the Law of Demeter to come up with three facts.
Ask them to put the found facts on a shared board so everybody can see it.

## Concept: Explain LoD based on the found facts

Explain what the Law of Demeter says, but not necessarily why it says that. 
The advantages of LoD will be discussed in the final conclusion.
Explain that the Law of Demeter is about information hiding. 
You may use a phrase along the lines of: "a software module or an object should not have the knowledge of the internal workings of other objects or modules".
It can be useful to mention the alternate name of "Principle of Least Knowledge".
In the following concrete practice the participants will have to look at code and recognize a violation of the LoD.
When you used the phrase: "Don't talk to strangers.", it might be helpful to explain the concept of a neighbor and a stranger, too.

## Concrete Practice: Recognize Violations of LoD

Use simple code examples that either show a violation of LoD or don't. Have the participants work in pairs to draw the objects and their dependencies using boxes and arrows. 
When they see a dependency that is a violation they should paint the arrow red. 
Provide them with examples that make obvious that it is not just about dot counting. 
[Here](https://github.com/gregorriegler/law-of-demeter-examples) are some small code examples you may use.

## Conclusion: Follow up and emphasize the solutions you liked

Take a few minutes to present the participants solutions you liked in particular. 
This allows other learners to verify their own conclusions.

## Concept: Demo a refactoring of resolving a LoD violation

Demo how to resolve a small LoD violation by moving code to its neighbor. 
You may have to first use "extract method" before you can finally do a "move method" refactoring.
Rely on automated, tool-assisted refactorings in your demo as often as you can.
A nice kata for this purpose is the [FantasyBattle-Refactoring-Kata](https://github.com/Neppord/FantasyBattle-Refactoring-Kata).

## Concrete Practice: Practice the same Refactoring

Have the participants practice the same refactoring in pairs. In the FantasyBattle-Refactoring-Kata they will find many violations of LoD they can practice resolving.

## Conclusion: Discuss the advantages of LoD

Ask the participants what they think are some advantages of adhering to the Law of Demeter and put those on a wall for everybody to see.

## Further Links

- [Object-Oriented Programming: An Objective Sense of Style (Paper where LoD was first published)](https://www2.ccs.neu.edu/research/demeter/papers/law-of-demeter/oopsla88-law-of-demeter.pdf)
- [The Paper boy example](https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/)


