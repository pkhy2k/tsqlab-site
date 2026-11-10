---
title: "Testing Is Asking Questions"
subtitle: Good test techniques, and good use of AI, both come down to the skill of asking good questions
category: column
author: director
thumbnail: /images/posts/en/column-testing-is-asking.jpg
thumbnail_alt: Illustration summarising the article
cover: /images/posts/en/column-testing-is-asking-cover.jpg
date: 2026-11-01
summary: Equivalence partitioning, boundary value analysis, decision tables and state transitions can each be summed up as a single question. What prevented a double booking of Room 703 was also one question asked in a meeting room. I reread test techniques and the use of AI from the perspective of questions.
tags: [Columns, Director's Column, Test Techniques, AI Agents, Software QA]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 1장, 에필로그."
---

Imagine that on a Saturday afternoon at a hotel front desk, two bookings are assigned to the same room on the same night. A family on the second night of a two-night stay and a business traveller who has just checked in are both standing there holding keys to Room 703. My book *Let's Do QA Together with AI Agents* (in Korean) opens with this hypothetical scene.

Tracing the cause, it turned out that the specification contained only the word "nights" and never defined up to which night a guest uses the room. The developer miscalculated the last night, and the defect only revealed itself on a peak-season weekend when the hotel was full.

At the end of the book, I wrote what happened afterwards. From that day on, the hotel's team began inviting a tester whenever they wrote a specification. In a meeting, the tester asked: "When is the last night for a two-night guest? How do we count nights?" That one question prevented the next Room 703.

## Techniques are another name for questions

Looking back as I finished the book, what I had covered from start to finish was, in the end, how to ask questions.

- **Equivalence partitioning** is the question "Will these values be treated the same way?"
- **Boundary value analysis** is the question "What happens exactly at the boundary?"
- **Decision tables** are the question "What if these conditions overlap?"
- **State transitions** are the question "What happens if I do this in the current state?"
- **Risk analysis** is the question "What would hurt the most?"
- **A defect report** is the question "How can anyone see this problem?"

People learning test techniques for the first time are often overwhelmed by terms and formulas. But the essence of a technique is not the formula; it is the question. The formula is just a tool that helps you ask that question thoroughly and repeatably.

## The front line is the raw material for questions

Anyone who has worked in a hotel will be familiar with questions like these. If a member also gets a multi-night discount, what is the total discount? Is a guest who arrives at exactly 3 p.m., the check-in time, an early check-in? How are nights counted for a booking that comes in after midnight? Is a stay from 31 December to 1 January calculated correctly?

All of these questions come from the front desk, reservations and settlement. You can ask them without knowing code, and people who know the front line can ask them even more sharply. Without a technical degree or coding skills, the workplaces you have worked in, the systems you have used and the people you have met all become raw material for questions.

## The second question in the age of AI

Working with AI agents is also a skill of asking questions. The first question is asking with good context. If you do not tell the AI your hotel's maximum occupancy by room type, its stay rules and its discount policies, it will fill the gaps with plausible guesses.

Then there is the second question: asking "Really?" of the answer that comes back. Does this test case include all the boundary values? Is this amount calculated correctly? Is this rule really in our specification?

However far AI advances, I believe this second question will remain a human job. The better AI gets at writing first drafts, the more valuable the people who know how to ask "Really?" of those drafts become.

## An organisation that asks questions

What the Room 703 case shows is not only an individual's ability to ask questions but the importance of a structure in which questions can flow. Inviting testers to planning meetings, asking about defects not "Whose fault is it?" but "Where did it come from?", and making quality the responsibility of the whole team rather than a single tester. When such a structure exists, questions from the front line get answered before they become defects.

Whether in a hotel or an IT company, organisations that create good services welcome questions. Testing, in the end, is the work of asking those questions systematically.
