---
theme: git
title: Git Interactive Rebase
kata: 
difficulty: 2
author: xaviametller
---

# Git interactive rebase
Git is a powerful source control system that, among other options, allows us to redefine the history of what happened. This learning hour is meant to understand what are some possibilities and put them in practice.

## Learning goals
* Understand Git history can be rewritten
* Merge, reorder and rewrite commits (and split)

## Session outline
* 5 min connect: what are some useful Git commands or alias you often use?
  * (alternative connect exercise: "How does git work?" or "What constitutes a commit?")
* 5 min concept: How does Git use commits
* 10 min demo: Interactive rebase
* 25 min do: Refactor the commits of a branch
* 5 min reflect: Explain how interactive rebase works

## Useful Git commands
Ask people to share one Git command or alias they find specially useful. Doesn't need to be a command line action, it can be done from any Git client.

## How does Git use commits
Git is a source control system that works with commits. We can consider a commit as if it were a diff file and a pointer to the parent commit. With this definition, when we checkout a commit (usually the latest in a branch), what we see is the result of applying a bunch of diffs in the order defined by the parenting relationship.

Luckily for us, Git provides us with the capability of changing the order of the commits, the contents, the messages and other things. 

Be careful though, this practice can mess up if you rewrite history that has already been shared with other people (remote branches)

## Interactive rebase:
* Open a terminal and run git rebase -i Head~3 with the current repo. 
* Go through the list of options the interactive rebase offers you (pick, reword, edit, ...) and explain each one.
* Toy around with some commits by using the options provided.
* Show you can rebase onto a specific commit instead of from the HEAD.

## Refactor the commits of a branch:
Using your preferred Git client, checkout the repo [Tennis Refactoring Git Kata](https://github.com/xrecoba/Tennis-Refactoring-Git-Kata) and try to apply all these improvements:
* There's a commit message which seems really verbose and opinionated, change the message so the content is more clear and objective.
* There’s a commit which deletes all the tennis Katas in Emily’s repo except for the Javascript-Jest one. This commit is one of the last ones, but it would make more sense before the whole refactoring, move that commit to the beginning.
* There's a commit that’s fixing an error introduced in another one. Remove both commits as there’s no point in keeping them.
* There are some commits which are very small and fine grained. All of a sudden you feel the urge merge them together in one single commit with a higher level of abstraction.
Compact some small commits into a bigger one
* A change related to evenResult function slipped into the commit "Refactor late game result to use array".
Split the commit in two and move the evenResult change into the previous commit "Rewrite even result to loookup"

## Explain how interactive rebase works
Pair with someone from another couple/group, and write in a post-it a summary of how does Git interactive rebase work.

Credits: LH created while working as Tech Coach for [SunwebGroup](https://www.sunwebgroup.com/) on top of the [Kata](https://github.com/xrecoba/Tennis-Refactoring-Git-Kata) created while working for [Volcànic](https://volcanicinternet.com/en/).
