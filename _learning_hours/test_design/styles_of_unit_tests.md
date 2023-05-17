---
theme: test_design
title: Styles of Unit Tests
kata: audit
difficulty: 3
author: ythirion
---

# Styles of Unit Tests

## Learning Objectives
* Understand the 3 types of Unit Tests
* Have in mind the drawbacks of the different styles and how/why to migrate from one to another

## Session Outline

* 5 min connect: Audit review
* 10 min concept: Styles and costs
* 40 min concrete: Refactor to output-based testing
* 5 min conclusions: Test readability

## Connect - Audit review
Open the `AuditManager_Should` test class from the [Audit kata](/kata_descriptions/audit.html).

- What can be improved in the tests? Why?
- What make this test hard to understand / maintain?
- What do you think about the naming?

## Concepts - Styles and costs
![State-Based Style](/assets/images/styles-of-unit-tests/state-based.png)

#### State-Based Example
```csharp
[Fact]
public void It_Should_Add_Given_Product_To_The_Order()
{
    var product = new Product("Free Guy");
    var sut = new Order();

    sut.Add(product);

    sut.Products.Should()
        .HaveCount(1)
        .And.Satisfy(item => item.Equals(product));
}
```

![Output-Based Style](/assets/images/styles-of-unit-tests/output-based.png)

#### Output-Based Example
```csharp
[Fact]
public void Discount_Of_2_Products_Should_Be_2_Percent()
{
    var product1 = new Product("Kaamelott");
    var product2 = new Product("Free Guy");

    var discount = PriceEngine.CalculateDiscount(product1, product2);
    
    discount.Should().Be(0.02);
}
```

![Communication-Based Style](/assets/images/styles-of-unit-tests/communication-based.png)

Refactorings are harder with `Communication-based` : if you change the interaction you need to change the tests as well.

#### Communication-Based Example
```csharp
[Fact]
public void Greet_A_User_Should_Send_An_Email_To_It()
{
    const string email = "john.doe@email.com";
    var emailGatewayMock = new Mock<IEmailGateway>();
    var sut = new Controller(emailGatewayMock.Object);
    
    sut.GreetUser(email);

    emailGatewayMock.Verify(e => e.SendGreetingsEmail(email), Times.Once);
}
```

The images above are part of the `Unit Testing Principles, Practices and Patterns` book infographic available [here](https://yoan-thirion.gitbook.io/knowledge-base/xtrem-reading/my-book-infographics).

## Concrete Practice - Refactor to output-based testing
Explain the purpose of the [Audit](/kata_descriptions/audit.html) kata. 

Ask them to:
* Refactor the tests and production code to `Output based` tests
    * Instead of hiding side effects behind an interface and injecting that interface into AuditManager, we can move those side effects out of the class entirely :
      * `AuditManager` is then only responsible for making a decision about what to do with the files
      * A new class, `Persister` acts on that decision and applies updates to the filesystem

![Functional code](/assets/images/audit-functional.png)

A `step-by-step` guide is available [here](https://github.com/katalogs/audit-kata/blob/main/step-by-step.md).

## Conclusion
Compare the first version of the `unit test` with the new one.

Which one is the easiest to read and why ?

### Resources
Concepts are coming from Vladimir Khorikov's book : [Unit Testing Principles, Practices and Patterns](https://www.manning.com/books/unit-testing).