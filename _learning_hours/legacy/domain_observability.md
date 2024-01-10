---
theme: refactoring
title: Domain Oriented Obervability on Reservation Kata
name: domain_oriented_observability
kata: reservation
difficulty: 2
author: pierrickblons
---

# Domain Oriented Obervability

It's useful to have logging and metrics in our code to understand how it's behaving in production. But sometimes those little calls to loggers or metrics class start to spread all across the code base. It's quite common to see methods with more code dedicated to observability than code actually solving the problem.

In this learning hour we will see how to improve the understandability of code that requires observability.

### Learning Goals

- Improving the readability of the code
- Refactoring techniques to extract code into methods

### Session Outline

* 5 min connect: Discussion around logging and metrics
* 15 min concept: Introduce domain oriented observability refactoring
* 30 min concrete: Do Reservation Kata in pairs
* 10 min conclusions: Discussion about this technique in your current code base

### Connect: What is observability?
Based on the [Pick only the correct items](https://sammancoaching.org/activities/connect/pick_the_correct_items_on_the_list.html) activity 

Share to the group the some propositions to answer the question "What is observability?".

Example:
1. Measure internal state of a system
2. Read data from database
3. Gives feedback on application usage
4. Monitor application performance
5. Alerts team when a service is down
6. Displays data in reports

### Concept: Domain probe
Explain [Domain probe](https://martinfowler.com/articles/domain-oriented-observability.html#DomainProbe) :
* High-level instrumentation API that is oriented around domain semantics.
* Encapsulates low-level instrumentation plumbing required for observability.

Demo the refactoring starting from the article example
```java
class ShoppingCart {
  applyDiscountCode(discountCode){
    this.logger.log(`attempting to apply discount code: ${discountCode}`);

    let discount; 
    try {
      discount = this.discountService.lookupDiscount(discountCode);
    } catch (error) {
      this.logger.error('discount lookup failed',error);
      this.metrics.increment(
        'discount-lookup-failure',
        {code:discountCode});
      return 0;
    }
    this.metrics.increment(
      'discount-lookup-success',
      {code:discountCode});

    const amountDiscounted = discount.applyToCart(this);

    this.logger.log(`Discount applied, of amount: ${amountDiscounted}`);
    this.analytics.track('Discount Code Applied',{
      code:discount.code, 
      discount:discount.amount, 
      amountDiscounted:amountDiscounted
    });

    return amountDiscounted;
  }
}
```

to this final implementation

```java
class ShoppingCart {
  applyDiscountCode(discountCode){
    this.instrumentation.applyingDiscountCode(discountCode);

    let discount; 
    try {
      discount = this.discountService.lookupDiscount(discountCode);
    } catch (error) {
      this.instrumentation.discountCodeLookupFailed(discountCode,error);
      return 0;
    }
    this.instrumentation.discountCodeLookupSucceeded(discountCode);

    const amountDiscounted = discount.applyToCart(this);
    this.instrumention.discountApplied(discount,amountDiscounted);
    return amountDiscounted;
  }
}
```

### Concrete: Reservation Kata
Experiment in pair the [Reservation Kata refactoring]() to refactor the code by introducing a Domain Probe in the ReservationService.

### Conclusions:
Can you think of code you've written where you could have used a Domain Probe ? 
Discuss in pairs for 5 minutes.
