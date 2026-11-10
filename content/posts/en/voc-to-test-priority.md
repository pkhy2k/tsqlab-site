---
title: "Customer Feedback (VOC) Shows Where the Next Test Should Look"
subtitle: Using VOC analysis, a long-standing service quality tool, to set priorities in software quality assurance
category: service-quality
author: research
thumbnail: /images/posts/en/voc-to-test-priority.jpg
thumbnail_alt: Illustration summarising the article
date: 2026-11-01
summary: Inquiries from guests and staff that accumulate in hotel systems are data showing where defects cluster. With an example, we show how to analyse VOC in five steps, organise, classify, count, interpret and apply, and link it to test priorities and product improvements.
tags: [VOC, Service Quality, Defect Clustering, Test Priorities, AI Agents]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 1장, 8장, 11장."
  - "ISTQB. Certified Tester Foundation Level (CTFL) Syllabus, v4.0.1."
---

In hotel management, the voice of the customer (VOC) is a basic resource for managing service quality. Collecting complaints and inquiries, finding their causes and fixing recurring problems are familiar tasks on the service front line. That the same data is also an important clue for software quality assurance has received relatively little attention.

Chapter 11 of Director Winston Park's book *Let's Do QA Together with AI Agents* (in Korean) treats VOC as "a treasure trove for testing". For a hotel system, inquiries left by front desk staff, cases logged by the customer service centre and incident reports are all VOC. These records show where real users run into inconvenience and where they encounter defects.

## Defects cluster

One of the seven testing principles set out by ISTQB is defect clustering: a large share of defects tends to concentrate in a small number of functions. The book compares this to hotels, where certain rooms attract complaints far more often than others. Functions with complex rules, such as settlement and discount calculations, are typical examples.

Time and people for testing are always limited. If every function cannot be examined in the same depth, the places where defects are most likely to cluster need closer attention. VOC lets you confirm that "where" with data rather than guesswork.

## Five steps of analysis

The book sets out VOC analysis in the following five steps.

1. **Organise**: Collect VOC for a set period and mask personal information.
2. **Classify**: Divide it by function (reservations, check-in, settlement and so on) and by type (suspected defect, how-to question, improvement request).
3. **Count**: Count the number of cases in each category, trends and recurring expressions.
4. **Interpret**: Find where cases are most frequent, where they are increasing and which are serious.
5. **Apply**: Reflect the findings in test priorities, checklists, the scope of regression testing and suggestions for product improvement.

## What 50 hypothetical VOC cases showed

The book presents an example analysis of 50 hypothetical VOC cases received by a hotel reservation system. By function, the results are as follows.

- Changes and cancellations: 9 suspected defects, 4 how-to questions and 3 improvement requests. This was the largest group, with repeated suspected defects related to refund amounts.
- Check-in: 5 suspected defects, 6 how-to questions and 2 improvement requests. Questions about group check-in were concentrated here.
- Settlement: 4 suspected defects, 2 how-to questions and 1 improvement request. Few cases, but high severity because money is involved.
- Reservations: 3 suspected defects, 5 how-to questions and 4 improvement requests. Many how-to questions make this a candidate for screen improvements.
- Other or undecided: 2 cases that need direct review.

In total there were 22 suspected defects, 17 how-to questions and 11 improvement requests, 50 cases in all. These results provide grounds for allocating more time to changes, cancellations and settlement in the next test cycle.

The reservations function deserves attention. Most inquiries here were how-to questions rather than defects. If users have to ask how to use a system even when it works as specified, that is a signal related to the principle that the absence of defects does not mean success, that is, whether what was built is what users actually wanted. The book treats passing this information on to the product planning team as part of QA's job.

> The place with the most cases and the place with the greatest harm can differ. There are only seven settlement cases, but money is at stake.

## What to leave to AI agents and what people must do

Classifying and counting dozens or hundreds of VOC cases is work an AI agent can handle quickly. The book shows how to ask an agent to classify VOC by function and type, count cases by function and find recurring defect patterns to suggest test ideas. Cases that are hard to classify are marked separately as "undecided".

At the same time, the book requires three checks: confirm that the counted totals match the original number of cases, pick a few cases at random and check the classification yourself, and have a person read the undecided cases directly. Counting is an area where AI easily makes mistakes, and unexpected defects sometimes hide among undecided cases. VOC text also tends to contain guests' names and contact details, so personal information should be masked within the company before anything is put into AI.

## Data that links service quality and system quality

VOC analysis is where service quality research and software quality assurance meet. From a service quality perspective, VOC is a record of the quality guests perceived; from a software quality perspective, it is evidence of defects surfacing in real use. If hotel organisations set up a structure in which operations and IT departments read guest complaint data together, they will be able to distinguish more accurately between problems to solve through staff training and problems to solve through system improvements.
