---
title: "The Seven Principles of Software Testing, Read Through a Housekeeping Checklist"
subtitle: Inspecting rooms and testing software have more in common than you might think
category: column
author: director
thumbnail: /images/posts/en/column-housekeeping-seven-principles.jpg
thumbnail_alt: Illustration summarising the article
cover: /images/posts/en/column-housekeeping-seven-principles-cover.jpg
date: 2026-11-01
summary: I reread ISTQB's seven principles of software testing in the language of hotel operations, from room inspections and problem rooms to the different standards of five-star and business hotels. The principles of managing quality travel across industries.
tags: [Columns, Director's Column, Testing Principles, ISTQB, Service Quality, Housekeeping]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 1장."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

The International Software Testing Qualifications Board (ISTQB) has distilled decades of testing experience into seven principles. They come up often in certification exams, but they matter more as standards to rely on when your judgement wavers in practice.

When I moved from hotels to an IT company and first studied these principles, they felt familiar rather than strange. I had already experienced most of them in hotels. In my book *Let's Do QA Together with AI Agents* (in Korean), I explained these principles through hotel stories. Here I revisit them from the perspective of housekeeping and room management.

## Principle 1. Testing shows the presence of defects, not their absence

If a housekeeper inspects ten rooms and finds no problems, that does not mean every room in the hotel is perfect. Testing is the same. Passing many tests means few defects were found, not that there are none. That is why a tester should not say "There are no bugs" but "I found no problems within this scope". Honest reporting begins with modest wording.

## Principle 2. Exhaustive testing is impossible

Combine stays of 1 to 14 nights, 1 to 4 guests, three room types, member or non-member, and all 365 days of the year, and you get 14 × 4 × 3 × 2 × 365 = 122,640 combinations. Trying them all is impossible, just as a housekeeping manager does not open every drawer in every room every day. What is needed is the skill of choosing what to check first and how much. Test techniques are exactly that skill of choosing.

## Principle 3. Early testing saves time and money

If you correct the position of a power socket at the drawing stage of a room renovation, you only need to change one line. After construction, you have to tear down the wall; after guests have stayed, you add apologies and compensation. Software is the same: the later a defect is found, the more it costs to fix. That is why reviews at the specification stage matter.

## Principle 4. Defects cluster together

Every hotel has rooms that attract complaints far more often than others: rooms with old plumbing, rooms next to the lift that are noisy, rooms whose windows do not close properly. Software defects also tend to concentrate in certain functions, typically those with complex rules such as settlement and discount calculations. It is efficient to look more closely at areas that had many defects in the past and areas that generate many customer inquiries.

## Principle 5. Tests wear out

If you inspect rooms in the same order every day, you end up looking only where you always look. Beds and bathrooms are checked carefully, but nobody has looked at the dust on top of the curtain rail for months. Likewise, repeating the same test cases makes it hard to find new defects. Test cases need to be revised regularly, with new data and perspectives added. This principle used to be called the "pesticide paradox", after the way insects develop resistance when the same pesticide is sprayed again and again.

## Principle 6. Testing depends on context

A five-star hotel and a business hotel cannot use the same room inspection standards. Testing is no different: a settlement function that handles payments and a notice board call for different depths and methods of testing. The starting point is not memorising one right answer but asking, "What matters in this situation?"

## Principle 7. The absence of defects is not success

Suppose you built a reservation system that works perfectly without a single bug, but front desk staff have to go through ten screens to make one booking. Nobody would want to use it. Finding and fixing defects is not enough; you also need to check that you built what users actually want. Even if a room has been cleaned perfectly to standard, if what the guest wanted was a quiet room, it is not a good room for that guest.

## The principles of quality travel across industries

Translating the seven principles into the language of hotels shows that software testing is by no means the exclusive domain of developers. Checking quality, setting priorities with limited resources and fixing processes so that the same mistakes do not recur happen every day in housekeeping, at the front desk and in settlement.

If service quality research deals with the quality customers perceive, software testing deals with the quality of the systems that support it. The fact that the principles of the two fields are so alike shows that what hotel people need to talk about system quality is not entirely new knowledge, but a language to carry over the experience they already have.
