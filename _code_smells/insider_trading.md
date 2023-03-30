---
layout: code_smell
title: Insider Trading
source: Martin Fowler
---

# Insider Trading
Classes or modules that know too much about the inside details of one another. They may pass private data between them. It's a sign they are too tightly coupled. Often this happens between a subclass and its parent classes - the subclass has access to too many details that should be private to the parent.