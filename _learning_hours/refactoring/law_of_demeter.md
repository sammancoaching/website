---
theme: refactoring
title: Law of Demeter
name: law_of_demeter
kata: fantasy_battle
difficulty: 3
author: neppord
affiliation: ProAgile
---

# Law of Demeter

This learning hour introduces the Law of Demeter and some concrete techniques for tackling code that breaks it.

## Session outline

* 10 min connect: Recognize these smells?
* 15 min concept: Law of Demeter
* 25 min concrete: Refactor the Player class
* 5 min conclusions: Write an important takeaway

## Connect - Recognize these smells?

Put descriptions of these three code smells around the room or on a shared online whiteboard. Have people form pairs and go around and read them. If they recognize the smell, and have experienced it in their work, put a "nose" sticker next to it. Give them a pile of nose stickers or brightly coloured postit notes.

* [Shotgun Surgery]({% link _code_smells/shotgun_surgery.md %})
* [Divergent Change]({% link _code_smells/divergent_change.md %})
* [Message Chains]({% link _code_smells/message_chains.md %})

You're hoping that people recognize all of these, especially the last one, since that's what this learning hour is mostly about.

## Concept - Law of Demeter
Explain what this is and why it's a problem. You might like to summarize it as "talk to your friends, not your friend's friends", or "avoid train wrecks". 

Put the code sample below on a shared screen. It's from the [FantasyBattle-Refactoring-Kata](https://github.com/Neppord/FantasyBattle-Refactoring-Kata).  Get some "train" stickers or similar. Ask them where you should put the stickers in the code to show where it's breaking the Law of Demeter.

    private int CalculateBaseDamage() {
            Equipment equipment = Inventory.Equipment;
            Item leftHand = equipment.LeftHand;
            Item rightHand = equipment.RightHand;
            Item head = equipment.Head;
            Item feet = equipment.Feet;
            Item chest = equipment.Chest;
            return leftHand.BaseDamage +
                   rightHand.BaseDamage +
                   head.BaseDamage +
                   feet.BaseDamage +
                   chest.BaseDamage;
        }

You should end up with stickers on almost every line. This should lead you directly into the demo where you show how to do Introduce - Extract - Move to fix the problem.

The essence of the demo is to refactor the method CalculateBaseDamage to follow the Law of Demeter. _Introduce_ a variable for Inventory, _Extract method_ on all the rest of the method, so you get a new method with one argument, inventory. Then _Move_ the method to Inventory. Now in class Inventory you do basically the same thing again. _Extract_ all the method contents so you get a new method with one argument - equipment - then _Move_ that method to Equipment.

The refactoring sequence is:
* [Introduce variable]({% link _refactorings/introduce_variable.md %})
* [Extract method]({% link _refactorings/extract_function.md %})
* [Move method]({% link _refactorings/move_function.md %})

Note there are no test cases in the default branch so it's important to know your tools are good enough to do these refactorings for you, or that you are following the refactoring steps strictly.

## Concrete - Fix the Player class
As with the demo, remove the Law of Demeter problems in the Player class by creating new methods and moving them to inventory and equipment. When you've completed that, similarly refactor the other method "CalculateDamageModifier". That one is almost the same but you have to handle the strengthModifier too.

When you've completed the refactoring, you should not be able to find any Law of Demeter problems in any of the classes, and all the methods will have good names that express what they do.

## Conclusions
[Write an important takeaway]({% link _activities/conclusions/write_important_takeaway.md %}). How will what you learned today change how you code in the future?

