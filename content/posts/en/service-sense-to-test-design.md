---
title: "When the Front Desk's 'What If?' Becomes a Test Case"
subtitle: How to turn the instincts of the hotel service front line into software testing techniques, and why verification matters more in the age of AI
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/service-sense-to-test-design.jpg
thumbnail_alt: Illustration summarising the article
date: 2026-11-01
pick: true
summary: The "What if this happens?" question experienced front desk staff ask out of habit has the same structure as software testing techniques. Using rules on length of stay, multi-night discounts and booking status, we explain equivalence partitioning, boundary value analysis and state transition testing, and offer a perspective for verifying tests created by AI agents.
tags: [Software QA, Test Techniques, Boundary Value Analysis, State Transitions, AI Agents, Hotel IT]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

Experienced front desk staff often think "what if" when looking at a booking screen. What if the check-out date is earlier than the check-in date? What if someone tries to check in with a cancelled booking? These questions, meant to prevent guest inconvenience in advance, have the same structure as the way of thinking used to design test cases in software quality assurance (QA).

Director Winston Park's book *Let's Do QA Together with AI Agents* (in Korean) focuses on this connection. This article picks three of the test techniques covered in the book that relate to hotel work and looks at how frontline instincts become systematic test design. The examples are based on the rules of the book's hypothetical hotel, "QA Stay".

## Equivalence partitioning through length-of-stay rules

QA Stay has the following rules.

- Stays of 1 to 14 nights can be booked.
- Stays of three nights or more get a 5% discount on the room rate.

Checking every case from 1 to 14 nights one by one is inefficient. Equivalence partitioning divides values the system is expected to handle in the same way into groups (partitions) and checks a representative value from each. The length of stay in the rules above divides as follows.

- Valid partitions: 1–2 nights (no multi-night discount), 3–14 nights (5% multi-night discount)
- Invalid partitions: 0 nights or fewer, 15 nights or more

Checking one value from each partition, for example 0, 2, 5 and 20 nights, covers every partition once with four tests. It is the same way front desk staff divide situations into "short stays without a discount, stays with a discount, and stays we cannot accept". The book stresses putting only one invalid value in each test. If you enter invalid values for both length of stay and number of guests at once, you cannot tell which one caused the error message.

## Defects live at the boundaries: boundary value analysis

On the front line, problems often arise where rules change. Missing a single inequality sign, such as a developer writing "14 nights or fewer" as "fewer than 14 nights", is a very common mistake. In that case guests staying 14 nights cannot book, but checking only the representative value of 5 nights would not find this defect.

Boundary value analysis targets defects like this. The two-value boundary value analysis set out in the ISTQB CTFL syllabus checks the edge value of each partition together with the closest value in the neighbouring partition. In the rules above, partitions meet at three boundaries, so six values are checked.

- 0 and 1 nights: the boundary between cannot book and can book
- 2 and 3 nights: the boundary between no multi-night discount and a 5% discount
- 14 and 15 nights: the boundary between can book and cannot book

In the prologue, the author recalls realising only when studying testing that his front-line habit of always trying 14 and 15 nights when there was a 14-night booking limit was boundary value analysis. A front desk employee's checking question, "Do three nights get the discount?", is also boundary value analysis performed by hand.

## State transition testing that follows the life of a booking

A booking's status changes over time. Simplified, it moves from "confirmed" through "checked in" to "checked out", and can branch along the way into "cancelled" or "no-show". State transition testing checks that allowed transitions happen correctly and that disallowed transitions are blocked.

From a service quality perspective, the latter matters more. Errors such as a check-in being processed on a cancelled booking, or a checked-out booking returning to checked-in status, disrupt room assignment and settlement as a whole. The moment front-line staff wonder, "This booking has already been cancelled, so why can I press the check-in button?" is exactly where a test for invalid transitions is needed.

## In the age of AI agents, the role that remains is verification

Recently, giving specifications to AI agents and having them create test conditions and test cases has been spreading. Part 3 of the book covers this process, including the step of verifying and correcting what the AI produces.

Applied to the length-of-stay example above, the verification perspective becomes clear: checking whether the list of test cases the AI made includes all the boundary values 0, 1, 14 and 15 as well as the discount boundary of 2 and 3 nights, whether only one invalid value is included per test, and whether invalid transitions such as checking in a cancelled booking are covered. You have to know the test techniques to notice what is missing.

> Creating tests can be left to AI, but judging whether those tests are sufficient is still a human job.

## Implications

The front-line instincts that hotel service staff have built up are not a capability that disappears in digital transformation; they can carry over into a capability that protects system quality. For those instincts to lead to systematic test design, however, a common language such as equivalence partitioning, boundary value analysis and state transitions is needed. When hotel IT organisations and educational institutions design pathways for developing service professionals into QA staff, they should consider teaching this language together with training in verifying what AI produces.
