---
title: "Errors, Defects and Failures Through the Double Booking of Room 703: A Question That Matters More Than 'Whose Fault?'"
subtitle: Following a case in which two bookings were assigned to the same room on the same night reveals the structure and root causes of software quality problems
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/room-703-error-defect-failure.jpg
thumbnail_alt: Illustration summarising the article
date: 2026-11-01
summary: Through a hypothetical case in which a hotel reservation system assigned the same room to two guests, we explain ISTQB's distinction between errors, defects and failures, and show why root cause analysis, rather than assigning blame, prevents recurrence.
tags: [Software QA, Errors Defects Failures, Root Cause, ISTQB, Hotel IT]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 1장."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

At 3 p.m. on a Saturday, a business traveller checked in at a hotel front desk and the system assigned Room 703. Just as the key was handed over, a family standing nearby looked puzzled. They had checked in on Friday for two nights until Sunday and were already staying in Room 703.

Director Winston Park's book *Let's Do QA Together with AI Agents* (in Korean) opens Chapter 1 with this scene at a hypothetical hotel, "QA Stay". Staff apologised to the business traveller and resolved the situation with a free upgrade to a vacant suite. But the hotel lost a night's revenue from a suite it could have sold, and if there had been no vacant room, the guest would have had to move to another hotel. A small software defect does not end on the screen; it spreads to the guest experience, staff's day, and the hotel's revenue and reputation.

In the meeting after the incident, someone asked, "Whose fault is this? The developer's, the specification's, or did testing miss it?"

## One incident, three names

The International Software Testing Qualifications Board (ISTQB) distinguishes three levels of terms to describe situations like this.

Tracing the cause back, the developer had miscalculated the last night a guest stays when building the condition for finding "available rooms". A guest who checks in on Friday and checks out on Sunday stays Friday and Saturday nights. The code, however, subtracted an extra day from the check-out date and calculated the stay as Friday night only, so Room 703 showed as vacant on Saturday night.

- **Error**: A mistake made by a person. In this case, the developer's judgement in miscalculating the last night. Errors are not made only by developers; a planner leaving out a condition or a tester writing down the wrong expected result are also errors.
- **Defect**: The flaw an error leaves in code or documents, commonly called a "bug". A wrong sentence in a specification is also a defect.
- **Failure**: The phenomenon in which a defect surfaces during execution and the system behaves differently from what is expected. Here, the moment another booking is placed in the same room on the last night of a guest staying two or more nights.

The book stresses two points about this relationship. First, a defect does not always cause a failure. The Room 703 defect stayed hidden on weekdays, when there were many vacant rooms and the system assigned another one, and only appeared on a peak-season weekend when the hotel was full. Second, failures are not caused only by defects. Environmental conditions such as a server's time zone setting or a network outage can also cause failures, so when a failure is found, you should first record the conditions under which it occurred before concluding that "the code is wrong".

## Root causes rather than blame

The meeting went one step further than "whose fault". Why did the developer understand it that way? Rechecking the specification, they found only the word "nights", with no definition anywhere of up to which night a guest uses the room. Behind the developer's mistake lay an ambiguous specification.

The most fundamental reason a problem occurred is called its **root cause**. Fixing the code alone makes the Room 703 problem go away, but if the way specifications are written does not change, similar problems will arise again in other functions. The purpose of finding root causes is not to blame people but to keep the same thing from happening again.

> Fixing defects is the job of testing; keeping defects from recurring is the job of quality assurance.

## Questions from the service front line prevent defects

The implication of this case for the hotel industry is clear. What was needed to understand the Room 703 problem was not a programming language but the frontline sense of "When is a two-night guest's last night?" The book's epilogue reports that after the incident, the QA Stay team began inviting a tester when writing specifications. A single question the tester asked in a meeting, "How do we count nights?", prevented the next Room 703.

One of ISTQB's testing principles is that early testing saves time and money. If the Room 703 problem had been found at the specification stage, fixing one sentence would have been enough. This is also why the whole-team approach is emphasised, in which planners, developers and testers share responsibility for quality from the start rather than leaving it to one tester.

Improving the quality of hotel IT systems ultimately means creating a structure in which people who know the front line can ask the right questions early in development. Organisations that ask about the inconvenience guests suffered not "Whose fault is it?" but "Where did it come from?" do not repeat the same mistakes.
