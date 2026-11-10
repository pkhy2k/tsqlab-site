---
title: "What to Check Before Putting Hotel Guest Data into AI"
subtitle: Pseudonymisation principles and result-checking habits for hotel IT teams using AI agents at work
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/hotel-data-ai-agent.jpg
thumbnail_alt: Illustration summarising the article
date: 2026-11-01
summary: Hotels are a classic data-intensive industry, handling names, contact details, passport numbers and even card information. We set out what not to enter when using AI agents in quality assurance work, the pseudonymisation to do inside the company first, and the habit of treating AI output as a draft and verifying it.
tags: [AI Agents, Personal Data, Pseudonymisation, Data Security, Hotel IT, Software QA]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 8장, 13장."
---

Hotels are among the service industries that handle the most personal data. A single booking contains a guest's name and contact details; for international guests, passport information is added, and if payment has been made, card information follows. Guest inquiry records and system logs are also mixed with this kind of information.

As more hotel IT teams use AI agents at work, a new question has arisen: when analysing guest inquiries or organising defect logs, can this data be put into AI as it is? Chapter 8 of Director Winston Park's book *Let's Do QA Together with AI Agents* (in Korean) offers practical answers to this question.

## The first standard is your company's AI usage policy

The first principle the book stresses is the company's AI usage policy. Depending on the company, external AI services may be banned, only business accounts contracted by the company may be allowed, or the range of information that can be entered may be defined. If there is no policy, the first step is to ask a manager. You should also check the data settings of the account you use, for example whether conversations are used to improve the service, based on official guidance.

Even where the policy allows use, some information should not be entered or must be masked. The book groups it into four categories.

- **Customer personal information**: Names, phone numbers, email addresses, home addresses, dates of birth
- **Sensitive identifiers**: Passport numbers, ID numbers, card numbers, bank account numbers
- **Authentication information**: Passwords, access keys, internal server addresses
- **Company confidential information**: Contract terms, unpublished rate policies, source code whose use is prohibited by policy

## Mask data inside the company first

If you want to analyse guest inquiries, mask the personal information before entering it. For example, an original text such as "Guest Kim ○○ (phone number) requested cancellation of a booking for Room 703" becomes "Guest A (contact deleted) requested cancellation of a booking for Room X". Sentences containing booking numbers and the last digits of cards are changed to arbitrary numbers, with card information deleted. Email addresses in logs are replaced with "[email]".

Here the book points out a commonly missed trap: pseudonymisation itself should not be left to the AI agent. To ask it to "mask the personal information", you must first enter the original, and at that moment the information has already been passed to an external service. Pseudonymisation should be done inside the company first, with find-and-replace in a spreadsheet or internal tools.

> What analysis needs is not "who" but "what problem, and how often". Masking hardly reduces the quality of analysis.

## Everything AI produces is a draft

Entering data safely is not the end. The book asks that test cases, defect reports and analysis results produced by AI agents all be treated as drafts, and presents the following verification habits.

- **Compare with the original**: Check that the conditions the AI summarised actually appear in the original specification.
- **Calculate numbers yourself**: Recalculate amounts, discount rates, counts and coverage.
- **Look for what is missing**: Check that all boundary values and rules derived with test techniques are included.
- **Ask for the basis**: Ask, "Where in the specification is this expected result based?"
- **Ask again differently**: Request the same task in different wording and compare the results.
- **People make the final call**: The team decides on release, severity and whether something is a defect.

The book also lists warning signs in answers: plausibly citing regulation clauses that do not exist, speaking in generalities as if it knew your company's rules, giving results without showing calculations, and calculating dates and days of the week. In a field example in the book, a tester two months into the job registered 30 test cases created with an AI agent without reviewing them, and a senior colleague's review pointed out that they assumed a maximum occupancy of two for every room. After that, the tester made a habit of first comparing AI output with values he had derived himself using test techniques.

## What remains for people in the age of AI

Chapter 13 of the book predicts that AI will get steadily better at drafting test cases, organising defect reports and summarising logs. That does not mean the human role shrinks. Deciding what to test, imagining the front line, verifying AI output, communicating with people, and the responsibility of saying "It can be released" and giving the reasons remain human work. The book argues that the better AI gets at writing drafts, the more valuable the people who can judge those drafts become.

From the hotel industry's perspective, protecting guests' personal data is part of service quality before it is a legal obligation. Guests expect their information to be handled safely just as much as they expect clean rooms and friendly staff. Setting principles for handling data within the organisation must go hand in hand with the pace of AI adoption.
