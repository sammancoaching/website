---
title: Audit everything
kata_name: audit
---

## Audit everything
The `Audit` project is an audit system that keeps track of all visitors in an organization.
It : 
* uses flat text files as underlying storage with the structure shown below
* system appends the visitor’s name and the time of their visit to the end of the most recent file
    - When the maximum number of entries per file is reached: a new file with an `incremented index` is created

![Audit file example]({% link assets/images/audit-example.png %})

This is actually a refactoring kata. 
The starting position is available on Github [here](https://github.com/katalogs/audit-kata).

## Acknowledgement
This kata has been described by [Vladimir Khorikov](https://www.linkedin.com/in/vladimir-khorikov-bb482653/) in his great book [Unit Testing Principles, Practices, and Patterns](https://www.manning.com/books/unit-testing).