"""기존 글 28편의 미리보기 카드 이미지(목록·홈·SNS 공유용) 생성
본문 상단 이미지(thumbnail)는 그대로 두고, 미리보기용 card 이미지만 새 템플릿으로 만든다.
사용법: python3 scripts/thumbs/cards_20261104.py <출력 폴더(png)>
"""
import sys
from thumblib import keyword, stat, compare, steps, render

C = {
 'channel-manager-integration-testing': steps('hotel-it-qa', '객실 재고는 시스템 사이에서 틀어진다', [('server', 'PMS', '재고·요금 원장'), ('doc', '채널 매니저', '판매 채널 중계'), ('globe', 'OTA', '온라인 판매 채널')]),
 'column-housekeeping-seven-principles': keyword('column', ['하우스키핑으로', '읽는 테스트 7원칙'], 'ISTQB 테스트 원칙을 객실 점검의 언어로', 'bed'),
 'column-kiosk-and-front-manager': compare('column', '프런트 매니저에서 QA 담당자로', ('두려움', '키오스크가 일을 대신할까', 'kiosk'), ('질문', '품질은 누가 지키는가', 'search')),
 'column-testing-is-asking': keyword('column', ['테스트는', '질문이다'], '네 가지 테스트 기법을 하나의 질문으로', 'search'),
 'defect-report-severity-priority': compare('hotel-it-qa', '메모와 결함 보고서의 차이', ('메모', '"할인 이상함, 확인 바람"', 'alert'), ('보고서', '재현 절차·기대 결과·실제 결과', 'doc')),
 'flow-at-the-kiosk': keyword('service-quality', ['키오스크 앞에서도', '몰입은 일어날까'], '플로우 이론으로 본 셀프서비스', 'kiosk'),
 'hotel-brand-portfolio-2026': compare('hotel-resort', '호텔 브랜드 재편의 두 방향', ('위로', '하이엔드로 재개관', 'star'), ('옆으로', '인수·전환으로 지방 확장', 'pin')),
 'hotel-data-ai-agent': keyword('hotel-it-qa', ['AI에 넣기 전', '확인할 것'], '호텔 고객 데이터와 개인정보', 'shield'),
 'hotel-dates-test-design': steps('hotel-it-qa', '호텔 날짜가 어긋나는 세 지점', [('calendar', '영업일자', '나이트 오디트 전후'), ('bed', '숙박일', '밤 단위 계산'), ('globe', '시간대', '해외 채널 연동')]),
 'hotel-grading-reform-2026': keyword('tourism-policy', ['호텔 등급평가,', '무엇이 바뀌었나'], '개인정보 보호가 평가 항목이 되다', 'shield'),
 'hotel-kiosk-quality-checklist': stat('hotel-it-qa', '461명', '호텔 키오스크 이용객 분석', '오류 없는 기능만으로는 충분하지 않다', 'kiosk'),
 'hotelier-to-domain-qa': compare('tourism-policy', '서비스 인력에게 열리는 경로', ('호텔리어', '현장 서비스 경험', 'hotel'), ('도메인 QA', '업무 시스템 품질관리', 'check')),
 'inbound-tourists-stay-quality-2026': stat('tourism-policy', '+21.5%', '1~9월 방한 외래관광객', '늘어난 방문, 줄어든 체류', 'plane'),
 'kiosk-failure-service-recovery': steps('service-quality', '셀프서비스가 실패할 때', [('kiosk', '기기 오류', '예약을 찾지 못함'), ('users', '직원 연결', '사람에게 넘김'), ('check', '회복', '설명·사과·보상')]),
 'kiosk-service-gap-barrier-free': keyword('tourism-policy', ['키오스크가 만드는', '서비스 격차'], '디지털 역량에 따라 달라지는 경험', 'users'),
 'lodging-q3-2026-price-led-growth': stat('hotel-resort', '+10.1%', '호텔·리조트 객실당 매출', '대부분 객실 단가 인상에서 · 2026년 3분기', 'chartup'),
 'new-book-qa-with-ai-agent': keyword('hotel-it-qa', ['비전공자를 위한', 'QA 입문서 출간'], '『이제 QA, AI Agent랑 같이 합시다』', 'doc'),
 'report-ai-agent-qa-workflow': compare('report', 'AI 에이전트와 함께하는 QA', ('맡길 일', '문서 정리·빠진 것 찾기', 'doc'), ('판단할 일', '실행과 판정은 사람이', 'check')),
 'report-cancellation-qa-case': steps('report', '예약 변경·취소 기능 QA 2주', [('doc', '리뷰', '기획서 검토'), ('search', '설계·실행', '테스트와 결함 관리'), ('check', '완료 보고', '결과 정리')]),
 'report-hotel-kiosk-sstqual-flow': keyword('report', ['무엇이 고객을', '몰입하게 하는가'], '호텔 키오스크 이용객 461명 분석', 'kiosk'),
 'report-risk-based-testing-hotel': keyword('report', ['무엇부터', '테스트할 것인가'], '호텔 시스템의 리스크 기반 테스트', 'alert'),
 'room-703-error-defect-failure': steps('hotel-it-qa', '703호 이중 배정', [('users', '오류', '사람의 실수'), ('alert', '결함', '시스템 속 문제'), ('bed', '장애', '고객이 겪는 문제')]),
 'service-blueprint-hotel-checkin': compare('service-quality', '호텔 체크인의 두 영역', ('선 위', '고객이 보는 서비스', 'users'), ('선 아래', '직원 업무와 시스템', 'server')),
 'service-sense-to-test-design': keyword('hotel-it-qa', ['프런트의 "혹시"가', '테스트 케이스로'], '현장 감각과 테스트 기법', 'key'),
 'servqual-and-system-quality': keyword('service-quality', ['SERVQUAL 이후,', '시스템을 보는가'], '호텔 서비스품질 측정의 과제', 'star'),
 'sstqual-seven-dimensions': stat('service-quality', '7가지', '셀프서비스 기술 품질 기준', 'SSTQUAL', 'kiosk'),
 'us-hotel-outlook-2026': stat('hotel-resort', '+4.4%', '2026년 미국 호텔 RevPAR 전망', '2.8%에서 상향 · CoStar·Tourism Economics', 'globe'),
 'voc-to-test-priority': steps('service-quality', 'VOC에서 테스트 우선순위로', [('users', '수집', '고객·직원 문의'), ('chartup', '집계', '유형별 분류'), ('check', '반영', '테스트 우선순위')]),
}

if __name__ == '__main__':
    render(C, sys.argv[1])
    print(len(C), 'cards')
