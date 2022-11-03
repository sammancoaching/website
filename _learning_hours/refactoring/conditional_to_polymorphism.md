---
theme: refactoring
title: Replace Conditional With Polymorphism
kata: parrot
difficulty: 3
author: emilybache
affiliation: Praqma
---


# Replace Conditional With Polymorphism

This refactoring replaces conditional logic with classes and polymorphism. The code smell that leads you to it is having a lot of similar switch statements that switch on type. In this session we'll practice doing it, and hopefully see just how good modern IDE tooling is for this kind of task.

## Session Outline
 
* 5 min connect: top tips for refactoring productivity
* 2 min concept: describe the smell and the refactoring
* 15 mins demo: Parrot, using IDE shortcuts   
* 25 min do: Parrot in pairs
* 5 min reflect: IDE shortcuts and productivity

### Connect - Refactoring and productivity
If you were advising a junior developer which tools to use for refactoring, what would you say?

### Explain the Parrot exercise
Show the starting position of the [Parrot Refactoring Kata](https://github.com/emilybache/Parrot-Refactoring-Kata) and explain the code smell - the switch statement that switches by type. Explain and sketch the refactoring that addresses this smell: 'Replace Conditional with Polymorphism'. 

It's also useful to run the tests and show they have good coverage and should be reliable for finding refactoring errors.

### Demo Parrot
You want to help people become more productive at refactoring, and this demo is about inspiring them with what's possible. Make it slick, make it fast. Put the tests on auto-run, or run them using a shortcut after every change. 

It's worth doing some research into the capabilities of your IDE here. In my experience, you can do nearly everything with shortcuts, almost no typing required. Not every language has equivalent support though. 

Timebox the demo and stop wherever you've got to. Leave them scope for improvements they can come up with themselves, to keep it interesting. 

I suggest you write the keyboard shortcuts you used on a whiteboard. You'd like them to refer to this list when they do the exercise themselves. For example you might end up with something like this (IntelliJ 2019.3.1, Java):

- Replace constructor with factory method
- Change access modifier
- Create class
- Change Signature
- Safe delete
- Override method
- Inline Method
- Encapsulate Field
- Push Members Down

or (CLion 2022.2.3, C++)

- Generate Definition for 'createParrot' declared in Parrot.h
- Create new C++ class 'EuropeanParrot' and inherit Parrot manually, or Subclass... and manually add to target.
- Generate constructor
- Import EuropeanParrot.h
- Remove declaration of parameter 'parrotType'
- Override functions... (watch out for checkbox 'show non-virtual functions')
- increase function visibility, make protected
- Safe delete
- Push Members Down
- Inline function (Only works if there is only one return in the function.)
- Change Signature
- Introduce Constant...


### Do Parrot
People should work in pairs to do the same exercise again from the start. If they lack IDE experience, they should follow your list of shortcuts from the whiteboard. More confident pairs may know other shortcuts and can try to achieve the same thing in a different way. Ask them to write down their sequence of steps if so.

People who are very skilled with the IDE already may complete the exercise very quickly. In that case ask them to do it with strict strong style pairing. The navigator will only say the high-level intent and the names of the refactorings. The driver is expected to know the shortcuts. They shoud do it twice, so each person experiences each role.

### Reflect: IDE shortcuts and productivity
Ask the group:

- Tell me three ways IDE shortcuts like these affect your productivity as a developer. 

Note the answers on a flipchart. You're hoping they will say things like:

- they help you to think at a higher level of abstraction. 
- as a navigator if you know the names of these you can communicate more effectively with the driver
- it takes time to learn them
- if your usual IDE doesn't have them you might want to switch, which could be costly
- a long sequence of small refactorings means you can make a larger change safely, avoiding bugs

Put the flipchart up in the team area.
