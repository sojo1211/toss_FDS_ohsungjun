# 프로젝트 명세서: 토스뱅크 Anti-Fraud Manager 맞춤형 포트폴리오 (toss_FDS_ohsungjun)

이 프로젝트는 **Toss CX FDS/RMS 실무 역량**과 **AI 데이터 분석/리스크 정량화 학술 연구 성과**를 결합하여, **토스뱅크 Anti-Fraud Manager** 직무에 최적화된 오성준 님의 싱글 페이지 포트폴리오 웹사이트 구축을 목표로 합니다.

---

## 👤 프로필 개요 (Profile Overview)
* **이름:** 오성준 (Oh Sungjun)
* **소속:** 토스씨엑스 (Toss CX) FDS Team / Pay Risk Management Team
* **역할:** Operations Supporter (리스크 운영) / AI Developer & Risk Analyst
* **타겟 직무:** 토스뱅크 Anti-Fraud Manager (여신 사기 방지 및 리스크 관리)

---

## 🎯 핵심 메시지 및 메인 카피 (Hero Section)
* **메인 타이틀:** Toss CX FDS / RMS Risk Operations Specialist
* **서브 타이틀 / 훅:**
  > "온보딩 데이터 검수부터 14대 RMS 라벨링, 약관 기반 리스크 통제, 그리고 AI 데이터 분석까지 갖춘 준비된 Anti-Fraud 전문가 오성준입니다."

---

## 💼 현직 실무 역량 (Current Work Experience: Toss CX)

### 1. 온보딩 6대 Risk Factor 정밀 검수
* 가맹점 입점(Onboarding) 시 제출된 6대 리스크 팩터와 실제 웹사이트 운영 데이터 간의 Discrepancy(불일치) 교차 검증.
* **주요 검수 항목:** 배송 종류(국내/해외), 배송/서비스 소요 시간, 최고 객단가, 판매 형태(중개/다단계/사전예약 등), 실물/비실물 구분, 취소/환불 규정.

### 2. MID 조회 및 14대 RMS 기준표 정량 라벨링
* RMS Alert 발생 건을 토스페이파트너스(TOI/Paybiz)에서 MID 단위로 역추적 후 가맹점 웹사이트 실사 점검.
* **14대 RMS 라벨링 기준:** ① 판매불가상품 ② 환금성판매 ③ 배송기간 1달 초과 ④ 판매상품 불명확 ⑤ 유의 상품 판매 ⑥ 운영종료 ⑦ URL 확인 ⑧ 신용불량 ⑨ 기본환불한도과다 ⑩ 기업회생/파산 ⑪ 수익/환불 보장 문구 ⑫ 3개월 거래 미발생 ⑬ 취소주기 ⑭ 상품 변질.

### 3. 계약 시점별 약관/공문 차등 리스크 통제 (2023.07.10 분기)
* **2023.07.10 이후 가입 가맹점:** 전자금융거래 이용약관 기반 메일 소명 요청 (일반 3일 / 신용불량 5일 타이트 관리).
* **2023.07.10 이전 가입 가맹점:** 서면 계약 조항 준수를 위한 내부 결재 및 정식 공문(인감 날인) 발송.

### 4. 선제적 자금 손실 차단 (Pre-signal Action)
* 미소명 및 고위험 가맹점 대상 지급보류, 결제 OFF(연동 해제), MID 분리, 서비스 비활성화 조치로 2차 연체 및 손실 사전 예방.

---

## 🎓 학술 연구 & 핵심 프로젝트 (Research & Projects)

### 1. SRHS (Stablecoin Risk Health Score)
* **내용:** 스테이블코인 붕괴 예방을 위한 5개 핵심 리스크 지표(PD·LS·CR·TI·RR) 정량화 프레임워크 설계.
* **성과:** 한국경영컨설팅학회 최우수상 수상 & KCI 등재지 『경영컨설팅연구』 제26권 3호 논문 게재.

### 2. SafeFall Intelligence
* **내용:** 시계열 생체신호 이상 탐지(Anomaly Detection) 및 Decision 라벨 설계.
* **성과:** 용인대학교 창업경진대회 최우수상 수상.

### 3. KB국민은행 제8회 AI Challenge
* **내용:** 소상공인 비대면 정책자금 사전 검증 RAG 기반 AI 에이전트 구축 (데이터 파이프라인 및 UI/UX).

---

## 🛠️ 기술 스택 & 도구 (Tech Stack Architecture)

### 1️⃣ Financial Risk & Systems (최상단)
* **Systems:** `RMS` · `FDS` · `AML` · `TOI Admin` · `SFDC (Paybiz)`
* **Domain:** `소매여신/SOHO Risk` · `비대면 서류 검수` · `가맹점 온보딩 Factor 검수` · `14대 RMS 라벨링` · `약관/공문 프로세스`

### 2️⃣ Data Analysis & Validation
* **Languages & Libs:** `Python` · `Pandas` · `NumPy` · `scikit-learn` · `SQL`
* **Analysis & Logic:** `Data Deep Dive` · `시계열 이상 탐지 (Anomaly Detection)` · `Fraud-Rule Optimization` · `Pre-signal Analysis`

### 3️⃣ AI Engine & Fast Prototyping
* **Tools & Models:** `Claude Code` · `LangChain` · `RAG` · `Vector DB (Chroma)` · `PyTorch`
* **Methodology:** `AI-Native Dev (Vibe Coding)` · `Fast Prototyping` · `PDF/HWP Data Pipeline`

### 4️⃣ Tools & Collaboration
* `Git` · `React` · `Tailwind CSS` · `Figma` · `Notion` · `Slack Core Channels`

---

## 🎨 UI/UX 디자인 가이드라인

* **컬러 팔레트:** 토스 특유의 신뢰감 있는 블루 컬러(Toss Blue: `#0040FF` 또는 `#3182F6`), 깔끔한 다크/라이트 모드 지원.
* **폰트:** Pretendard 또는 Toss Product Sans 느낌의 깔끔한 Sans-serif.
* **레이아웃 구조:**
  1. **Hero Section:** 타이틀, 서브타이틀, 프로필 요약, 주요 링크(GitHub, Contact).
  2. **Tech Stack Section:** 4개 카테고리별 태그 카드 형태 배치 (Financial Risk가 맨 위에 오도록).
  3. **Current Role (Toss CX):** 타임라인 및 4가지 핵심 프로세스(온보딩, 14대 라벨링, 약관/공문, 손실차단) 시각화.
  4. **Research & Projects:** SRHS, SafeFall, KB RAG 프로젝트 카드 및 배지(학회 최우수상, KCI 게재 등).
  5. **Contact / Outro:** 이메일, 연락처, 토스뱅크 Anti-Fraud를 향한 비전 문구.
