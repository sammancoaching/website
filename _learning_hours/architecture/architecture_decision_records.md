---
theme: architecture
title: Architecture Decision Records
kata: instavoiced
difficulty: 4
author: emilybache
affiliation: ProAgile
---

# Architecture Decision Records

This is a way for architects to communicate their decisions. Most developers will at some point need to follow guidance from architects and might be shown Architectur Decision Records so it could be good to know what they are.

## Session outline

* 5 min connect: what is an architecture decision
* 10 min concept: Architecture Decision Records
* 15 min concrete: Active Review ADRs
* 20 min concrete: write an ADR
* 5 min conclusions: could you use this?

### Connect: What is an architecture decision
[Pick only the correct items]({% link _activities/connect/pick_the_correct_items_on_the_list.md %})

Which of these is an architecture decision?

* No deploys on Fridays
* Use microservices communicating via a message bus
* Use tabs not spaces
* Use a graph database for storing customer details and connections
* Use whiteboard coding exercises in job interviews
* Use feature flags instead of feature branches
* Work remotely apart from on Tuesdays when we will all meet at the office
* The web tier should not depend directly on the database schema
* Interfaces should be named with an 'I' prefix eg "IMessage" and "ISensor"

Some of them are perhaps grey areas? Try not to get into a big discussion though. Hopefully this will lead you into the next section.

### Concept: Architecture Decision Record
Explain what you think an Architecture Decision is. For example Neal Ford and Mark Richards say "a good architecture decision is one that helps guide development teams in making the right technical choices" in their book "Fundamentals of Software Architecture". Grady Booch says "Architecture represents the significant design decisions that shape a system, where significant is measured by cost of change."

The source for Architecture Decision Records is  [Michael Nygard's blog post](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) - go through it.

### Active Review 
Find some publically available ADRs that are good examples of what you are looking for. For example [The winning entry in O'Reilly's architectural katas competition in 2022](https://github.com/tekiegirl/Archangels/blob/main/4.ADRs/README.md). You want people to read them actively, so prepare a version of them where you have deliberately introduced errors - eg you swapped some of the sections and titles. Ask them to read them through and tell you the errors.

### Write your own ADR
Make an architecture deicion for the [Instavoiced]({% link _kata_descriptions/instavoiced.md %}) system. For example you could decide:

* What data storage option to use for archiving invoice pdfs
* What web framework to use for suppliers to upload their pdf invoices
* Where to host the system - on-premises or in the cloud? Which cloud?
* What architectural style should the system use? eg monolith, microservices
* What programming language or tool should generate xml? How should we store it?
* How should we ensure quick recovery if the production environment goes wrong? Canary deploys? Blue/Green deployments?

Work in pairs. Pick an area, make a decision, and write it up in the form of an Architecture Decision Record. 

Join two pairs together to review one another's ADRs. Suggest improvements to make them even better.

### Conclusions
[When should you use this](/activities/conclusions/when_to_use_this.html)? Looking at your own team's situation, are there any decisions you should write up as ADRs?