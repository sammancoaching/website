---
theme: documentation
title: Simon Brown's 4C model - Container diagram
kata: instavoiced
difficulty: 2
---

# Simon Brown's 4C model - Container diagrams

This learning hour follows on from the previous one on this topic and goes into a little more detail about [The C4 model for visualising software architecture](https://c4model.com/)

## Learning Goals
- sketch a Container diagram
- distinguish between important elements to show in a Container diagram and details to exclude
- apply rules that make diagrams easier to read and understand

## Session Outline

* 10 min connect: 4C recap 
* 10 min concept: Context and Container diagrams
* 20 min concrete: draw a container diagram 
* 15 min conclusions: compare Context and Container diagrams

### Connect: 4C recap
The list below comprises descriptions of elements of the 4C model. Some statements describe a Diagram, some describe an Abstraction. Fill in the blanks with the following words:

- Component
- System Context
- Person
- Software System
- Container
- Code

1. A ____________ represents one of the human users of your software system (e.g. actors, roles, personas, etc).
1. A ____________ diagram can be used to zoom into an individual component, showing how that component is implemented.
1. A ____________ is a grouping of related functionality encapsulated behind a well-defined interface. If you're using a language like Java or C#, the simplest way to think of it is as a collection of implementation classes behind an interface.
1. A ____________ is the highest level of abstraction and describes something that delivers value to its users, whether they are human or not.
1. A ____________ diagram zooms into the software system in scope, showing the high-level technical building blocks.
1. A ____________ diagram provides a starting point, showing how the software system in scope fits into the world around it.
1. A ____________ diagram zooms into an individual container, showing the components inside it.
1. A ____________ represents an application or a data store. It is not the same as in Docker. It is something that needs to be running in order for the overall software system to work.

### Context and Container diagrams

Go through the example diagrams on [The C4 model](https://c4model.com/) website. Explain in particular the differences between Context and Container diagrams. Provide a context diagram for the Instavoiced exercise. Either one you designed yourself or one created in the previous session.

Go through some advice on notation:
- Put titles on diagrams. What type of diagram is it? What is the scope? eg “System Context for Instavoiced".
- Put the most important things in the middle.
- Every element has a name, type and description.
- Lines should have an arrow in only one direction, with a label explaining the purpose: summarize the intent of the relationship. Avoid saying ‘Thing A Uses Thing B’, rather say _how_ A uses B.
- Have a legend or key.
- Make sure diagram still makes sense if you take away all colour, shape and size. Those things are to make it aesthetically pleasing and easier to read, not convey necessary information.
- Prefer to use full sentences not short titles. A long-term document needs some detail.
- Try not to use acronyms unless you’re sure your audience understands them.

### Concrete: draw a container diagram
Take the example context diagram or the one your pair produced last time. Create a Container diagram that 'zooms in' on the Instavoiced system. If you have time, pick one of the containers and create a component diagram for it.

### Conclusions
Join with another pair to compare the diagrams you have come up with. Did you make the same decisions about what details to include? Go through the advice on notation - did you follow it? If you have time, update your diagram.

### Homework
Go and read more about the C4 model [The C4 model](https://c4model.com/). Create Context and Container diagrams for the software you work on.



