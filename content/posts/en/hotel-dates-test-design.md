---
title: "Why Hotel Systems So Often Get Dates Wrong"
subtitle: Where the business date, nights of stay and local time diverge, and how to test those boundaries
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/hotel-dates-test-design.jpg
thumbnail_alt: Timeline showing the calendar date and the hotel business date diverging between midnight and the night audit
date: 2026-11-02
summary: Many defects in hotel systems come from dates. The calendar date differs from the hotel's business date, stays are counted in nights, and each booking channel uses a different time zone. We set out the date concepts in hotel operations and propose test perspectives to check at their boundaries.
tags: [Hotel IT, Software QA, Test Design, Boundary Value Analysis, Night Audit, PMS]
references:
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

Collect defect reports from hotel systems and an unusually large share relate to dates. Rates are applied a day late, check-ins of guests arriving after midnight are not processed, or month-end revenue spills into the next month. These are often less a matter of developer mistakes than of the date concepts used in hotel operations differing from ordinary calendar dates.

This article sets out the typical points where dates diverge in hotel systems and proposes how to test those boundaries. It is based on concepts commonly used across hotel operations rather than the behaviour of any particular product; actual rules differ between hotels and systems, so check them against your own specifications.

## 1. The calendar date and the business date are different

Hotels do not close the day at midnight. Most hotels run a night audit to close the day's business overnight, and only when it finishes does the system's business date move to the next day. The closing time differs between hotels, and some run it at 2 or 3 a.m.

As a result, for a few hours between midnight and closing, the calendar says 2 November while the system's business date is still 1 November. What happens during these hours is a major source of date defects.

- Which date's booking does the check-in of a guest arriving at 1 a.m. count against?
- Which business day's revenue do minibar or room service charges incurred in this window count towards?
- Do channels such as kiosks or mobile check-in, where the system works off the calendar time, use the same basis as the business date?

The last item becomes more important as channels multiply. The PMS works off the business date, but if a connected external system judges by the server's calendar date, the two systems see the same booking for the same guest on different dates.

## 2. Stays are counted in nights

A hotel stay is counted as the number of nights from the check-in date up to the day before the check-out date. Check in on 1 November and check out on 3 November and it is two nights, with rates applied to the nights of 1 and 2 November. This seems obvious, but whether code that handles dates includes the end date or not is one of the most common mistakes.

- When rates differ by date (weekday and weekend, the start of peak season), is the check-out date's rate wrongly applied?
- In rules that depend on the number of nights, such as multi-night discounts, is the count off by one?
- When a booking change moves the dates of a stay, are rates for nights already passed recalculated?

It is usual to apply the rate for the date of the stay, not the date the booking was made. A December stay booked in October should get December's rate. Defects that confuse the booking date with the stay date often surface just before peak season, when rates change frequently.

## 3. The same moment differs depending on where you look from

Connecting with overseas online travel agencies (OTAs) or channel managers brings time zone issues. If an external system sends times in Coordinated Universal Time (UTC) and the hotel system does not convert them to Korean time, there is a nine-hour gap. A booking made before 9 a.m. Korean time is the previous day in UTC.

At cancellation deadlines this becomes a money issue. In a policy of "free cancellation until 6 p.m. three days before check-in", is 6 p.m. the hotel's local time, the guest's local time or the server's time? If this basis differs between systems for international bookings, the same cancellation is free on one side and subject to a penalty on the other. Testing cancellation policies and penalty calculations is covered in detail in [A QA Case Study of Hotel Booking Changes and Cancellations](/posts/report-cancellation-qa-case/).

## 4. When the month and year change

Month end and year end are when revenue totals, settlements and statistics are cut off. A multi-night booking that checks in at the end of one month and checks out in the next must have its revenue split across two months. At year end, booking number schemes, receipt numbers and annual cumulative statistics may reset with the change of year, and this processing must be checked for accuracy.

Leap years are also easy to miss. In a year with 29 February, the number of nights in February, statistics compared with the same date a year earlier, and period calculations such as "within one year" must behave differently from ordinary years. The next leap year is 2028.

## Test design: turn the boundaries into a list

Most date defects arise at boundaries. Applying boundary value analysis to dates, you can list the moments to test in advance. The following is the date boundary list the Editorial Team proposes.

1. Just before and after midnight (23:59, 00:00, 00:01)
2. Just before and after the night audit, and while it is running
3. Just before, exactly at and just after the cancellation deadline
4. The night before and the night of a rate change
5. Month-end check-in with next-month check-out, and year-end check-in with next-year check-out
6. 28 February, 29 February and 1 March
7. Bookings from external channels made before 9 a.m. Korean time

To test these moments, you need a test environment in which the system time can be changed to the point you want. Waiting for real dates to arrive means month-end or leap-year defects cannot be found before release. Whether the time can be adjusted in the test environment should be agreed with the development team at the test planning stage.

Anyone who has worked at a front desk knows how often guests arriving after midnight, month-end closing and settlement for multi-night guests cause problems. That experience is itself a set of test conditions. How to turn front-line instincts into test design is also covered in [When the Front Desk's "What If?" Becomes a Test Case](/posts/service-sense-to-test-design/).
