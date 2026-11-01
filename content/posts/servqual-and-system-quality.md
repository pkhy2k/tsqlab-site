---
title: SERVQUAL 이후, 호텔 서비스품질 측정은 시스템을 보고 있는가
subtitle: 고객 접점이 디지털로 옮겨간 지금, 소프트웨어 품질은 서비스품질의 일부로 다뤄져야 한다
category: service-quality
author: research
date: 2026-11-01
featured: true
pick: true
summary: 호텔의 고객 접점이 키오스크·모바일 체크인·PMS로 옮겨가면서, 사람 중심으로 설계된 기존 서비스품질 척도만으로는 품질 문제의 원인을 설명하기 어려워졌다. 서비스품질 연구와 소프트웨어 품질 표준을 연결하는 관점을 제안한다.
tags: [서비스품질, SERVQUAL, 호텔IT, 소프트웨어품질]
references:
  - "Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1985). A conceptual model of service quality and its implications for future research. *Journal of Marketing*, 49(4), 41–50."
  - "Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1988). SERVQUAL: A multiple-item scale for measuring consumer perceptions of service quality. *Journal of Retailing*, 64(1), 12–40."
  - "Cronin, J. J., & Taylor, S. A. (1992). Measuring service quality: A reexamination and extension. *Journal of Marketing*, 56(3), 55–68."
  - "Parasuraman, A., Zeithaml, V. A., & Malhotra, A. (2005). E-S-QUAL: A multiple-item scale for assessing electronic service quality. *Journal of Service Research*, 7(3), 213–233."
  - "ISO/IEC 25010:2011. Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model."
---

체크인 카운터 앞에 줄이 길어지는 장면을 떠올려 보자. 고객은 "직원이 느리다"고 느끼고, 사후 설문에서는 응답성(responsiveness) 점수가 낮게 나온다. 그런데 실제 원인이 직원이 아니라 객실관리시스템(PMS, Property Management System)의 응답 지연이었다면, 이 점수는 무엇을 측정한 것일까.

## 사람을 중심에 둔 측정 도구

서비스품질 연구의 출발점으로 꼽히는 Parasuraman, Zeithaml과 Berry(1985)의 갭 모형(Gap Model)은 고객의 기대와 지각의 차이로 서비스품질을 정의하였다. 이를 측정 도구로 구체화한 SERVQUAL(1988)은 유형성, 신뢰성, 응답성, 확신성, 공감성의 다섯 차원으로 구성되며, 이후 숙박업 등 여러 산업에 맞게 변형되어 쓰여 왔다. Cronin과 Taylor(1992)는 기대를 빼고 지각만 측정하는 SERVPERF를 제안하며 측정 방식에 대한 논쟁을 이어갔다.

이들 척도는 공통적으로 **사람이 서비스를 전달하는 상황**을 전제로 설계되었다. 신뢰성은 "약속한 서비스를 정확하게 수행하는가", 응답성은 "신속하게 도우려 하는가"를 묻는다. 여기서 주어는 대체로 직원이다.

## 고객 접점이 시스템으로 옮겨가고 있다

오늘날 호텔의 고객 접점은 상당 부분 시스템을 거친다. 예약은 채널 매니저(Channel Manager)와 예약 엔진을 통해 들어오고, 체크인은 키오스크나 모바일 앱에서 이루어지며, 객실 상태와 요금은 PMS가 관리한다. 직원이 응대하는 순간에도 그 뒤에서는 시스템이 정보를 불러오고 처리한다.

이러한 환경에서 고객이 겪는 품질 문제의 상당수는 시스템 결함이나 성능 저하에서 비롯될 수 있다. 예약 정보가 채널 간에 일치하지 않는 문제, 결제 처리 지연, 객실 상태가 늦게 갱신되는 문제는 모두 고객에게는 "서비스가 나빴다"는 경험으로 남는다. 그러나 사람 중심으로 설계된 척도로는 이 경험이 어디서 비롯되었는지 구분하기 어렵다.

> 고객이 지각하는 서비스품질의 일부는 이미 소프트웨어 품질이다.

## 두 연구 전통을 잇는 관점

이 공백을 메우려는 시도가 없었던 것은 아니다. Parasuraman, Zeithaml과 Malhotra(2005)는 온라인 서비스의 품질을 측정하는 E-S-QUAL을 개발하여 효율성, 시스템 가용성, 이행, 프라이버시 등의 차원을 제시하였다. 다만 이는 고객이 웹사이트를 직접 이용하는 전자서비스를 대상으로 한 것으로, 직원과 시스템이 함께 서비스를 전달하는 호텔 현장의 혼합적 상황을 직접 다루지는 않는다.

한편 소프트웨어공학에는 ISO/IEC 25010과 같은 제품 품질 모델이 있다. 2011년판 기준으로 이 모델은 기능 적합성, 성능 효율성, 신뢰성, 사용성 등으로 소프트웨어 품질을 정의한다. 흥미로운 점은 이 품질 특성들이 서비스품질 차원과 상당 부분 대응한다는 것이다. 예컨대 시스템의 성능 효율성은 고객이 지각하는 응답성에, 시스템의 신뢰성은 서비스의 신뢰성에 영향을 미칠 수 있다.

## 현장과 연구에 주는 시사점

호텔 실무에서는 서비스품질 개선을 직원 교육 중심으로 접근하는 경우가 많다. 그러나 고객 불만의 원인이 시스템에 있다면 교육만으로는 문제가 해결되지 않는다. 고객 불만 데이터를 분석할 때 시스템 장애 기록과 함께 살펴보는 것만으로도 원인 진단의 정확도를 높일 수 있다.

연구 측면에서는 서비스품질 척도와 소프트웨어 품질 특성의 대응 관계를 실증적으로 검토하는 작업이 필요하다. 시스템 품질이 고객의 서비스품질 지각에 어떤 경로로 영향을 미치는지 밝힌다면, 호텔 IT 투자와 품질관리(QA) 활동의 성과를 고객 경험의 언어로 설명할 수 있게 될 것이다.
