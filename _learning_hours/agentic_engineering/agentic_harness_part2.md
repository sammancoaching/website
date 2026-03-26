---
theme: agentic_engineering
name: harness_for_agentic_autonomy
title: Designing a Harness for Agentic Autonomy (Part 2)
kata: WarehouseDeskApp
difficulty: 1
author: martinsson
via: emilybache
tags:  agentic tdd
---

# Designing a Harness for Agentic Autonomy (Part 2)

Starting from a minimal harness and code with a 'long method' smell, we learn how to improve our harness. This learning hour was originally designed as a longer workshop, so it is split into several parts. See also [Agentic Harness Part 1]({% link _learning_hours/agentic_engineering/agentic_harness_part1.md %}).

## Learning Goals

* Describe the benefits of moving instructions from an agent conversation into a harness file.
* Use a knowledge document to prompt the coding agent to address a 'long method' code smell.

## Session Outline

* 5 min connect: Discuss: What is the difference between a Prompt and a Harness?
* 5 min concept: What is a knowledge document and how is it different from AGENTS.md
* 40 min concrete practice: Build a new feature with and without a Harness
* 5 min conclusion: Explain the main idea

### Connect
Ask: What is the difference between a Prompt and a Harness? (This was one of the learning goals for part 1).

### Concept
Ensure everyone is clear on the terms we introduced in part 1 (Prompt, Context, Harness), and go on to describe [Knowledge Documents](https://lexler.github.io/augmented-coding-patterns/patterns/knowledge-document/). Note the main difference - that these are only loaded into the context when we are asking the agent to do a task that needs this knowledge. The piece of harness we used last time - AGENTS.md - is always loaded.

#### Step 1: Improve the design through prompting
Start from the code you had at the end of part 1. There should be a new feature implemented, and there should be some unit tests. The design should be largely unchanged from before, still with a [Long Method]({% link _code_smells/long_function.md %}) code smell. Make sure the code is committed so you can revert to this point.

You would like it to refactor the design. Give a simple prompt like:

        Improve the design, keeping the tests the same.

Review the design changes. Prompt it again to correct anything it did which doesn't align with your preferences. Keep prompting in the same conversation until you are happy with the code. 

#### Step 2: Create a "Knowledge Document"
Give this prompt in the same conversation as before:

        Extract the design principles we have used into a document "design-principles.md"

Take a look at what it comes up with and keep prompting until the document looks good. (Don't write any of the document by hand, use prompts).

#### Step 3: Use your "Knowledge Document"
Revert your code changes back to the poorly designed code you had at the start, but keep the new design-principles document. Give this single prompt:

    Use "design-principles.md" to improve the design, keeping the tests the same.

Review the code changes. If it still doesn't meet your expectations, continue the conversation until it looks good. When you are happy, ask it to update the knowledge document. Revert the code and repeat until it can do a good enough design in one shot.

#### Step 4: Additional Knowlege Documents
Review the contents of "AGENTS.md". Should anything here also be moved into a separate knowledge document? Discuss and experiment.

### Conclusions
Ask people to [explain the main idea]({% link _activities/conclusions/explain_main_idea.md %}) of a Knowledge Document.
