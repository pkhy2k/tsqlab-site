---
title: "When the PMS Connects to AI Assistants: The Spread of MCP and the Challenge of Permissions"
subtitle: The current state of AI agents in hotel operations through Apaleo, roommaster and an h2c survey
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/pms-mcp-ai-assistant-governance-2026.jpg
thumbnail_alt: Diagram showing a property management system (PMS) connecting to several AI assistants through MCP, with permissions, logging and designated owners placed between them
date: 2026-11-04
summary: The MCP approach, which connects hotel property management systems (PMS) directly to AI assistants, is spreading quickly. We review the cases of Apaleo and roommaster and an industry survey, and the questions of permissions and accountability hotels must settle before AI reads and changes booking data.
tags: [Hotel IT Solutions, PMS, MCP, AI Agents, Data Governance, Personal Data]
references:
  - "Hospitality Net (2026.10.28). Hotels are putting AI agents to work in live operations, with Apaleo MCP Server use up 70%. https://www.hospitalitynet.org/news/4135158/hotels-are-putting-ai-agents-to-work-in-live-operations-with-apaleo-mcp-server-use-up-70"
  - "Hotel Tech Report (2026.10). Hotels are putting AI agents to work in live operations, with Apaleo MCP Server use up 70%. https://hoteltechreport.com/news/hotels-are-putting-ai-agents-to-work-in-live-operations-with-apaleo-mcp-server-use-up-70"
  - "Hospitality Net (2026.10.19). roommaster Introduces AI Connector, Bringing Live Hotel PMS Data into ChatGPT, Claude, Microsoft Copilot and Google Gemini. https://www.hospitalitynet.org/news/4134994/roommaster-introduces-ai-connector-bringing-live-hotel-pms-data-into-chatgpt-claude-microsoft-copilot-and-google-gemini"
  - "roommaster (2026.10.19). Introducing roommaster AI Connector: Now Your AI Assistant Knows Your Hotel. https://www.roommaster.com/news/introducing-roommaster-ai-connector-now-your-ai-assistant-knows-your-hotel"
  - "Hospitality Net (2026.10.27). HN Brief: Is ARI Plumbing the Main Obstacle to Agentic AI?, Seven Components for Hotel Agent Governance. https://www.hospitalitynet.org/editorial/4135138/is-ari-plumbing-the-main-obstacle-to-agentic-ai-seven-components-for-hotel-agent-governance-hvs-broad-revpar-recovery-sets-an-elevated-base-for-2027"
---

Hotel staff asking an AI assistant "Which guests arriving today have outstanding balances?" instead of running a report is becoming reality. What makes this possible is MCP (Model Context Protocol), an open standard that lets AI assistants exchange data with external systems in a defined way, and hotel property management system (PMS) vendors have been adopting it one after another. This article reviews recent cases and surveys, and looks at the issues hotels must settle first when AI reads and changes booking data.

## Usage is rising fast

According to Apaleo's announcement of 28 October 2026, reported by Hospitality Net and Hotel Tech Report, usage of the MCP server the company launched in September 2025, the first in the PMS sector, grew 70% from July to September 2026. Month by month, usage rose 23% from July to August and 38% from August to September, an accelerating pace. These are relative figures given by the company; absolute usage was not disclosed.

Most use cases in the announcement automate repetitive work. One serviced apartment operator modified about 2,000 bookings at once, saving about 50 hours of work, and one hotel group saved about two hours a week by identifying bookings eligible for upgrades every day. Other cases included building demand forecasts from last year's results and turning existing rate tables into rate plans.

US PMS vendor roommaster also announced an MCP-based connection tool on 19 October. Hotels can query arrivals and departures, outstanding balances and room inventory in everyday language from ChatGPT, Claude, Microsoft Copilot and Google Gemini. The company said the connection is not switched on automatically and must be approved by the hotel, that the scope of queries follows user permissions, and that conversations are subject to each AI service's terms and data processing policies.

## Use is growing, but trust is flat

Apaleo's announcement also cited results from h2c's *Hotel Chain Tech Report 2026*. Ninety-one percent of hotel chains use AI, up from 78% a year earlier, but only 15% have a standardised AI data connection layer such as MCP, and 52% have no plans to adopt one. Reliance on AI rose from 4.7 to 5.4 out of 10, while trust stayed at 6.5. Sixty percent of everyday AI use was through external tools such as ChatGPT, and 27% through AI built into vendor systems. These figures are cited indirectly through a press release, so the survey methods should be checked in the original report.

These results show that staff already use external AI tools at work, but how those tools are connected and used has not yet been put in order.

## Settle permissions and accountability first

In a Hospitality Net briefing on 27 October, Burcin Turkkan Zencirli presented seven components of hotel AI agent governance: identity, permissions, human control, data access, traceability, management of external agents, and accountability. She pointed out that in hotels, authority is split among individual properties, operators, brands, owners and vendors, so the fact that an agent can access a system does not mean all its actions are approved. Citing a 2024 Canadian case in which an airline was held responsible for its website chatbot's advice (Moffatt v. Air Canada), she argued that an owner must be designated for each automated task.

Based on this discussion, the editorial team suggests checking the following.

- **Separate reading from writing**: Start with queries, and open permissions that change data, such as modifying bookings or changing rates, step by step for each task.
- **Follow the permissions of human accounts**: Agents should not act with separate administrator rights but only within the permissions of the staff member who instructed them.
- **Keep logs and designate owners**: It must be possible to trace who changed what under which instruction, and an owner should be assigned for each automated task.
- **Verify bulk changes in advance**: Being able to change 2,000 bookings at once means a wrong instruction is also applied to 2,000 bookings at once. Check the results on a sample of bookings before applying changes to all of them.
- **Check where guest data goes**: When guest information is passed to an external AI service, Korean law requires a review of whether this counts as entrusted processing or a cross-border transfer of personal data. Detailed standards need to be checked against the law and with experts; the basic principles are summarised in [What to check before putting hotel guest data into AI](/posts/hotel-data-ai-agent/) (in Korean).

## Conclusion

MCP is turning the PMS from a system staff go into and search, into a system they ask and delegate to through AI. As repetitive work decreases, staff can spend more time with guests. Those benefits, however, can be gained safely only by hotels that first put in place the basic safeguards of permissions, logging and accountability. The pace of governance, more than the pace of technology, will decide success.
