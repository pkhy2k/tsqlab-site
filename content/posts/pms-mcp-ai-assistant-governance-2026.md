---
title: PMS가 AI 비서와 연결될 때, MCP 확산과 권한 관리의 과제
subtitle: 아팔레오와 룸마스터의 사례, h2c 조사로 본 호텔 운영 AI 에이전트의 현재
category: hotel-it-qa
author: research
thumbnail: /images/posts/pms-mcp-ai-assistant-governance-2026.jpg
thumbnail_alt: 객실관리시스템(PMS)이 MCP를 통해 여러 AI 비서와 연결되고, 그 사이에 권한, 기록, 책임자 지정이 놓이는 구조를 보여 주는 도식
date: 2026-11-04
summary: 호텔 객실관리시스템(PMS)을 AI 비서와 직접 연결하는 MCP 방식이 빠르게 퍼지고 있다. 아팔레오와 룸마스터의 사례와 업계 조사를 정리하고, AI가 예약 데이터를 읽고 바꾸게 될 때 호텔이 먼저 정해야 할 권한과 책임의 문제를 살펴본다.
tags: [호텔IT솔루션, PMS, MCP, AI에이전트, 데이터거버넌스, 개인정보]
references:
  - "Hospitality Net (2026.10.28). Hotels are putting AI agents to work in live operations, with Apaleo MCP Server use up 70%. https://www.hospitalitynet.org/news/4135158/hotels-are-putting-ai-agents-to-work-in-live-operations-with-apaleo-mcp-server-use-up-70"
  - "Hotel Tech Report (2026.10). Hotels are putting AI agents to work in live operations, with Apaleo MCP Server use up 70%. https://hoteltechreport.com/news/hotels-are-putting-ai-agents-to-work-in-live-operations-with-apaleo-mcp-server-use-up-70"
  - "Hospitality Net (2026.10.19). roommaster Introduces AI Connector, Bringing Live Hotel PMS Data into ChatGPT, Claude, Microsoft Copilot and Google Gemini. https://www.hospitalitynet.org/news/4134994/roommaster-introduces-ai-connector-bringing-live-hotel-pms-data-into-chatgpt-claude-microsoft-copilot-and-google-gemini"
  - "roommaster (2026.10.19). Introducing roommaster AI Connector: Now Your AI Assistant Knows Your Hotel. https://www.roommaster.com/news/introducing-roommaster-ai-connector-now-your-ai-assistant-knows-your-hotel"
  - "Hospitality Net (2026.10.27). HN Brief: Is ARI Plumbing the Main Obstacle to Agentic AI?, Seven Components for Hotel Agent Governance. https://www.hospitalitynet.org/editorial/4135138/is-ari-plumbing-the-main-obstacle-to-agentic-ai-seven-components-for-hotel-agent-governance-hvs-broad-revpar-recovery-sets-an-elevated-base-for-2027"
---

호텔 직원이 보고서를 뽑는 대신 AI 비서에게 "오늘 도착 예정 고객 중 미수금이 있는 사람은?"이라고 묻는 방식이 현실이 되고 있다. 이를 가능하게 하는 것이 MCP(Model Context Protocol)이다. MCP는 AI 비서가 외부 시스템과 정해진 방식으로 데이터를 주고받도록 하는 공개 표준으로, 최근 호텔 객실관리시스템(PMS, Property Management System) 공급사들이 잇따라 도입하고 있다. 이 글은 최근 사례와 조사를 정리하고, AI가 예약 데이터를 읽고 바꾸게 될 때 호텔이 먼저 정해야 할 문제를 살펴본다.

## 사용량이 빠르게 늘고 있다

Hospitality Net과 Hotel Tech Report가 전한 아팔레오(Apaleo)의 발표(2026년 10월 28일)에 따르면, 이 회사가 2025년 9월 PMS 분야에서 처음 내놓은 MCP 서버의 사용량은 2026년 7월부터 9월까지 70% 늘었다. 월별로는 7월에서 8월 사이 23%, 8월에서 9월 사이 38% 늘어 증가 속도가 빨라졌다. 다만 이는 회사가 밝힌 상대 수치이며, 절대 사용량은 공개되지 않았다.

발표에 소개된 활용 사례는 대부분 반복 업무의 자동화이다. 한 서비스드 아파트 운영사는 예약 약 2,000건을 한 번에 수정해 약 50시간 분량의 작업을 줄였고, 한 호텔 그룹은 업그레이드 대상 예약을 매일 찾아내는 작업으로 주당 약 2시간을 아꼈다. 지난해 실적을 바탕으로 수요 예측을 만들거나, 기존 요금표를 요금 상품으로 바꾸는 데 쓰는 사례도 있었다.

