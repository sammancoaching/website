---
theme: small_steps
title: Outside-in TDD
kata: todo
difficulty: 5
author: emilybache
tags:  small_steps bdd
---

# Outside-in TDD

This learning hour is still being worked on.

When you’re doing TDD and you have an outer-loop "Guiding Test" defined, you can choose to work outside-in on the inner loop TDD. Emily wrote [an article](http://coding-is-like-cooking.info/2013/04/outside-in-development-with-double-loop-tdd/) that explains more details.

Many programmers over-use mocks and in this learning hour we look at how the inventors of mocks intended them to be used.

## Session Outline
 
* 5 min connect: Mocks as intended?
* 5 min concept: Design downstream collaborators using mocks/test doubles
* 35 min do: Implement design outside
* 5 min reflect: How is this different from what you do today?

### Connect:
That’s what we  … designed JMock to do …
“Tell, Don’t Ask” object-oriented design.”
— Nat Pryce, in an email to a discussion forum.

We want Sociable tests, but use Solitary tests along the way.
https://martinfowler.com/bliki/UnitTest.html

When do you use a mock, stub, fake or test double today?

- End 2 end testing 
- Acceptance test
- Characterizing test
- Given when then/BDD/UAT 
- Integration testing
- Unit testing

What do you mock today?
- Other peoples code 
- Your own code
- Both
- Sometimes both


### Concept: 
We want to expand our System Under test to encompass:
From Adapter to Port in a hexagonal architeture. In a more traditional n tier application it would be external services, api's database eg.

We want to put our test doubles after the port or as low as possible in a layered architecture, think crossing process boundaries. Or perhaps when things are tricky, like dates and time.

We want to do it from the outside, driven by our guiding test and use that DSL as a basis for our inner loop. We can add more test in the inner loop, maybe there are some edge cases, bounday values eg. (not the focus of this session, we stay on the happy path.)

#### Demo: Stepping into the inner loop.
We first demo the last part of the Acceptance test:
Implementation of the WithDraw method and show how the different "dependencies" as being empty.
NEED to point to commit or something here...

Then moving into the inner loop after a failed assertion.

Demo "copy" paste of scenario test into a Unit test.
We take our composition root for our design for this scenario:
````
_calendarStub = new CalendarStub()
_bankStatementPrinterSpy = new BankStatementPrinterSpy()
new AccountService(_calendarStub, new FakeTransactionRepository(), _bankStatementPrinterSpy)
````

Along side our test dsl:
````
void Deposit(int of, DateTime on) {...}  
void WithDraw(int of, DateTime on) {...}  
void PrintBankStatement() {...}
void ExpectedPrintedStatement(string) {...}
````

And copy it to a new unit test file, basically you delete our Acceptance scenario test case.

Write the first "fact" test and make an "open" assert, maybe talk to the team about what would be the simplest test at this stage (printing the header).

Do that test and show the test go green by faking, talk about it's okay to commit even though the acceptance test is still red and then it's over it them.

WIP!!!!
Basically these commits:
https://github.com/STRUDSO/Bank.Kata/commit/d4e5171f811f3af26a2c50e8d65e5b5432be90dd
https://github.com/STRUDSO/Bank.Kata/commit/673fa0f0463dd40ba66b113f14f4719ab8864c9d



### Do: 

Take the Acceptance test and convert to inner loop.  
Put more and more of the design into play as you drive the design based on the acceptance test.
There is a little design exercise hidden. (x marks the spot.)
Use the test dsl from the scenario to drive the system under test.  
You don't have to use the exact examples from the acceptance test. you can find more and maybe you also need some edge cases. (not the intention behind this exercise)

Pick a test and implement it:   
- [ ] Print Empty Account  
- [ ] Deposit Amount  
- [ ] Withdraw Amount



![img.png](/assets/images/learning-hours/outside-in-design-sketch.png)

Bonus:
- Use a mocking framework instead of handcoded test doubles.
- Start thinking about "real" implementation of the Repository

### Reflect: 
Contrast this with how you traditional have designed from the bottom up and maybe have had less of the system under test.  
Does this make things easier when we don't need to design the database or the api interactions first?
Does this make you reflect over your design...
Does this increase or decrease your confidence in the code?