---
title: AI가 객실 요금을 정할 때, 수익관리자는 무엇을 정하는가
subtitle: 듀에토의 FLYR 호스피탈리티 인수와 업계 실무자의 증언으로 본 AI 수익관리시스템의 현재
category: hotel-it-qa
author: research
thumbnail: /images/posts/ai-rms-guardrails-2026.jpg
thumbnail_alt: AI 수익관리시스템이 반복적인 일일 요금 결정을 맡고, 수익관리자는 요금의 상한과 하한, 예외 상황, 협상 요금을 맡는 역할 분담을 보여 주는 도식
date: 2026-11-04
summary: 수익관리시스템(RMS)에 AI가 기본 기능으로 들어가면서, 요금 결정의 상당 부분이 자동화되고 있다. 듀에토의 FLYR 호스피탈리티 인수와 업계 실무자들의 증언을 정리하고, 자동화 시대에 수익관리자가 맡아야 할 역할을 살펴본다.
tags: [호텔IT솔루션, 수익관리, RMS, AI요금, 호텔경영]
references:
  - "Hospitality Net (2026.10.08). Duetto acquires FLYR Hospitality to expand its platform and accelerate innovation for hoteliers. https://www.hospitalitynet.org/news/4134812/duetto-acquires-flyr-hospitality-to-expand-its-platform-and-accelerate-innovation-for-hoteliers"
  - "PhocusWire (2026.10). Duetto acquires FLYR Hospitality to boost AI capabilities. https://www.phocuswire.com/news/technology/duetto-acquires-flyr-hospitality-boost-ai-capabilities"
  - "Rajecki, R. (2026.08.20). The new revenue playbook: AI-powered, human-led. Hotel Management, August/September 2026. https://hotelmanagement.mydigitalpublication.com/articles/the-new-revenue-playbook-aipowered-human-led"
---

수익관리(Revenue Management)는 같은 객실을 언제, 누구에게, 얼마에 팔 것인가를 정하는 일이다. 과거에는 수익관리자가 예약 추세와 경쟁 호텔 요금을 보며 판단했고, 수익관리시스템(RMS, Revenue Management System)은 그 판단을 돕는 도구였다. 최근에는 AI가 요금을 직접 정하고 실시간으로 바꾸는 단계로 넘어가고 있다. 이 글은 최근의 업계 인수 소식과 실무자들의 증언을 정리하고, 자동화가 진행될 때 수익관리자가 맡아야 할 역할을 살펴본다.

## AI가 요금 엔진의 중심이 되었다

Hospitality Net 보도(2026년 10월 8일)에 따르면, 호텔 수익관리 소프트웨어 기업 듀에토(Duetto)는 자동화 수익관리와 경영정보 분석 기업 FLYR 호스피탈리티(FLYR Hospitality)를 인수하였다. 인수 금액은 공개되지 않았다. FLYR의 요금 엔진은 하나의 예측값이 아니라 여러 수요 시나리오를 함께 계산하고, 강화학습(Reinforcement Learning)으로 계속 학습하며, 요금을 실시간으로 바꾼다. 일상 언어로 질문하면 답을 주는 분석 도구도 함께 넘어왔다. 듀에토는 이를 기존 제품군에 합쳐, 사람이 직접 조정하는 방식과 완전 자동화 방식 가운데 호텔이 고를 수 있게 하겠다고 밝혔다.

같은 흐름은 현장에서도 확인된다. 미국 호텔 전문지 Hotel Management의 기사(2026년 8월 20일)에서 한 호텔 그룹의 수익 담당 부사장은 거의 모든 RMS에 AI나 머신러닝이 들어가 있다고 말하였다. 호텔이 시스템의 추천을 모두 받아들이지 않더라도, 요금 전략 자체는 이미 AI가 만든 결과에 기대고 있다는 것이다.

## 자동화되는 일과 남는 일

같은 기사에 등장한 실무자들은 AI와 사람의 역할을 비교적 분명히 나누었다. 한 호텔 체인의 수익 담당 임원은 AI 시스템이 호텔이 정한 범위 안에서 매일의 요금을 정하고, 수익관리자는 신규 호텔의 초기 운영, 시장의 급격한 변화, 기업·항공 승무원 같은 협상 요금을 맡는다고 설명하였다. 듀에토의 최고기술책임자는 수익관리자가 범위, 즉 가드레일(Guardrail)을 정하고 AI는 그 안에서 실행하는 구조를 강조하였다. 다른 운영사 임원은 경험 많은 운영자가 시장을 이해하고 필요할 때 데이터에 이의를 제기해야 한다고 말하였다.

이 증언들은 하나의 방향을 가리킨다. 반복되는 대량의 요금 결정은 AI가 맡고, 사람은 그 결정의 경계와 예외를 맡는다. 다만 이는 한 매체가 소개한 미국 실무자들의 견해이며, 국내 호텔의 도입 수준이나 효과를 보여 주는 자료는 아니다.

## 요금 자동화가 고객 경험에 닿는 지점

요금은 수익의 문제이면서 고객이 가장 먼저 마주하는 서비스 정보이다. 국내 숙박시장의 2026년 3분기 성장이 주로 객실 단가 인상에서 나왔다는 점은 [객실은 비싸졌고 손님은 그대로다](/posts/lodging-q3-2026-price-led-growth/)에서 정리하였다. 가격이 오를수록 고객의 기대도 높아진다는 점을 생각하면, 요금을 자동으로 바꾸는 시스템일수록 설명할 수 있는 가격이어야 한다. 편집부의 제안으로 AI 요금을 도입할 때 점검할 항목을 정리하면 다음과 같다.

- **가드레일을 문서로 남긴다**: 요금의 하한과 상한, 하루 최대 변동 폭, 경쟁 호텔 대비 허용 범위를 수익관리자가 정하고 기록한다. 시스템이 바뀌거나 담당자가 바뀌어도 기준이 남아야 한다.
- **예외 상황의 전환 기준을 정한다**: 대형 행사, 재난, 시스템 장애처럼 과거 데이터가 맞지 않는 시기에는 자동화를 멈추고 사람이 판단하는 조건을 미리 정한다.
- **추천을 거부한 이유를 남긴다**: 수익관리자가 AI의 추천을 받아들이지 않은 경우 그 이유를 기록하면, 시스템을 조정하는 근거이자 팀의 학습 자료가 된다.
- **채널 간 요금 일관성을 확인한다**: 요금이 자주 바뀔수록 채널 매니저와 예약 엔진에 같은 요금이 제때 반영되는지가 중요해진다. 연동 점검은 [채널 매니저 연동 테스트](/posts/channel-manager-integration-testing/)에서 다루었다.
- **고객에게 설명할 수 있는가를 묻는다**: 같은 날짜의 요금이 몇 시간 만에 크게 달라지면 고객은 이유를 묻는다. 프런트와 예약 담당자가 답할 수 있는 수준의 설명이 준비되어야 한다.

## 맺으며

AI 수익관리시스템은 수익관리자의 일을 없애기보다 일의 위치를 바꾸고 있다. 매일의 요금 결정에서 한 걸음 물러나, 그 결정이 지켜야 할 경계와 예외를 설계하는 일이 수익관리자의 핵심 역할이 된다. 자동화의 수준이 높아질수록 가드레일을 정하고 지키는 사람의 판단이 호텔의 수익과 고객 신뢰를 함께 좌우할 것이다.
