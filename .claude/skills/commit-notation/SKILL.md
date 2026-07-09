---
name: commit-notation
description: Write commit messages using Arlo's Commit Notation (ACN) — a one-or-two-character prefix encoding the change's risk and type. Use when committing in this repo, or when asked to classify or rewrite a commit message in ACN. Triggers on "commit notation", "Arlo's notation", "ACN", "what prefix should this commit have".
---

# Arlo's Commit Notation (ACN)

Every commit subject starts with a **risk marker** and a **type letter**, then a space, then a
present-tense description:

```
[risk][type] description
```

Examples: `. e Add commit-notation skill`, `! F use ical to get training dates`, `. r Extract method`.

Source: <https://github.com/RefactoringCombos/ArlosCommitNotation>

## Type letters

| Letter | Type | Meaning |
|--------|------|---------|
| `F` / `f` | Feature | Change or extend one aspect of program behavior without altering others. |
| `B` / `b` | Bugfix | Repair one existing, undesirable behavior without altering any others. |
| `R` / `r` | Refactoring | Change implementation **without** changing program behavior. |
| `D` / `d` | Documentation | Communicates to team members; no impact on program behavior. |
| `e` | Environment *(repo extension)* | Build, CI, config, dev-tooling and agent tooling (`.claude/skills`, `.windsurf`, `.gitignore`, workflows). No product behavior change. |

**Case:** uppercase = the change is **user-visible / behavior-changing** (belongs in a changelog);
lowercase = **internal only**, no behavior change. So a feature users will notice is `F`; a
developer-only feature is `f`. Refactoring and docs are normally lowercase (`r`, `d`).

## Risk markers

| Marker | Level | Meaning |
|--------|-------|---------|
| `.` | Safe | Addresses all known **and unknown** risks. Provable refactoring, pure additions, test-only or tooling changes. |
| `^` | Validated | Addresses all **known** risks; intended change is verified. **This repo writes this as `-`.** |
| `!` | Risky | Some known risks remain unverified; only the intended change is checked. |
| `@` | Broken | No attestation — may not even compile. Avoid except on private WIP. |

> **House style:** this repo uses **`-` instead of `^`** for *validated*, and uses **`e`** for
> environment/tooling. Match the surrounding history: `git log --oneline` to see recent prefixes.

## Rules of thumb

- **One behavior change per `F`/`B`.** More than one behavior change drops you to `@`.
- **`^`/`-` for `F`/`B` only if ≤ 8 lines changed** (tests included) and the change is validated.
- **`. r`** requires a *provable* refactoring (tool-assisted) or a refactoring confined to test code.
- **`. F`/`. f`** requires the feature to be developer-only, or to meet all validated-feature criteria.
- Pure additions of files that cannot break existing behavior (new tooling, new docs) are `.`.

## How to classify a commit

1. **Type:** Does it change product behavior users care about? → `F`/`B`. Behavior-preserving code
   change? → `r`. Team-facing text only? → `d`. Build/CI/config/agent tooling? → `e`.
2. **Case:** user-visible → uppercase; internal-only → lowercase.
3. **Risk:** Provably safe / pure addition / tool-assisted? → `.`. Validated but not proven (and
   small)? → `-` (this repo) / `^`. Intended change works but risks unverified? → `!`.
4. Prepend `[risk][type] ` to a concise, present-tense subject. Check `git log` for local style.
