---
theme: test_doubles
title: Contract Tests for repositories
name: contract_tests_for_repositories
difficulty: 2
author: hdeweirdt
tags: test_doubles test_design
---

# Contract tests for repositories

When writing tests using repositories, one might use mocks or fakes instead of the real implementation.
They both carry the risk of behaving differently from the 'actual' code.
Contract tests are introduced as a why to reduce behavioral drift between fake and real implementations.

Accompanying Miro slides: found [here](https://miro.com/app/board/uXjVH9Vcgcg=/?share_link_id=314485831274)

## Learning Objectives

* Understand the value of using Contract Tests to ensure fake and production implementations don't drift.
* Write an abstract contract test for a repository and implement it for both fake and production implementations.

## Session Outline

* 5 min connect: code review of two tests using badly set-up mocks.
* 10 min concept: Sample code for repository interface and fake implementation
* 30 min do: Refactoring kata: from separate tests for fake and production code to a contract test
* 5 min reflect: describing the concept of a contract test

### Connect - code review

Show two simple tests that both verify behavior of a class using a certain Repository.
The tests currently use a mock of that Repository, however each test mocks the behavior of a single function differently.
One `findThing()` might return `null` when nothing is found, another might throw an exception for example.
There is nothing that keeps us from mocking the real behavior incorrectly!

### Connect - introduction of a Contract Test

Show a fake implementation of the Repository, and introduce doubt on how we'll ensure it has the same behavior as the production code.
Again there is nothing that keeps us from having the fake behave differently!

Then show an interface defining a test for the behavior of the Repository, and how the tests for the fake and real implementation should implement that
interface.

### Do: refactor existing repository tests

The [accompanying kata](https://github.com/hdeweirdt/contract-test-kata) has an example implementation of a `UserRepositoryContractTest`, implemented by an `InMemoryUserRepository` and a `SqlUserRepository`.
The task is now to take the `InMemoryCarRepositoryTest` and `SqlCarRepositoryTest` and rework them towards extending a `CarRepositoryContractTest` and only
having to provide an implementation of the `getRepository` function.

### Reflect: concept

If you had to describe the main concept of a contract test to a colleague, what would you say?
