---
title: "A Guide to QA Work with AI Agents: What to Delegate and What to Judge"
subtitle: From the four elements of a prompt to dividing roles at each stage, practical guidance on AI-assisted quality assurance for hotel IT teams
category: column
author: director
thumbnail: /images/posts/en/report-ai-agent-qa-workflow.jpg
thumbnail_alt: Illustration summarising the article
cover: /images/posts/en/report-ai-agent-qa-workflow-cover.jpg
date: 2026-11-01
summary: AI agents are good at organising documents and spotting what is missing, but they do not run or judge systems. I set out what AI does well and what to be careful about, the four elements of a good prompt, how to refine results through conversation, and how to divide roles from requirements analysis to the completion report.
tags: [Columns, AI Agents, Prompts, Work Guide, Software QA, Hotel IT]
references:
  - "박건희 (2026). *이제 QA, AI Agent랑 같이 합시다*. 부크크. 8장, 12장, 13장."
---

As generative AI services have become everyday work tools, the way software quality assurance (QA) work is done is changing too. The time spent extracting test conditions from specifications, turning notes into defect reports and classifying accumulated customer inquiries has dropped sharply. But as the tools have become faster, the ability to judge whether their results are correct has become more important.

Based on Part 3 of my book *Let's Do QA Together with AI Agents* (in Korean), this article sets out practical guidance for hotel IT teams using AI agents in QA work. So as not to be tied to any particular product, the book explains things in terms of features most AI services share, and this article follows the same principle.

## 1. How to understand AI agents

The book compares an AI agent to "a senior colleague at the next desk". It knows a lot, never gets tired and can be asked anything at any time. But it does not know much about your company's circumstances, and it sometimes says wrong things with confidence. The starting point is to work with it while keeping both sides in mind.

### What AI agents do well

- **Reading and organising long documents**: Extracting test conditions from a specification dozens of pages long, summarising meeting minutes
- **Finding what is missing**: Pointing out ambiguous wording in requirements, boundary values missing from test cases
- **Generating varied ideas**: Error-guessing lists, exploratory testing ideas, variations of test data
- **Organising into tables and templates**: Test case tables, decision tables, defect report templates
- **Polishing sentences**: Turning notes about a defect into a standard report
- **Explaining unfamiliar things**: Error messages, logs, technical terms you have never seen

### What to be careful about

- **They do not actually run the system**: They cannot judge that a test has passed. Execution and judgement are done by people.
- **They do not know your internal rules**: If you do not tell them, they fill the gaps with guesses based on general rules.
- **They produce plausible wrong answers (hallucinations)**: They can describe functions or rules that do not exist as if they were facts.
- **They make mistakes in calculation and counting**: Amounts and numbers of combinations can be wrong.
- **Their answers vary slightly each time**: The same question can produce different results, so reproducibility is low.

## 2. The four elements of a good prompt

The book compares two prompts to show how much the result of the same request depends on how you ask. Ask "Make test cases for the booking function", and the AI agent imagines a generic booking system and produces a plausible list. Ask with the following four elements, and you get verifiable results that fit your rules.

- **Role**: The perspective to answer from. For example, a QA engineer with long experience testing hotel reservation systems
- **Context**: Your situation, which the AI does not know. For example, maximum occupancy by room type (standard 2, deluxe 3, suite 4), allowed length of stay (1 to 14 nights) and the screen currently under test
- **Task**: Exactly what to do. For example, create test cases for the number of guests and nights using equivalence partitioning and two-value boundary value analysis, with only one invalid value per test
- **Format**: The shape you want the result in. For example, a table of "TC number / technique / input / expected result", followed by a list of partitions and boundary values

The book stresses that context is the most important of these. If the result looks wrong, first check whether you gave enough context. Differences in results come not from the AI agent's ability but from the quality of the question.

The book also offers tips for better results: show an example of the output you want, break the task into steps, have the AI leave a "needs checking" list instead of guessing when information is missing, have it ask for the information it needs before starting, and refine the result over a conversation rather than expecting a perfect answer at once. The single sentence "If information is missing, do not guess" in particular greatly reduces hallucinations and is used in every exercise in Part 3 of the book.

## 3. Refining through conversation: three requests

The book shows an example of refining test cases for the number of guests in a deluxe room over three exchanges.

1. In the **first request**, asking for test cases without context, the AI agent judged that four guests could be booked. It did not know the rule that a deluxe room holds at most three. The boundary values of zero and three were also missing.
2. In the **second request**, after being told the maximum of three and the techniques to use, the partitions (0 or less invalid, 1 to 3 valid, 4 or more invalid) and boundary values (0, 1, 3, 4) were reflected correctly. The error message wording, however, might differ from the specification.
3. In the **third request**, the error messages were aligned with the specification wording and the table format was specified, completing the result.

The result improved because each time a person spotted what was wrong and gave a precise instruction. The book concludes that the ability to use AI agents well is ultimately the ability to verify their results.

## 4. Dividing roles at each stage

The comprehensive exercise in Chapter 12 of the book divides the roles of AI agents and people across an entire QA project for a booking change and cancellation function as follows.

- **Requirements analysis**: The AI finds candidate ambiguities and omissions. People add questions from a frontline perspective, finalise the list of questions and communicate with the planner.
- **Planning**: The AI drafts the wording of the plan. People decide the scope, risk priorities and exit criteria.
- **Design**: The AI writes test case tables and files and suggests additional ideas. People choose techniques, design boundary values and check amounts.
- **Execution and defects**: The AI drafts reports, interprets logs and suggests regression test candidates. People execute, judge results, confirm reproduction and decide severity.
- **Completion**: The AI summarises metrics and drafts the report. People decide on release, assess remaining risks and propose improvements.

There is a consistent principle in this division. AI agents handle **writing and organising**; people handle **choosing, judging and taking responsibility**. What to test, whether the results are right and whether to release are decided by people to the end.

## 5. Verification habits and data protection

Everything an AI agent produces is a draft. The book presents these verification habits: compare with the original, calculate numbers yourself, use test techniques to find what is missing, ask for the basis, ask again in a different way, and leave the final judgement to a person.

Data protection is given the same weight. Check your company's AI usage policy first, and do not enter, or mask, customers' personal information, sensitive identifiers, authentication details and company secrets. Pseudonymisation should be done inside the company first, not left to the AI, because the information has already been passed on the moment the original is entered. This principle is especially important in the hotel industry, which handles customer information in large volumes.

## 6. Adoption guidelines for hotel IT teams

Based on the above, here are guidelines for hotel IT teams introducing AI agents into QA work. This section is the Lab's extension of the book's content to the organisational level.

1. **Set an AI usage policy first.** Document which services and accounts are allowed, what information may be entered and the procedure for pseudonymisation.
2. **Manage shared context as an asset.** Organise context such as maximum occupancy by room type, stay rules, discount and penalty rules and test case templates, and manage them as prompts and reference material the team shares. The book introduces how to use the project features many AI services provide.
3. **Build verification into the process.** Have test cases created by AI registered only after the person in charge compares them with values derived directly using test techniques. In the book's field example, this comparison took no more than ten minutes and greatly reduced comments in reviews.
4. **Make clear who judges and who is responsible.** Decisions on whether something is a defect, its severity and whether to release are made and recorded by people.

The book argues that the better AI gets at writing drafts, the more valuable the people who can judge those drafts become. Whether AI agents are introduced successfully depends less on the performance of the tool than on how well the organisation has the people and procedures to verify its results.
