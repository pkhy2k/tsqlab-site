---
title: "A QA Case Study of Hotel Booking Changes and Cancellations, from Specification Review to Completion Report"
subtitle: Following a two-week hypothetical QA project through five deliverables to see the whole process of hotel system quality assurance
category: column
author: director
thumbnail: /images/posts/en/report-cancellation-qa-case.jpg
thumbnail_alt: Illustration summarising the article
cover: /images/posts/en/report-cancellation-qa-case-cover.jpg
pick: true
date: 2026-11-01
summary: I analyse a two-week QA project for a hypothetical hotel's booking change and cancellation function in five stages: requirements review, test planning, test design, execution and defect management, and completion reporting. From a defect found at a cancellation penalty boundary, I draw principles for assuring the quality of functions that involve money.
tags: [Columns, Case Study, Cancellations, Cancellation Penalties, Boundary Value Analysis, Software QA, Hotel IT]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 12장."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

Booking changes and cancellations are among the functions in hotel systems where guest complaints and financial disputes arise most often. Cancellation penalties depend on how long remains before check-in, changes require rates and discounts to be recalculated, and after a cancellation the room must immediately return to sale. If anything goes wrong at any point, guests are overcharged or the hotel loses revenue.

Using the comprehensive exercise in Chapter 12 of my book *Let's Do QA Together with AI Agents* (in Korean) as a case, this article analyses how quality assurance activities connect as a single function moves from specification to release decision. The case is set at a hypothetical hotel, "QA Stay", and to keep calculations simple the deluxe room rate is fixed at KRW 100,000 per night.

## 1. Project overview

QA Stay is developing a new "booking change and cancellation" function. The QA specialist has two weeks and must produce five deliverables.

1. Requirements review results (a list of questions for the planner)
2. A test plan summary
3. Test cases and a traceability matrix
4. Defect reports
5. A test completion report

The specification (v0.9) has five core requirements. Guests can change the date, room type and number of guests up to two days before check-in (C-01). Changes trigger recalculation of rates and discounts, and the changed booking must still follow the rules on occupancy and length of stay (C-02). Cancellation is free up to seven days before check-in, 50% from three to six days before, and 100% from two days before to the day of check-in (C-03). Guests who do not arrive by the day of check-in are treated as no-shows and charged 100% (C-04). When a booking is cancelled, the room becomes vacant and a cancellation confirmation email is sent (C-05).

## 2. Requirements review: testing starts with the specification

In this case, the first quality assurance activity is not running tests but reviewing the specification. The QA specialist first reviews the specification alone and writes down questions from a frontline perspective, then asks an AI agent to find ambiguities, omissions and contradictions, and finally combines the two to finalise the list of questions for the planner.

The finalised questions are of the following kinds.

- **Ambiguous criteria**: Is "two days before" based on calendar dates or 48 hours before the check-in time? Does "by the day of check-in" mean midnight or the front desk's closing time?
- **Conflicts between rules**: If a date change moves the stay into peak season, is the discount removed? How is the difference explained to the guest?
- **Missing calculation basis**: Is the penalty based on the amount before or after discounts? If a guest cancels after changing the date, is the penalty based on the original or the new date?
- **Unclear scope**: Can part of a multi-room booking be cancelled?

The planner answered that days are counted by calendar date, penalties are based on the amount paid after discounts, cancellations after a change are based on the new check-in date, and partial cancellation is outside the scope of this release.

Notably, many of these questions could only occur to someone who has worked at a front desk or in settlement. The basis amount for penalties in particular is the first point of contention in real guest disputes, yet it was missing from specification v0.9. This omission reappears at the end of the project under "lessons learned".

## 3. Test planning: functions involving money come first

The test plan covers objectives, scope, approach, risk priorities, entry and exit criteria, and schedule. The scope includes changes, rate recalculation, cancellation penalties, no-shows, room status and emails, and excludes partial cancellation and actual refund processing by the payment gateway.

Risk priorities were set in the following order.

1. Miscalculated penalty amounts
2. Errors in recalculating discounts after changes
3. Room status not updated after cancellation

The book explains that putting functions involving money at the top is basic practice in hotel system QA. The exit criteria are 100% execution of test cases, zero defects of "high" severity or above, and agreed responses for unresolved defects. Setting exit criteria in advance like this reduces the need for emotional arguments just before release about "when to stop testing".

## 4. Test design: combining four techniques

### 4.1 Boundary value analysis of penalty bands

If D is the check-in date minus the cancellation date, the penalty rules fall into four partitions. If D is 7 or more, cancellation is free; if 3 to 6, 50%; if 0 to 2, 100%; and if below 0, the check-in date has passed, so the cancel button is disabled and the no-show rule applies.

There are three boundaries: between 6 and 7, between 2 and 3, and between −1 and 0. The test values chosen by two-value boundary value analysis are the six values 7, 6, 3, 2, 0 and −1. In the same way, for whether changes are allowed (C-01), changes are possible if D is 2 or more and not possible if D is 1 or less, so 2 and 1 are tested.

