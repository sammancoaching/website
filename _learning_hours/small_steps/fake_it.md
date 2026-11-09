---
theme: small_steps
title: Fake It Til You Make It
kata: binary_diagnostic
difficulty: 2
author: pfichtner
affiliation: Atruvia
tags:  small_steps tdd
---

# Fake It Til You Make It

This session covers three strategies to getting to green faster when doing TDD: Fake It ('Til You Make It), Obvious Implementation and Triangulation. The learning hour is particularly suitable for people who are already familiar with TDD but have trouble understanding the terminology. There is also often a misunderstanding about how to deal with a fake

## Learning Goals

* Describe three approaches to passing a failing test in TDD: Fake It ('Til You Make It), Obvious Implementation and Triangulation with focus on the first one.
* Use Fake It ('Til You Make It) during development

## Session Outline

* 5 min connect: misconceptions about fakes
* 15 min concept: three TDD approaches and live demo
* 30 min concrete: practise the same kata from scratch
* 10 min conclusions: reflect on what changed

### Connect: misconceptions about fakes

In pairs, think of three common misconceptions about using fakes in TDD. After a few minutes, share with the whole group.

Then, as a whole group, review these statements together. Mark each as true or false and debrief:

* Before writing "real code" in TDD, you always start with a fake. -> False. Not always - see Obvious Implementation in the next section.
* Fakes are used to get the test green first. -> True. But that is only the first step; from there you continue with "fake it 'til you make it."
* In the next step, a fake is replaced by the real implementation. -> False. A fake can also be replaced by one or more better fakes. If we throw it away immediately, it probably did not help us much.
* In TDD, there are other approaches besides fakes. -> True. For example, Obvious Implementation and Triangulation.

### Concept - Green Bar Patterns

When your test is red and you need to get to green, there are three main approaches you can take.

**Obvious Implementation** means you write the code you believe is correct directly. If the test stays red, stop - do not keep guessing or experimenting aimlessly. This approach works well when you already know the solution and don't need to discover it through the tests.

**Fake It ('Til You Make It)** means you return a constant or write the simplest possible code to make the test pass. The fake does not need to look clean or elegant - that is okay. The real solution will emerge as you add more tests and refactor. An example follows. This is a powerful way to let the tests drive the design incrementally.

**[Triangulation]({% link _learning_hours/small_steps/triangulation.md %})** means you add additional test cases to force a more general programmatic solution. You start with a specific case, add another that reveals the limitation, and generalise when the duplication between special cases becomes obvious.

These approaches can be mixed and swapped during development, even within the same TDD cycle.


### Concrete: Demo

The “Binary Diagnostic Kata” provides a solid foundation for how to replace fakes step by step, illustrating the process at each stage. 
Introduce the rules of the kata and do a short live demo. While demonstrating, use as many automated IDE refactorings as possible. Run the test(s) after each step. In the small steps, you can also include an error here and there to show how it affects the development process (we don't have to think or search for long to figure out what's wrong).

Suggested implementation steps:

1. Write a test, for example: `assertThat(calcDiagnose(diagnose)).isEqualTo(198)`. Start with a fixed solution.
2. Replace `198` with `22 * 9`.
3. Replace `22` and `9` with function calls (Extract Method), pass in diagnose, and adjust the target methods.
4. Express `22` as `Integer.valueOf("10110", 2)` and do the same for `9`. This is a good place to try to trigger an error, for example, by using an incorrect `Integer.valueOf("10110")`.
5. In the `gamma()` function, replace the first bit with a method such as `mostCommonBit(String[] diagnose, int column)`. Split out the string, extract a method, and adjust the signature:

        private int gamma(String[] diagnose) {
            return binToDec("1" + "0110");
        }

    Then extract again:

        private int gamma(String[] diagnose) {
            return binToDec(mostCommonBitInColumn0(diagnose) + "0110");
        }
        private String mostCommonBitInColumn0(String[] diagnose) { return "1"; }

6. Continue implementing `mostCommonBitInColumn0`. For example, copy in the values for column 0 and count them manually:

        private String mostCommonBitInColumn0(String[] diagnose) {
            // column0 0111100
            long zeros = 3;
            long ones = 4;
            return ones > zeros ? "1" : "0";
        }

    Then replace part of the manual counting with real code:

        private String mostCommonBitInColumn0(String[] diagnose) {
            String column0 = "0111100";
            long zeros = column0.chars().filter(ch -> ch == '0').count();
            long ones = 4;
            return ones > zeros ? "1" : "0";
        }

7. Next, either duplicate the counting logic for `'1'`, or extract it into a reusable helper method first.
8. This is where the demo ends.
9. A possible next step is to replace the fake for column0, again using Extract Method:

        private String column0(String[] diagnose) {
            return "0111100";
        }

    Then replace it step by step:

        private String column0(String[] diagnose) {
            return "0" + "111100";
        }

        private String column0(String[] diagnose) {
            return diagnose[0].substring(0,1) + "111100";
        }

        private String column0(String[] diagnose) {
            int line = 0;
            return diagnose[line++].substring(0,1)
                + diagnose[line++].substring(0,1)
                + diagnose[line++].substring(0,1)
                + diagnose[line++].substring(0,1)
                + diagnose[line++].substring(0,1)
                + diagnose[line++].substring(0,1)
                + diagnose[line++].substring(0,1);
        }

        private String column0(String[] diagnose) {
            int beginIndex = 0;
            int endIndex = beginIndex + 1;
            int line = 0;
            return diagnose[line++].substring(beginIndex, endIndex)
                + diagnose[line++].substring(beginIndex, endIndex)
                + diagnose[line++].substring(beginIndex, endIndex)
                + diagnose[line++].substring(beginIndex, endIndex)
                + diagnose[line++].substring(beginIndex, endIndex)
                + diagnose[line++].substring(beginIndex, endIndex)
                + diagnose[line++].substring(beginIndex, endIndex);
        }

    Then refactor from this into a loop or stream:

        private String column0(String[] diagnose) {
            int beginIndex = 0;
            int endIndex = beginIndex + 1;
            return Arrays.stream(diagnose)
                .map(l -> l.substring(beginIndex, endIndex))
                .collect(joining());
        }

    Then inline a little more and introduce column as a parameter:

        private String column0(String[] diagnose, int column) {
            return Arrays.stream(diagnose)
                .map(l -> l.substring(column, column + 1))
                .collect(joining());
        }

    At this point, `gamma()` is implemented well enough for now.

It may also make sense to use a smaller example to drive the implementation, for example `{ "01", "01", "10" }`. Together with the `198` test this gives you an acceptance test that you can mark as `@Disabled` at the beginning and only enable at the end. Once the implementation is complete, it must pass. This helps reduce the risk of accidentally leaving a fake in the final code.

### Concrete: Exercise

Now let the participants start over and do the exercise themselves. Other approaches are fine too, as long as they use fakes as part of the process.

Possible alternative katas:
* FizzBuzz
* Phone Number

See the related material by Llewellyn Falco. He also offers deeper conceptual guidance, for example around: separate - encapsulate - calculate - automate - clean.

### Conclusions

Ask participants to write cards in response to a guiding question (e.g. "How has your understanding of fakes changed?"). Give them 2 minutes for this. Then go through all cards together and discuss them.


## See also

* [Triangulation Learning Hour]({% link _learning_hours/small_steps/triangulation.md %})

# Acknowlegements
This learning hour was first published elsewhere: [Fake It Til You Make It](https://github.com/atruvia/samman-coaching-website/blob/lh-additions/_learning_hours/small_steps/fake_it.md)
