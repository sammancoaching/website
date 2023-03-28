---
theme: architecture
title: Modelling vs Diagramming
kata: instavoiced
difficulty: 2
author: emilybache
affiliation: ProAgile
---

# Modelling vs Diagramming

Before we get into designing container diagrams we should talk about the difference between a model and a diagram.

## Session outline

* 5 min connect: tools you know
* 10 min concept: Modelling
* 5 min concept: intro to Structurizr
* 25 min concrete: make a model for Instavoiced
* 10 min conclusions: note down facts about modelling

### Connect: Diagramming and modelling tools you know
What do you use to make architecture diagrams? Add notes with names of tools to a shared whiteboard. Put a plus marker by any which you have used.

### Concept: Diagramming vs Modelling
There used to be an article on the c4model site about this, you can find it on the [wayback machine](https://web.archive.org/web/20220520164641/https://c4model.com/#Modelling). Similar material by the same author is outlined in an [article about Structurizr](https://structurizr.com/help/modelling). 

The basic idea is that you can generate more than one diagram from the same model. A model is a non-visual artifact that defines elements and the relationships between them. When you use it to produce a diagram, you can choose which elements and relationships to show, and how to represent them visually. A diagram is a picture that shows elements and their relationships - usually some kind of boxes and lines. A second diagram that displays the same elements and relationships but does not share an underlying model may easily become inconsistent with the original diagram.

### Intro to Structurizr
[Structurizr](https://structurizr.com/) is an example of a modelling tool. I found I could get a free account to try it out. This was sufficient to begin to understand what a modelling tool is and how it differs from a diagramming tool. Give people a brief demo of how to use the tool to create a Context diagram and where to find the documentation.

There is a [starting position](https://github.com/emilybache/Instavoiced-Architecture-Kata/blob/main/instavoiced_starting_point.structurizr) in the DSL with some styling set up, which you could give them.

### Concrete: Model Instavoiced
Ask them to create a model that will produce the Context diagram which they came up with in the previous session [Simon Brown's 4C model - Intro]({% link _learning_hours/architecture/simon_brown_4c_context.md %}).

If they have time, they could go on to model a Container diagram too.

### Conclusions
Compare the diagrams produced by the different groups. If you like, show them a sample solution from the [Instavoiced materials repo](https://github.com/emilybache/Instavoiced-Architecture-Kata)

Have them note down any facts they want to remember about architecture modelling.





