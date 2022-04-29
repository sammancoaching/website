---
theme: architecture
title: User Documentation and code snippets
kata: recently_used_list
difficulty: 3
author: emilybache
affiliation: ProAgile
---

# User Documentation and code snippets

Unit tests form part of the documentation for your code. They should probably not be the entirety of the documentation. In this learning hour we look at using code snippets in documentation.

## Learning Goals
- describe some additional elements you expect in user documentation over unit tests.
- operate a pre-existing script to generate html documentation from markdown and code snippets.
- prepare some user documentation based on some unit tests.

## Session Outline

* 10 min connect: documentation attitudes
* 10 min concept: Tutorials and How-to documentation in practice
* 20 min concrete: Write some how-to guides
* 15 min conclusions: Swap documents and give feedback


### Connect: Documentation attitudes
Put a mark by the statements you agree with:

- I use documentation much more often than I write it.
- All the documentation can be generated from the source code if you write good comments, tests and name things well.
- It’s best to hire a technical writer to do the documentation, programmers can’t write it very well. 
- Documentation that is out-of-date or wrong is the normal state for much of the software I work on. 
- Documentation should include code snippets as examples.
- You need less documentation if you have good code comments and unit tests. 
- Documentation should be laid out nicely with pretty fonts and css or else people will not use it. 
- I enjoy writing and updating documentation.


### Concept - Tutorials and How-to documentation in practice
In the repo [Recently-Used-List-Docs](https://github.com/emilybache/Recently-Used-List-Docs) there is an example project with user documentation. It is a solution to the [RecentlyUsedList](/kata_descriptions/recently_used_list.html) kata in C++.
The documentation uses [Markdown Snippets](https://github.com/SimonCropp/MarkdownSnippets) and [Jekyll](https://jekyllrb.com/). The idea is to write documentation in markdown that can be rendered as html. In the markdown we can include snippets of the unit test code. 

Show how it works. Modify one of the snippets and some of the markdown and show the process to update the documentation. Relate this learning hour to the one on [the Divio Documentation system](divio_system.html) for why the documentation is organized as it is.

### Concrete
In the [Recently-Used-List-Docs](https://github.com/emilybache/Recently-Used-List-Docs) project the how-to page is largely empty, with only some headings. The exercise is to fill in these blanks and then to add more documentation as you see fit. If you have time, implement a the new feature and write the associated documentation. Feature description:

The RecentlyUsedList class should not only reject empty strings, but also any strings on a blocklist. The blocklist is a list of strings that is provided on construction and by default is empty. The blocklist can be updated at any time by users of the RecentlyUsedList. When that happens any items held in the RecentlyUsedList that are on the updated blocklist should be removed. All the other items should be preserved in the original order.

### Conclusions
If you've been working in small groups or pairs, compare the documentation each group has come up with. Discuss these question:

- Do you think it is worth creating additional user documentation on top of code comments, unit tests and great naming?
- What text did you add to turn a unit test into a how-to documentation? Was it anything that wasn't present in the code already?
- Was this more fun than the kind of documentation you've written previously?
- Would this kind of documentation be more likely to stay up-to-date than the documentation you've written previously?