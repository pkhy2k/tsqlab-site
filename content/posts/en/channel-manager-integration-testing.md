---
title: "Channel Manager Integration Testing: Room Inventory Goes Wrong Between Systems"
subtitle: Defects that arise at the interfaces linking the PMS and sales channels, and the perspective of integration testing
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/channel-manager-integration-testing.jpg
thumbnail_alt: Diagram of inventory, rate and booking messages moving between a PMS, a channel manager and several online sales channels, marking where delays, duplicates and out-of-order messages occur
date: 2026-11-02
summary: A hotel's room inventory and rates are kept in line as they move between the PMS, the channel manager and several online sales channels. We explain why defects arise between systems even when each one works correctly, and set out the perspectives to check in integration testing.
tags: [Hotel IT, Software QA, Integration Testing, Channel Manager, Interfaces, Overbooking]
references:
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

Hotel rooms are not sold in just one place. The booking engine on the hotel's own website, several online travel agencies (OTAs) and contracted travel agency rates all look at the same inventory at the same time. The channel manager's role is to distribute this inventory and these rates to the various channels and pass incoming bookings to the property management system (PMS). Overbooking, where the last remaining room is sold on two channels at once, usually arises not in any one system but between systems.

## Each works correctly, yet together they go wrong

The PMS calculates inventory accurately, the channel manager passes on the values it receives accurately, and the OTA sells as much inventory as it receives. Even if all three systems pass their own tests, problems remain, because information takes time to travel, and other sales happen in the meantime.

The International Software Testing Qualifications Board (ISTQB) CTFL syllabus divides integration testing, one of the test levels, into two kinds: component integration testing, which looks at the components within one system, and system integration testing, which looks at the interfaces between different systems or external services. Channel integration is a typical target of system integration testing. It is all the more difficult because the hotel cannot control the external systems, and test environments are often hard to obtain.

## Types of defects that arise at interfaces

Situations worth checking in channel integration can be grouped by how messages travel.

- **Latency**: The few seconds to minutes when inventory has reached 0 in the PMS but still shows 1 on the OTA. A booking that comes in during this window becomes an overbooking.
- **Duplication**: A system that receives no response sends the same booking again. If the receiving side does not recognise it as the same booking, two bookings are created. You need to check idempotency: receiving the same request several times should have the same result as processing it once.
- **Out-of-order**: A booking change message arrives before the original booking, or a cancellation is processed before a change.
- **Partial failure**: A rate is applied on four of five channels and fails on only one. If the failure is silently buried, one channel sells at a different rate.
- **Mapping**: Room type codes, rate codes, occupancy bases and the notation for dates and time zones differ between systems. Time zone issues are covered in detail in [Why Hotel Systems So Often Get Dates Wrong](/posts/hotel-dates-test-design/).

These defects do not show up with a single normal booking. You only see them by deliberately creating situations where things happen at the same time, late, twice or in reverse order.

## What to test, and how

The Editorial Team proposes the following perspectives for testing channel integration.

1. **Sell the last room at the same time**: With one room left in inventory, put in bookings from two channels almost simultaneously and check how the system handles them. Whether staff can tell immediately when an overbooking occurs is also something to check.
2. **Send the same message twice**: Repeatedly send identical booking, change and cancellation messages and see that bookings are not duplicated.
3. **Disconnect and reconnect**: When the channel manager or network stops briefly and then recovers, check that queued messages are processed in the right order and that nothing is missing.
4. **See whether failures are reported**: Check that the system retries when a transmission fails and, if it ultimately fails, records it and notifies the person in charge. Silent failure is the most dangerous kind.
5. **Treat reconciliation as a function**: If there is a function that periodically compares the PMS's inventory and rates with the values actually posted on each channel, the accuracy of that comparison itself is also something to test.

It is impossible to test every channel and every combination. It is realistic to start where failure has the greatest impact: channels with a large share of sales, peak seasons with little inventory, and periods of frequent rate changes. How to set these priorities is set out in [What to Test First: Risk-Based Testing for Hotel Systems](/posts/report-risk-based-testing-hotel/).

> The question in integration testing is not "Was it sent?" but "Has the receiving side reached the same state?"

## Defects surface at the front desk

The consequences of interface defects ultimately appear at the check-in counter: guests whose bookings cannot be found, two bookings assigned to the same room on the same day, and inquiries from guests who saw different rates on different channels. How a double assignment spreads to the guest experience and revenue is also examined in [Errors, Defects and Failures Through the Double Booking of Room 703](/posts/room-703-error-defect-failure/).

## Closing

The quality of channel integration is hard to assign to any single vendor. That is why it is important for hotels and solution vendors to agree together to treat the "space between systems" as a test target, and to agree in advance on the expected behaviour when delays, duplicates and failures occur. Guests see neither the PMS nor the channel manager. All they see is one thing: whether the room they booked is there.
