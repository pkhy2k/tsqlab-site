---
title: "What to Test First: Risk-Based Testing for Hotel Systems"
subtitle: Setting test priorities by likelihood and impact, and a proposal for impact criteria suited to hotel operations
category: column
author: director
thumbnail: /images/posts/en/report-risk-based-testing-hotel.jpg
thumbnail_alt: Illustration summarising the article
cover: /images/posts/en/report-risk-based-testing-hotel-cover.jpg
date: 2026-11-01
summary: There is never enough time for testing. Using a risk matrix for a new settlement function as the main example, I set out the principles and steps of risk-based testing, how to apply it to test estimation and regression scope, and propose impact criteria that reflect the nature of hotel operations.
tags: [Columns, Risk-Based Testing, Test Management, Regression Testing, Settlement, Hotel IT]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 1장, 6장, 10장, 11장, 12장."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

Release schedules for hotel systems are usually tied to business schedules. The opening date of a new hotel, the start of peak season and the launch of a promotion are set regardless of how software development is going. As a result, people responsible for quality assurance almost always find themselves unable to test everything in the time available.

One of ISTQB's testing principles is that exhaustive testing is impossible. My book *Let's Do QA Together with AI Agents* (in Korean) shows this in numbers. Combining stays of 1 to 14 nights, 1 to 4 guests, three room types, member or non-member and all 365 days of the year gives 14 × 4 × 3 × 2 × 365 = 122,640 combinations. The question is not "What should we test?" but "What should we test first, and how deeply?" This article explains risk-based testing, a way of answering that question, in the context of hotel systems.

## 1. Defining and measuring risk

A risk is something bad that might happen. The size of a risk is judged on two dimensions.

- **Likelihood**: The probability that it will happen
- **Impact**: The size of the damage if it does

The level of risk is found by multiplying the two (risk level = likelihood × impact). Risks include **project risks**, which threaten the project, such as schedule delays, staff shortages and test server outages, and **product risks**, which threaten the quality of the product, such as calculation errors, slow responses and security vulnerabilities. Risk-based testing mainly deals with product risks.

Risk management consists of an **analysis** stage, in which risks are identified and sized, and a **control** stage, in which responses are decided, carried out and monitored. The main response to product risks is to reduce them through testing: the higher the risk of a function, the earlier, more deeply and with more techniques it is tested. Other responses include accepting the risk as it is, transferring it to another party and preparing contingency plans for when problems occur.

## 2. Case: a risk matrix for a new settlement function

The book uses the example of a new settlement function being introduced at a hypothetical hotel, "QA Stay", two weeks before opening. The team listed product risks and rated likelihood and impact on a scale of 1 to 3.

- **Miscalculated payment amount after discounts**: likelihood 3, impact 3, level 9. Test first, with every rule in the decision table and boundary values.
- **Receipt amount mismatched after a partial refund**: likelihood 2, impact 3, level 6. Test second, focusing on refund scenarios.
- **Duplicate payment when the card payment gateway responds slowly**: likelihood 2, impact 3, level 6. Address through system integration testing and error guessing.
- **Mismatched totals in the end-of-day report**: likelihood 2, impact 2, level 4. Check by comparing against sample data.
- **Broken receipt print layout**: likelihood 2, impact 1, level 2. Check quickly with a checklist.

The value of this table lies less in the calculation itself than in the agreement it creates. A single table produces an answer, with reasons, to "What will we look at first, and how deeply, over the next two weeks?" When a QA specialist tells a manager "We'll take a light look at the receipt layout", it becomes a reasoned judgement rather than laziness.

## 3. Three criteria for priority, and dependencies

The book presents three common criteria for deciding the order of testing.

- **Risk-based**: Highest risks first
- **Coverage-based**: Whatever covers the most ground with the fewest tests first
- **Requirements-based**: Requirements that stakeholders have marked as important first

When deciding the order, however, dependencies between functions must also be considered. Even if settlement testing is the most important, you cannot reach settlement if bookings cannot be created. Risk ranking decides "what to look at deeply"; dependencies decide "what can be run first".

## 4. Estimation: how many days will it take?

"How many days will testing take?" is the question QA specialists are asked most often. Answers based on gut feeling usually fall short. Of the methods the book introduces, three-point estimation is easy to use on your own. Take an optimistic value (a), a most likely value (m) and a pessimistic value (b), and calculate E = (a + 4m + b) ÷ 6.

For example, with an optimistic estimate of 4 days, a most likely estimate of 6 days and a pessimistic estimate of 14 days, the result is (4 + 24 + 14) ÷ 6 = 7 days. Even if the most likely value is 6 days, allowing for pessimistic situations such as test server outages or many defects makes 7 days the safer figure. Used together with the risk matrix, it lets you request time for high-risk functions with a clear basis.

## 5. Applying it to regression scope

Risk-based thinking is also used to decide the scope of regression testing after a defect is fixed. Confirmation testing, which rechecks the fixed defect, is simple; regression testing, which checks that the fix has not broken other functions, always raises the question of "how far".

In a case where the discount calculation logic was fixed, the book analyses the impact on each function to set the scope. Creating, changing, and cancelling and refunding bookings are rated "high" impact, so the whole decision table is rerun, prices are recalculated after changing the length of stay, and refund amounts for discounted bookings are checked. Receipts and the end-of-day report are rated "medium", so only the amounts for two discounted bookings are checked. Check-in and check-out are rated "low", so normal operation is checked with one representative scenario. Writing down these reasons means you can later answer the question "Why did you only take a light look at this function?"

## 6. Evidence for likelihood: VOC and defect history

The part of risk assessment most prone to subjectivity is likelihood. Based on the tendency of defects to concentrate in certain functions (defect clustering), the book recommends looking more closely at areas with many past defects and many customer inquiries (VOC). In the book's VOC analysis example, changes and cancellations had the most suspected-defect inquiries, at 9, while settlement had only 4 but high severity because money was involved. Data like this grounds likelihood scores in records rather than intuition.

## 7. The Lab's proposal: impact criteria suited to hotel operations

From here on is the Lab's proposal based on the book. As the book's example shows, the highest-impact risks in hotel systems are usually related to money. But damage to a hotel is not measured in money alone. As in the Room 703 double-booking case, defects spread to the guest experience, staff work and the hotel's reputation. When scoring impact, I therefore propose considering the following four perspectives together.

1. **Financial impact**: Are guests overcharged, or does the hotel lose revenue?
2. **Guest experience impact**: Do guests directly suffer inconvenience or disadvantage on site?
3. **Operational impact**: Do front desk, housekeeping or settlement operations stop, or require manual workarounds?
4. **Reputational and compliance impact**: Could it lead to online reviews or breaches of data protection rules or terms and conditions?

Under this approach, impact is rated high if any one of the four applies strongly. These criteria carry over into test management the service quality perspective of looking at both the quality customers perceive and the organisation's operational quality. If hotel IT organisations draw up risk matrices together with operations departments, they can reflect in their priorities impacts that development teams alone cannot see.

## 8. Conclusion

The core of risk-based testing is to accept the reality that you cannot look at everything, and within that, to look first and most deeply at what would hurt most. A risk matrix turns that judgement into a basis the team can share. In hotel systems, functions involving money usually come out on top, but only when guest experience, operations and reputation are included in impact assessment do you get priorities suited to quality management in a service industry.
