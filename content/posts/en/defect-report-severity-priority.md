---
title: "'Discount looks odd, please check' Is Not a Defect Report"
subtitle: How to structure a report developers can reproduce in one go, and why severity and priority must be judged separately
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/defect-report-severity-priority.jpg
thumbnail_alt: Illustration summarising the article
date: 2026-11-01
summary: A one-line note left in a hurry can cost the development team a day. Using a hotel rate discount defect as an example, we set out how to write defect reports centred on reproduction steps, expected results and actual results, and the criteria for judging severity and priority separately.
tags: [Defect Reports, Severity, Priority, AI Agents, Software QA]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 6장, 10장."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

A tester checking the rate calculation function of a hotel reservation system found an odd result. Calculating three nights in a deluxe room with a member account produced a different figure from the one expected. In a hurry, the tester left this note for the development team: "Member 3 nights, discount looks odd. Shows 15%. Please check."

The developer who received the note had no choice but to ask back: which room was it, was it peak season, which version, and why is 15% wrong? A day passes while questions and answers go back and forth. Chapter 10 of Director Winston Park's book *Let's Do QA Together with AI Agents* (in Korean) starts from this scene to show that "communicating" a defect matters as much as "finding" it.

## Say what is wrong in numbers

The book's hypothetical hotel, "QA Stay", has the following discount rules. Members get 10% off and stays of three nights or more get 5% off; if both apply, only the larger discount is given. The deluxe room rate is fixed at KRW 100,000 per night.

Under these rules, a member staying three nights in a deluxe room has a list price of KRW 300,000, and only the larger 10% discount should apply, giving KRW 270,000. The screen, however, showed the two discounts combined, 15%, or KRW 255,000. The note "discount looks odd" conveys none of this.

## Three pillars of a good defect report

The book identifies three items that are decisive for developers to reproduce a problem.

- **Steps to reproduce**: Number them and write one action per step. Anyone who follows them should get the same result.
- **Expected result**: State what should happen, citing the requirements document. In the example above, "10% discount, KRW 270,000 (discount rules requirement)".
- **Actual result**: Write down exactly the figures, messages and screen state that actually appeared.

The title follows the format "[screen or function] condition + symptom". Instead of "Discount error", write "[Create booking] 15% combined discount applied when a member books 3 or more nights", so that the title alone shows where, under what condition and what happened. Adding preconditions such as version and environment, number of guests and whether it is peak season lets the developer start reproducing without asking questions.

## Reports written by AI agents must be verified too

The book shows how to give a hurried note to an AI agent and have it turned into a standard report. It also shows the process of verifying the result rather than using it as is. In the book's example, the AI agent inserted a step, "leaving the coupon code field empty", into the reproduction steps, although it was not in the note. QA Stay's screen had no such field; the AI had imagined a generic booking screen and added a plausible step. The preconditions also left out the number of guests and whether it was peak season, both of which affect the discount rules.

The lesson of this case is simple. The surest way to check that a report is complete is for the tester to follow the reproduction steps the AI wrote one more time. The report is complete when the defect reproduces by following those steps.

## Judge severity and priority separately

Defect reports often record severity and priority together, but the two criteria are different in nature.

**Severity** is the size of the defect's impact on the system and the business, and is mainly judged by the tester. Using hotel systems as an example, the book suggests the following levels.

- Critical: Core operations stop, data is lost or there is a security problem. For example, check-in is impossible or payments are charged twice
- High: Major functions malfunction or there is financial loss. For example, combined discounts or a room assigned twice
- Medium: The function works but is inconvenient, and there is a workaround
- Low: Minor display problems, such as a typo on a button

**Priority** is how quickly it must be fixed, and is decided by managers or product owners taking schedules, customers and business circumstances into account.

The two criteria do not always move together. An error in a year-end settlement report used once a year may be high in severity but low in priority, since it only needs to be fixed before the year end. Conversely, a typo in the hotel's name on the home screen has low severity because it does not affect any function, but if there is an opening event the next day, it must be fixed first. Recording the two criteria separately lets the team decide the order of fixes rationally.

> A defect report is not about "who got it wrong" but about passing on information: "under these conditions, it behaves like this".

## Similar to reporting habits on the service front line

Anyone who has worked in a hotel will find this principle familiar. A good handover note does not say "Guest in 703 unhappy" but "Guest in 703 complained at 9 p.m. about a missed room service order; first response was a complimentary dessert; check again at breakfast tomorrow". The habit of separating facts and conditions from expectations and results builds trust in the same way on the service front line and in quality assurance.
