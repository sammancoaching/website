---
name: describe-kata
description: Write a kata (coding exercise) description for the website's _kata_descriptions/ collection. Use when adding a new kata, or reformatting an existing problem statement to match the site's conventions. Triggers on "write a kata description", "add a kata", "document this exercise".
---

# Write a Kata Description

Produce a consistent, clear kata description for `_kata_descriptions/<kata_name>.md`. Keep language simple, direct, present-tense, and example-driven.

## Structure

A kata description has these sections, in order:

1. **YAML front matter** — open and close with `---`. Required keys:
   - `title`: human-friendly name.
   - `kata_name`: machine identifier in `snake_case` (match the filename).
2. **Main title** — a Markdown heading with the kata's name.
3. **Problem description** — state the problem and any scenario. Include sample data, inputs, or outputs in code blocks where helpful.
4. **Requirements / Rules** — bullet points. For multi-part katas use `## Part 1`, `## Part 2`, etc.
5. **Examples** — concrete input/output pairs as code or tables.
6. **Additional Features / Follow-ups** (optional) — stretch goals.
7. **Acknowledgements** — credit the original author/source with links if applicable.

## Style

- Clarity and brevity; avoid jargon.
- Neutral, instructive, encouraging tone.
- Present tense, imperative where giving instructions.
- Prefer concrete examples over abstract explanation.
- Save to `_kata_descriptions/<kata_name>.md` with a lowercase filename matching `kata_name`.

## Ask the human if unclear

- Intended title and `snake_case` name?
- Core problem statement / scenario?
- Precise requirements or rules?
- Sample inputs and expected outputs?
- Edge cases or special rules to highlight?
- Extensions / follow-up challenges?
- Who to credit, and any external links?

## Template

```markdown
---
title: Example Kata
kata_name: example_kata
---

Example Kata
============

Describe the scenario and problem here.

## Requirements

- List each requirement as a bullet point.
- Be specific and clear.

## Example

```
Input: [example input]
Output: [expected output]
```

## Additional Features

- Optional: stretch goals or follow-up challenges.

### Acknowledgements
This kata was inspired by [Author Name](link).
```
