---
theme: frontend_testing
title: Introducing Frontend TDD
difficulty: 1
author: ronheywood
affiliation: Spektrix
tags: frontend tdd javascript testing
---

# Introducing Frontend TDD

Goal: Understand how TDD applies to browser-based development and how the testing pyramid maps to modern JavaScript apps.

# Connect:

## Bug Stories

In pairs, share stories about bugs you've encountered on websites or bugs you've released yourself:
- What happened?
- How did it make you feel?
- What was the impact (on users, business, team morale)?
- How was it discovered?
- Could it have been prevented with better testing?

After 5 minutes of discussion, ask for volunteers to share key insights with the whole group.

# Concept:

**Introduce the differences between front-end and back-end testing strategies**

**Reference the Test Desiderata: speed, reliability, feedback, cost (see [Test Desiderata]({% link _learning_hours/test_design/test_desiderata.md %}))** 

**An updated test pyramid (static, unit, integration, End to end)**

![The test automation pyramid is biased towards favoring more unit tests, for speed and predictability and fewer UI tests which are slower and more error prone](/assets/images/frontend-tdd/The_test_automation_pyramid.png)

> The pyramid is based on the assumption that broad-stack tests are expensive, slow, and brittle compared to more focused tests, such as unit tests.

In front-end testing, our integration tests are much more valuable, and they're much faster than backend integration tests too, since there's often little to no infrastructure required.

End to end tests remain slow and sometimes brittle, so we still use these sparingly to give us confidence on those components that could cause reputational damage if they fail.

### The Test Trophy
Visualize the pyramid now more like:
![Testing trophy diagram showing the distribution of test types: many integration tests in the middle, some unit tests at the bottom, few end-to-end tests at the top, and static analysis as the base]({% link /assets/images/frontend-tdd/testing-trophy.png %})

### Static Test Tools
* [ESLint](https://eslint.org/) - Identifies problematic patterns in JavaScript code
* [TypeScript](https://www.typescriptlang.org/) - Static type checking for JavaScript
* [Prettier](https://prettier.io/) - Code formatting tool
* [SonarQube](https://www.sonarsource.com/products/sonarqube/) - Code quality and security scanner

### Unit Test Tools
* [Jest](https://jestjs.io/) - JavaScript testing framework with built-in assertion library
* [Vitest](https://vitest.dev/) - Blazing fast unit test framework powered by Vite
* [Mocha](https://mochajs.org/) - Flexible JavaScript test framework
* [Jasmine](https://jasmine.github.io/) - Behavior-driven development framework

### Integration Test Tools
* [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) - Testing React components
* [Vue Test Utils](https://test-utils.vuejs.org/) - Testing Vue components
* [Angular Testing Utilities](https://angular.io/guide/testing) - Testing Angular components
* [Playwright Component Testing](https://playwright.dev/docs/test-components) - Component testing across frameworks

### End to End Test Tools
* [Cypress](https://www.cypress.io/) - JavaScript end-to-end testing framework
* [Playwright](https://playwright.dev/) - Reliable end-to-end testing for modern web apps
* [Selenium](https://www.selenium.dev/) - Browser automation tool
* [TestCafe](https://testcafe.io/) - Automated browser testing

## Concrete Practice:

Diagram the test trophy as it would apply to your website.
Which features and components would benefit from which kind of test?

## Conclusions:


### Further Reading:
[Martin Fowler – The Practical Test Pyramid](https://martinfowler.com/bliki/TestPyramid.html)

[Kent C. Dodds – Write Tests. Not Too Many. Mostly Integration](https://kentcdodds.com/blog/write-tests)

<iframe width="1007" height="566" src="https://www.youtube.com/embed/Fha2bVoC8SE?list=PLV5CVI1eNcJgNqzNwcs4UKrlJdhfDjshf" title="Kent C. Dodds – Write tests. Not too many. Mostly integration." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen aria-label="Video: Kent C. Dodds explains testing strategy focusing on integration tests"></iframe>