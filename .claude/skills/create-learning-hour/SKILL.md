---
name: create-learning-hour
description: Author a Learning Hour (a time-boxed Connect/Concept/Concrete/Conclusions workshop using Sharon Bowman's 4C format) for the website's _learning_hours/ collection. Use when creating a new learning hour, or restructuring workshop notes into the site format. Triggers on "create a learning hour", "add a learning hour", "write a workshop session".
---

# Create a Learning Hour

A Learning Hour is a time-boxed, interactive workshop following the 4C format
(Connect, Concept, Concrete, Conclusions) from Sharon Bowman's *Training from the Back of the Room*. Gather the content, structure the document,
and place it under `_learning_hours/<theme>/`.

## Steps

1. **Collect metadata**
   - Theme (the folder under `_learning_hours/`, e.g. `ensemble`, `bdd`, `legacy`).
   - Title (Title-case).
   - Kata (exercise name or link).
   - Difficulty (1–5).
   - Author & affiliation.
   - Languages and tags (optional).

2. **Interview the writer**
   - Motivation / intro sentence.
   - Learning objectives / goals.
   - Timeboxes for each phase (minutes).
   - **Connect** — icebreaker or context activity.
   - **Concept** — theory or demo (sometimes labeled "Demo").
   - **Concrete** — hands-on tasks (sometimes labeled "Do").
   - **Conclusions** — wrap-up (sometimes labeled "Reflect").
   - Any prerequisites (`## Requirements`) or acknowledgements.

3. **Write the sections** using the template below.
   - Link internal exercises/activities with Jekyll's `link` tag, e.g.
     `{% link exercises/warm_up_questions/go_syntax.md %}`.
   - Use standard URLs for external links.
   - Timings in minutes; bullet lists; imperative voice; consistent heading levels.

4. **Review style & links**
   - Check synonym consistency (Goals/Objectives, Outline/Session Outline,
     Concept/Demo, Concrete/Do, Conclusions/Reflect).
   - Validate every link and the front matter.

5. **Place the file**
   - Save under `_learning_hours/<theme>/` with a lowercase, underscore filename.

6. **Build & verify**
   - Run the site locally (`./build_and_run`) and preview in the browser.
   - Only commit/push when Ivett asks.

## Template

```md
---
theme: <theme>
title: <Title>
kata: <kata>
difficulty: <n>
author: <you>
affiliation: <org>
languages: <opt>
tags: <list>
---

# <Title>
<One–two sentence intro>

## Learning Objectives
- …

## Session Outline
* <min> connect: …
* <min> concept: …
* <min> concrete: …
* <min> conclusions: …

### Connect: <short label>
<Instructions & link>

### Concept: <short label>
<Theory / demo steps>

### Concrete: <short label>
<Hands-on exercise instructions>

### Conclusions: <short label>
<Wrap-up questions / links>
```