### 4.2 A decision table for discounts after changes

QA Stay's discount rules are 10% for members and 5% for stays of three nights or more; if both apply, only the larger discount is given, and there are no discounts in peak season. When a change alters the length or dates of a stay, the booking must pass these rules again. The case focuses on three changes.

- Changing a non-member's 3-night stay to 2 nights: the 5% multi-night discount disappears, so KRW 285,000 should become KRW 200,000.
- Changing a member's 2-night stay to 4 nights: the discount stays at 10%, so KRW 180,000 should become KRW 360,000, without the discounts being combined (15%).
- Moving a non-member's 3-night stay into peak season: the discount disappears, so KRW 285,000 should become KRW 300,000.

### 4.3 State transitions of a booking

A booking moves between the states confirmed, cancelled, in-house, no-show and completed. Changing a confirmed booking keeps it confirmed and recalculates the rate; cancelling it moves it to cancelled, calculates the penalty and makes the room vacant. Along with allowed transitions, the tests check that invalid transitions, such as changing a cancelled booking, checking in a no-show or cancelling an in-house stay, are blocked.

### 4.4 Error guessing

Situations that are hard to systematise with techniques are covered by experience-based error guessing: pressing the cancel button twice in quick succession, two staff members changing or cancelling the same booking at the same time, and changing dates across the year end. These are scenes that actually happen at the front desk.

Based on this design, an AI agent drafted the test cases and the QA specialist verified them, completing 46 test cases including 24 representative ones. The verification points were whether all six penalty boundary values were present and whether penalties had been wrongly calculated on the pre-discount amount. For example, if a member's 3-night stay (KRW 270,000) is cancelled at D = 4, the penalty should be KRW 135,000, 50% of the post-discount amount.

## 5. Execution and defect management: a defect found at the boundary

Alongside test execution, a 60-minute exploratory testing session was run. It explored situations in which rates, penalties and room status could become tangled, such as changing the date of the same booking three times and then cancelling, or changing the room type and then changing it back. The session produced one low-severity display defect and two questions to confirm with the planner.

The most notable defect in the case was found at a penalty boundary. When a booking for one night in a deluxe room (KRW 100,000) with check-in on 20 November was cancelled on 14 November (D = 6), instead of the expected penalty of KRW 50,000 (50%), the screen showed a penalty of KRW 0 and a full refund. D = 7 and D = 3 worked correctly; only D = 6 was treated as free. This defect was presumed to be an error in handling the "within seven days" boundary.

The book points out that without boundary value analysis, for example if only a cancellation five days before had been tested, this defect would have gone into production as it was. In real operation, it would have meant lost revenue: no penalty collected from any guest cancelling six days before check-in.

The second defect came from discount recalculation after a change. When a non-member's 3-night stay (KRW 285,000) was changed to 2 nights, the 5% multi-night discount was kept, so KRW 190,000 was shown instead of KRW 200,000. Both defects were logged as "high" severity, and after the fixes the regression scope included all six penalty boundary values and no-show handling, the whole change decision table and the discount rules for creating bookings.

## 6. Completion report and process improvement

According to the completion report, all 46 test cases were executed: 44 passed and 2 failed, and the 2 failed cases passed on retesting after the defects were fixed. There were 2 high-severity defects (resolved), 1 medium (resolved) and 2 low (one deferred to the next release by agreement), and the QA specialist judged the function ready for release. Remaining risks recorded were the operational inconvenience for group bookings due to the lack of partial cancellation, and the need for separate integration testing of actual refunds with the payment gateway.

The final section of the report, "lessons learned", is the heart of this case. On the grounds that a rule directly tied to money, the basis amount for penalties, had been missing from the specification, it proposed adding that item to the specification review checklist for money-related functions. The book calls this "the moment testing becomes QA": not stopping at fixing the defects found this time, but improving the process so that the same gap does not appear in the next specification in the first place.

## 7. Implications

Three implications for hotel system quality assurance can be drawn from this case.

**First, boundaries involving money must be tested with boundary values.** Points where rules change, such as cancellation penalties, discounts and free-cancellation deadlines, are where developers' inequality-sign mistakes concentrate, and those defects lead directly to lost revenue or guest disputes.

**Second, frontline experience is most valuable at the planning stage.** Questions such as the basis amount for penalties, the distinction between no-shows and same-day cancellations, and partial cancellation of group bookings can be asked by people who know front desk and settlement work. This is why hotel IT organisations should involve people with operational experience in specification reviews.

**Third, AI agents write and people judge.** Throughout the case, the AI agent found ambiguous wording, drafted test case tables and organised report drafts, while people chose techniques, designed boundary values, checked amounts, decided severity and made the release decision. This division of roles can serve as a reference when designing quality assurance organisations in hotel IT as AI tools spread.