미국의 PMS 공급사 룸마스터(roommaster)도 10월 19일 MCP 기반 연결 도구를 발표하였다. 호텔은 ChatGPT, Claude, Microsoft Copilot, Google Gemini에서 도착·출발 고객, 미수금, 객실 재고를 일상 언어로 조회할 수 있다. 회사는 연결이 자동으로 켜지지 않고 호텔이 직접 승인해야 하며, 조회 범위는 사용자 권한에 따르고, 대화 내용은 각 AI 서비스의 약관과 데이터 처리 방침을 따른다고 밝혔다.

## 쓰임은 늘지만 신뢰는 그대로다

아팔레오 발표에는 h2c의 「Hotel Chain Tech Report 2026」 결과도 인용되었다. 호텔 체인의 91%가 AI를 쓰고 있어 1년 전 78%보다 늘었지만, MCP 같은 표준화된 AI 데이터 연결 계층을 갖춘 곳은 15%였고 52%는 도입 계획이 없었다. AI에 대한 의존도는 10점 만점에 4.7점에서 5.4점으로 올랐으나 신뢰도는 6.5점에 머물렀다. 일상적인 AI 사용의 60%는 ChatGPT 같은 외부 도구였고, 공급사 시스템에 내장된 AI는 27%였다. 이 수치는 보도자료를 통해 간접 인용된 것이므로 세부 조사 방법은 원 보고서로 확인할 필요가 있다.

이 결과는 직원들이 이미 외부 AI 도구를 업무에 쓰고 있지만, 그 연결과 사용 방식은 아직 정리되지 않았다는 점을 보여 준다.

## 권한과 책임을 먼저 정해야 한다

Hospitality Net의 10월 27일 브리핑에서 부르진 투르칸 젠지를리(Burcin Turkkan Zencirli)는 호텔 AI 에이전트 관리의 일곱 요소로 신원, 권한, 사람의 통제, 데이터 접근, 추적 가능성, 외부 에이전트 관리, 책임을 제시하였다. 그는 호텔에서는 권한이 개별 호텔, 운영사, 브랜드, 소유주, 공급사로 나뉘어 있어, 시스템에 접근할 수 있다는 것만으로 에이전트의 모든 행동이 승인된 것으로 볼 수 없다고 지적하였다. 또 항공사가 웹사이트 챗봇의 안내에 책임을 진 2024년 캐나다 사례(Moffatt v. Air Canada)를 들어, 자동화된 업무마다 책임자를 지정해야 한다고 주장하였다.

이상의 논의를 바탕으로 편집부가 제안하는 점검 항목은 다음과 같다.

- **읽기와 쓰기를 나눈다**: 조회부터 시작하고, 예약 수정이나 요금 변경처럼 데이터를 바꾸는 권한은 업무별로 단계적으로 연다.
- **사람 계정의 권한을 따르게 한다**: 에이전트가 별도의 관리자 권한으로 움직이지 않고, 지시한 직원의 권한 범위 안에서만 작동하게 한다.
- **기록을 남기고 책임자를 정한다**: 누가 어떤 지시로 무엇을 바꾸었는지 추적할 수 있어야 하며, 자동화된 업무마다 담당자를 정한다.
- **대량 변경은 미리 검증한다**: 2,000건을 한 번에 바꿀 수 있다는 것은 잘못된 지시도 2,000건에 한 번에 적용된다는 뜻이다. 일부 예약으로 결과를 확인한 뒤 전체에 적용한다.
- **고객 데이터의 이동을 확인한다**: 외부 AI 서비스로 투숙객 정보가 전달되면 국내에서는 개인정보 처리 위탁이나 국외 이전에 해당하는지 검토가 필요하다. 세부 기준은 법령과 전문가 확인이 필요하며, 기본 원칙은 [호텔 고객 데이터를 AI에 넣기 전에 확인할 것](/posts/hotel-data-ai-agent/)에서 정리하였다.

## 맺으며

MCP는 PMS를 직원이 찾아 들어가는 시스템에서 AI에게 묻고 맡기는 시스템으로 바꾸고 있다. 반복 업무가 줄어드는 만큼 직원은 고객 응대에 더 많은 시간을 쓸 수 있다. 그러나 그 효과는 권한, 기록, 책임이라는 기본 장치를 먼저 갖춘 호텔에서만 안전하게 얻을 수 있다. 기술의 속도보다 관리 체계의 속도가 성패를 가를 것이다.
