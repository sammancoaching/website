---
title: Fractions - 分数
kata_name: fractions
---

分数
==========

编写一个实现分数加法的程序。

1/2 + 3/4

应该得到。

1 1/4

限制条件
------------

分数是一个[值对象](https://martinfowler.com/bliki/ValueObject.html)，也就是说，一旦创建，它就不能被更新或改变。 "add" 操作应该返回一个新的分数，代表 2 个分数的和。

当你把两个分数相加时，结果应该用最简化的形式表示。
例如，你应该给出:

3/5

而不是

6/10

### 鸣谢
我从 J.B.Rainsberger 那里得到了这个Kata，但我对它做了些许改动。
