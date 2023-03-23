---
theme: refactoring
title: Lift-Up Conditional on Gilded Rose
name: lift_up_conditional
kata: gilded_rose
difficulty: 3
author: claresudbery
via: xaviametller
---

# Lift-Up Conditional on Gilded Rose

Using the "Lift-Up Conditional" refactoring to detangle complex if statements. 

This is a powerful, satisfying and almost magical refactoring technique. It’s really useful for detangling complex knots of if statements. Llewelyn Falco came up with the technique, and Emily Bache named it. There’s a good video by Emily demonstrating the technique [here](https://www.youtube.com/watch?v=OJmg9aMxPDI).

The basic principle is to find conditions that are repeated throughout the code and then “lift them up” so that each condition has its own dedicated branch of the code. The result is that we can replace the original complex if statement with a switch statement. Once we’ve done that, we can replace the switch statement with polymorphism (see [Replace Conditional With Polymorphism]({% link _learning_hours/refactoring/conditional_to_polymorphism.md %})).

In this learning hour we demonstrate the technique, and then let the participants try it out for themselves on the [Gilded Rose Refactoring Kata]({% link _kata_descriptions/gilded_rose.md %}). You can do this in one hour, but as the technique takes a bit of time to really understand, it’s a good idea to do this [intro learning hour]({% link _learning_hours/refactoring/lift_up_conditional_intro.md %}) first.

This [slide deck](https://docs.google.com/presentation/d/11HjxVD99vyKyt8HT_5UHIBnAnr4Pck5g/edit?usp=sharing&ouid=117794872566978197093&rtpof=true&sd=true) (also available as a [pdf](https://drive.google.com/file/d/11cEwkIv2NRWLkSCQfqltXIkNUTzCQFyW/view?usp=sharing)) contains all the resources on this page plus more - many of which may be useful in preparing for this learning hour.


### Learning Goals

- Use Keyboard shortcuts to do Lift-up conditional on Gilded Rose
- Recognize when Lift-up conditional would be an appropriate technique to try  

## Session Outline

* 5 min connect: favourite keyboard shortcuts
* 15 min concept: Lift-up conditional
* 30 min concrete: Do Lift-up conditional on Gilded Rose
* 5 min conclusions: What's been learnt

### Connect: Favourite Keyboard Shortcuts

As a whole group, ask participants to answer the question “What are your favourite keyboard shortcuts in [insert relevant IDE, eg Visual Studio]?”

You can ask them to write their answers on stickies using a tool like Miro, Mural or Jamboard, or in bullet points in a shared doc, or on actual stickies in person.

This is a good exercise to get them thinking about keyboard shortcuts, which witruell be useful in this exercise and are demonstrated in the videos linked to below. Hopefully some of them will learn new shortcuts as a result of this exercise.

### Concept: Lift-up Conditional Demo
I find it helpful to use schematics to visualise what’s happening, as if you haven’t seen the technique before it can be confusing at first. I also show the Gilded Rose code before and after, to show what we’re aiming for and get them primed for what I’m about to demonstrate.

![Lift Up Conditional Simple Schematic](/assets/images/lift_up_conditional_simple_schematic.png){: width="600"}

This [slide deck](https://docs.google.com/presentation/d/11HjxVD99vyKyt8HT_5UHIBnAnr4Pck5g/edit?usp=sharing&ouid=117794872566978197093&rtpof=true&sd=true) (also available as a [pdf](https://drive.google.com/file/d/11cEwkIv2NRWLkSCQfqltXIkNUTzCQFyW/view?usp=sharing)) contains two versions of the schematic above, as well as a more detailed example using the same principle. I recommend only using the more detailed version if you are planning to devote two learning hours to this activity. Even then, you may prefer the shorter simpler version.

I follow the schematics with this video of a [C# demo of the technique](https://vimeo.com/801311948/41a83a3c4e), played at double speed, with me talking over the top. [This branch of the Gilded Rose kata](https://github.com/claresudbery/GildedRose-Refactoring-Kata/tree/csharp-liftup-demo) contains a commit for every step I made in the video. The tests were passing at each commit. There is also this [video of Emily Bache demonstrating the technique in Java](https://www.youtube.com/watch?v=OJmg9aMxPDI), but it’s quite long so you might want to make your own or select only some short snippets to show.

### Concrete: Do Lift-up Conditional

In pairs, ask them to attempt the technique themselves on the Gilded Rose code base. Encourage them to move in small steps and make sure the tests pass after each tiny change. For C#, I give them [this C# starting point](https://github.com/claresudbery/GildedRose-Refactoring-Kata/tree/csharp-liftup-start. I did the following, which got them moving as quickly as possible:

* All other languages have been removed from this branch, to avoid distraction and make it clear where to start
* The approval tests are set up for maximum coverage and will pass as soon as they open the code
* Participants downloaded the code and made sure they could build it and make the tests pass before we started the workshop (I have [notes on how to handle any Visual-Studio-related gotchas](https://clare-wiki.herokuapp.com/pages/think/code-princ/Gilded-Rose#gilded-rose-working-in-visual-studio))

I also added the above schematic and these [instructions on using the approval tests](https://clare-wiki.herokuapp.com/pages/think/code-princ/Gilded-Rose#gilded-rose-getting-started-with-approval-tests-in-c) to a central location (a Mural board and a Google doc) which all participants could access.

### Conclusions: Reflect on what's been learnt

Ask the two simple questions below, and give partipants some simple way of choosing from the multiple choice answers (I created several yellow stars that participants could pick up and move into the relevant space - see image below). This gives you an idea of how well the learning hour has gone, and also gives participants a way of reinforcing in their own heads the value of the workshop.

![img.png](/assets/images/how_confident_lift_up_conditional.png){: width="600"}