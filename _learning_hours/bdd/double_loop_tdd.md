---
theme: bdd
title: 双环TDD
kata: monty_hall
difficulty: 2
author: emilybache
---


# 双环TDD

当你做双循环TDD时，你在几分钟的节奏上进行内循环，在几小时到几天的节奏上进行外循环。外循环的测试是从系统用户的角度来写的。我写了[一篇文章](http://coding-is-like-cooking.info/2013/04/outside-in-development-with-double-loop-tdd/)，解释了更多细节。

许多组织都有不是单元测试的自动化测试，但他们对它们的称呼有很大的不同。本次会议的第一部分，我们要发现这个组织对它们的称呼，并研究它们是否适合在双环 TDD 中使用。

## 会议大纲

* 5分钟的连接：测试种类的名称
* 5分钟的概念：双循环
* 35分钟做：创建一些指导性测试
* 10分钟反思：比较你以前知道的和现在知道的

### 连接：你怎么称呼那些不是单元测试的测试？
如果你在工作中实际使用了这些术语，并且它们指的是自动化但不是单元测试的测试，请在任何一个术语旁打上标记：

- 客户测试（Customer Test）
- 指导性测试（Guiding Test）
- 验收测试（Acceptance Test）
- 组件测试（Component Test）
- 集成测试（Integration Test）
- 程序员测试（Programmer Test）
- 微测试（Microtest）
- Gherkin 测试
- 微服务测试（Microservice Test）
- (也可插入商业工具的名称)

不要担心他们不熟悉和不使用的术语。通过他们所使用的术语，试着找出它们是否适合作为双环 TDD 的外环测试。要做到这一点，程序员需要能够在他们的开发环境中运行它们。他们还需要使用客户或用户会理解的词语。

### 概念：双环TDD
展示这张图片！[双循环TDD](/assets/images/double_loop.jpg)

解释一下这个概念--TDD中的单元测试周期以分钟为单位进行循环。外循环的速度更慢--从第一次编写测试到测试通过，需要几天甚至一两周的时间。这是一个他们可能已经知道的 "行为驱动开发（BDD）"，或 "实例化需求（SBE）" 或 "验收测试驱动开发（ATDD）" 的想法。

外环测试是从用户或客户的角度来写的。它应该使用他们能理解的词语。可以用[Cucumber](https://cucumber.io/)、[Fitnesse](http://docs.fitnesse.org/FrontPage)或[Approvals](https://approvaltests.com/)等工具来写，也可以用普通的单元测试框架来写。

### 做：Monty Hall或类似的
为 "Kata" 描绘一个指导性的测试。例如 [Monty Hall](/kata_descriptions/monty_hall.html) 或 [Lift](/kata_descriptions/lift.html) 或 [Theater](https://github.com/emilybache/Theater-Kata) 或 [Train Reservation](https://github.com/emilybache/KataTrainReservation)。

分成两组，让人们在一张纸上制作草图。大约5-10分钟后，让他们向小组其他成员介绍。给他们一些反馈。让他们再花5分钟左右来完善他们的草图。再次分享这些草图并确定理想的特征。理想的情况是，让小组同意一个可以在未来的会议中作为指导性测试使用的草图。

如果他们有时间，可以重复另一个 "Kata"。

### 总结
对比一下你在本次会议之前对指导性测试（或你在组织中对其的称呼）的认识和假设，以及你现在所知道的。写一段话来总结你的比较。
