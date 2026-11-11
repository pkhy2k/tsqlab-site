---
title: "Is an Error-Free Kiosk a Good Kiosk?"
subtitle: Reframing the quality checks for hotel kiosks around the seven SSTQUAL factors
category: hotel-it-qa
author: research
thumbnail: /images/posts/en/hotel-kiosk-quality-checklist.jpg
thumbnail_alt: A checklist dividing hotel kiosk quality checks into conditions for reuse and conditions for flow
date: 2026-11-02
summary: Quality management for hotel kiosks usually focuses on checking that functions work without errors. A study analysing 461 hotel kiosk users shows that functionality contributes to the intention to reuse but does not create flow. We translate the seven SSTQUAL factors into quality check perspectives and set out what to check beyond functional testing.
tags: [Hotel IT, Software QA, Kiosks, SSTQUAL, Usability Testing, PMS]
references:
  - "박건희 (2025). *호텔 키오스크의 셀프 서비스 기술 품질(SSTQUAL)이 플로우(Flow)와 지속이용의도에 미치는 영향: 디지털 리터러시의 조절효과를 중심으로*. 박사학위논문, 경기대학교 대학원. 제1장, 제4장, 제5장."
  - "Lin, J. S. C., & Hsieh, P. L. (2011). Assessing self-service technology encounters: Development and validation of SSTQUAL scale. *Journal of Retailing*, 87(2), 194-206."
---

For QA staff validating a hotel kiosk, the criteria for a good kiosk are usually clear. Is the booking retrieved correctly? Is the room assigned correctly? Is the payment amount right? Is the room key issued? Is all this information properly reflected in the hotel's property management system (PMS)? If the flow passes without defects, it is judged ready for release.

Director Winston Park's doctoral dissertation provides evidence that these criteria are necessary but not sufficient. This article rereads the dissertation's findings from the perspective of hotel IT quality management. The dissertation's results and the Editorial Team's interpretation are written separately.

## Why hotel kiosks are especially difficult

The dissertation raises the problem through the difference between hotel kiosks and restaurant kiosks. A restaurant kiosk is a simple flow from menu selection to ordering and payment. A hotel self check-in/out kiosk is a complex process linking booking retrieval, room assignment, room key issuance, payment, payment for add-on services, room key recognition and check-out, and it must exchange this information with the PMS in both directions in real time.

Because of this structure, the dissertation finds that the hotel industry tends to view kiosks in terms of stability and maintenance efficiency rather than user experience. The more integration points there are, the greater the chance of failure, so it is natural that quality management focuses on stability. The problem is that, as a result, kiosks can come to be seen as tools that guests find hard to use on their own.

## What the study showed: the conditions for reuse and for flow are different

The dissertation analysed the effects of the seven factors of the self-service technology quality scale SSTQUAL on customers' continuance intention and on flow, respectively.

For **continuance intention**, all six factors except convenience were significant.

- Enjoyment β = .197, functionality β = .183, customisation β = .172
- Design β = .149, assurance β = .124, security/privacy β = .106

For **flow**, only two factors were significant.

- Enjoyment β = .307, customisation β = .298
- Functionality (β = −.060), security/privacy (β = .001), assurance (β = .079) and convenience (β = .008) were not significant, and design (β = .105) stayed at the borderline with p = .052.

Flow in turn led to continuance intention (β = .610). In short, functionality and security contributed to customers using the kiosk again but did not create flow at the kiosk; what created flow was enjoyment and customisation.

There are cautions in interpreting these figures. Non-significance in multiple regression means a factor's unique explanatory power is small when the other factors are considered together, not that it has no effect. The simple correlation between functionality and flow was .385 and significant. This study is also cross-sectional, measuring perceptions at the time of the survey, so it is safer to read the relationships between factors as significant associations rather than to assert causation.

## Editorial interpretation: turning the seven factors into check perspectives

From here on are the Editorial Team's proposals based on the dissertation's findings. Turning each SSTQUAL factor into a question QA can check gives the following. The first three items are areas existing functional and non-functional testing generally covers; the last four are areas covered relatively less.

### Areas covered by existing testing

1. **Functionality**: Is everything from booking retrieval to check-out processed accurately and quickly? Does the system recover from PMS integration failures, payment approval delays and room key issuance errors?
2. **Security/privacy**: Are the personal and payment details entered processed securely? Does no information from the previous guest remain for the next one?
3. **Convenience**: Is the kiosk in an easy-to-find place, and is it available during operating hours?

### Areas covered less

4. **Design**: Can a first-time guest tell the next step without guidance? According to the dissertation's moderation results, design had a greater effect on flow among users with lower digital literacy. This is grounds for recruiting usability test participants from guests who are not familiar with digital devices.
5. **Enjoyment**: Is the check-in process a positive experience for guests? As a practical implication, the dissertation suggested checking technologies that can create interest (such as facial recognition) and whether photos and copy are displayed.
6. **Customisation**: Are multiple languages and voice guidance provided? Are there flows suited to guests' languages and ages? The dissertation also gave offering payment methods commonly used in guests' home countries as an example of customisation.
7. **Assurance**: Do guests feel they can trust this device and this hotel enough to enter their information? When an error occurs, are they told what to do next?

The last four items do not fit the format of a defect report well. To address them, it is realistic to state them as acceptance criteria at the requirements stage. They become test targets only when written in a checkable form, such as "four or more supported languages", "copy guiding the next action shown on every screen" or "at least four of five participants unfamiliar with digital devices complete check-in without help". The figures are examples and should be set to suit the hotel and its guest mix.

## Setting priorities

Not every item can be examined in the same depth. From a risk-based testing perspective, functionality and security have the greatest impact when they fail. Payment errors or exposure of personal data lead to financial and legal problems before they affect the guest experience. These two areas should therefore still be tested first and most deeply. How to assess risk is set out in the [risk-based testing report](/posts/report-risk-based-testing-hotel/).

The findings do, however, give grounds for the next priority. Among kiosks that already function stably, what separated guests' flow and reuse was enjoyment and customisation. Extending release criteria beyond "no defects" to include user experience items could be how hotel kiosk QA contributes to service quality.

## Reading it together with the study's limitations

The dissertation states that these results were obtained by mixing kiosks from several vendors and a variety of hotel guests, so differences in technical quality between vendors were not controlled. Respondents also recalled usage experiences from the previous three months, so impressions of the whole stay may have been mixed in. Rather than applying these results directly to a particular device at a particular hotel, it is better to use them as a starting point to check against your own device's user data and guest inquiries (VOC). How to connect guest inquiries to test priorities is covered in [Turning VOC into Test Priorities](/posts/voc-to-test-priority/).
