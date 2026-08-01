# 📌 오성준 (Oh Sungjun) — Portfolio

<p align="center">
  <img src="./성준사진.jpg" width="300" alt="오성준 프로필 사진" style="border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);" />
</p>
---

# 👤 Profile

- **이름:** 오성준 (Oh Sungjun)
- **소속:** Toss CX FDS Team / Pay Risk Management Team
- **직무:** Risk Operations · AI Developer · Risk Analyst
- **Target Position:** Toss Bank Anti-Fraud Manager

---

# 🎯 Hero

## Toss CX FDS / RMS Risk Operations Specialist

> **Toss CX FDS/RMS 실무 경험과 AI 데이터 분석·SRHS 리스크 정량화 연구 성과를 바탕으로 Anti-Fraud 전문성을 갖춘 오성준입니다.**

---

# 💼 Current Work Experience

## 1️⃣ Onboarding Risk Review

가맹점 입점(Onboarding) 시 등록된 **6대 Risk Factor**와 실제 웹사이트 운영 정보를 교차 검증하여 리스크를 식별했습니다.

**주요 검수 항목**

- 국내/해외 배송 여부
- 배송 및 서비스 소요 기간
- 최고 객단가
- 판매 형태
- 실물/비실물 상품
- 취소 및 환불 정책

---

## 2️⃣ RMS Labeling

RMS Alert 발생 건을 TOI / Paybiz에서 MID 단위로 역추적하여 실제 가맹점을 조사하고 **14대 RMS 기준**에 따라 정량 라벨링을 수행했습니다.

대표 검수 항목

- 판매불가상품
- 환금성 판매
- 배송기간 초과
- 판매상품 불명확
- 유의 상품
- 운영 종료
- URL 확인
- 신용불량
- 기본 환불한도 과다
- 기업회생 / 파산
- 수익·환불보장 문구
- 거래 미발생
- 취소주기
- 상품 변질

---

## 3️⃣ Contract-based Risk Control

계약 시점에 따라 차등 리스크 통제를 수행했습니다.

### 2023.07.10 이후

- 전자금융거래 이용약관 기반 메일 소명 요청
- 일반 3일
- 신용불량 5일

### 2023.07.10 이전

- 내부 결재 진행
- 인감 날인 공문 발송
- 계약 조항 기반 리스크 통제

---

## 4️⃣ Pre-signal Action

고위험 가맹점에 대해

- 지급보류
- 결제 OFF
- MID 분리
- 서비스 비활성화

등의 조치를 수행하여 자금 손실을 사전에 예방했습니다.

FDS 팀/업무 일지

https://app.notion.com/p/FDS-35d4fb823a9e83b3928281123aa0d524?source=copy_link
---

# 🎓 Research & Projects

## 🏆 SRHS (Stablecoin Risk Health Score)

### 연구 배경

Terra-UST 사태 이후 스테이블코인의 안정성을 객관적으로 평가할 수 있는 기준의 필요성이 커졌습니다. 기존 평가는 담보비율이나 가격 유지 여부 등 **단일 지표 중심의 사후 분석**에 머무르는 한계가 있었습니다.

이에 저는 **"스테이블코인의 건전성을 사고 발생 이전에 정량적으로 평가할 수 있는 리스크 모델"** 을 목표로 연구를 수행했습니다.

---

### 연구 내용

SRHS(Stablecoin Risk Health Score)는 스테이블코인의 건전성을 **다섯 가지 핵심 리스크 요인(PD, LS, CR, TI, RR)** 으로 분해하여 평가하는 **리스크 정량화 프레임워크**입니다.

단순히 위험 요소를 나열하는 것이 아니라, 각 리스크를 계량화하고 종합 점수(Risk Health Score)로 산출하여 **스테이블코인의 안정성을 객관적으로 비교·평가할 수 있는 모델**을 설계했습니다.

주요 평가 요소는 다음과 같습니다.

- **PD (Peg Deviation)** : 목표 가격(페그) 유지 안정성
- **LS (Liquidity Stability)** : 유동성 안정성
- **CR (Collateral Risk)** : 담보 건전성
- **TI (Transparency Index)** : 정보 공개 투명성
- **RR (Reserve Reliability)** : 준비자산의 신뢰성

이 프레임워크를 통해 **사후 붕괴 분석이 아닌 사전 리스크 예측 및 예방 관점의 정량적 평가 모델**을 제안했습니다.

---

### 연구 의의

이 연구를 수행하며 단순한 AI 모델 개발을 넘어,

- 금융 리스크를 정의하고,
- 리스크 요인을 설계하며,
- 정량화 지표를 구축하고,
- 하나의 Risk Score로 통합하는

**리스크 모델링(Risk Modeling)과 Risk Scoring Framework 설계 역량**을 쌓았습니다.

이러한 경험은 현재 Toss CX에서 수행하고 있는 **RMS 라벨링, Risk Review, 정책 기반 리스크 통제 업무**와도 자연스럽게 연결되고 있습니다.

---
### 성과

🏆 **한국경영컨설팅학회 최우수 논문상**

📖 **KCI 등재지 『경영컨설팅연구』 제26권 제3호 논문 게재**

👨‍💻 **공동 저자**

[Uploading B2B 무역결제에서 스테이블 코인의 안정성 평가 모델 개발  실시간 건전성 지수(SRHS)와 규제 통합 프레임워크 중심.pdf…]()

---

## 🏆 SafeFall Intelligence

### 연구 내용

시계열 생체신호 이상 탐지(Anomaly Detection) 및 Decision Label 설계

### 성과

- 용인대학교 창업경진대회 최우수상

---

## 🏆 KB국민은행 제8회 AI Challenge

### 프로젝트

소상공인 비대면 정책자금 사전 검증을 위한

- RAG 기반 AI Agent 구축
- 데이터 파이프라인 설계
- UI/UX 개발

---

# 🛠 Tech Stack

## Financial Risk

`FDS`
`RMS`
`AML`
`TOI Admin`
`SFDC (Paybiz)`

## Domain Knowledge

`Merchant Onboarding`
`Risk Review`
`Fraud Detection`
`SOHO Risk`
`Retail Lending`
`Risk Labeling`

## Data Analysis

`Python`
`SQL`
`Pandas`
`NumPy`
`scikit-learn`

## AI

`LangChain`
`RAG`
`Claude Code`
`Vector DB`
`PyTorch`

## Collaboration

`Git`
`React`
`Tailwind CSS`
`Figma`
`Slack`
`Notion`

---

# 📈 Career Timeline

| Year | Experience |
|------|------------|
| Present | Toss CX FDS Team / Pay Risk Management |
| 2026 | KB국민은행 AI Challenge |
| 2025 | SRHS 논문 KCI 게재 |
| 2024 | SafeFall Intelligence 최우수상 |

---

# 📜 Certifications

- AML Basic
- SQLD (Planned)
- ADsP (Planned)

---

# 💡 My Story

## From Research to Real-world Risk Operations

저는 **"사고를 탐지하는 것보다, 사고를 예방하는 것이 리스크 관리의 본질"** 이라는 문제의식을 바탕으로 AI와 금융 리스크를 연구해왔습니다.

이러한 문제의식을 바탕으로 **스테이블코인의 건전성을 정량적으로 평가하는 SRHS(Stablecoin Risk Health Score) 모델**을 설계했으며, 해당 연구는 **한국경영컨설팅학회 최우수상 수상**과 **KCI 등재 논문 게재**라는 성과로 이어졌습니다.

이후 실제 금융 환경에서 리스크 관리가 어떻게 운영되는지 경험하기 위해 **Toss CX FDS Team**에 합류했습니다.

현재는 **가맹점 온보딩 6대 Risk Factor 검수, 14대 RMS 라벨링, 지급보류, 결제 OFF, MID 분리, 공문 발송** 등 리스크 통제 프로세스를 직접 수행하며 실무 경험을 쌓고 있습니다.

특히 **자동화된 리스크 탐지 결과를 운영 관점에서 재검증하며 정책 우회 사례를 발견하고 통제하는 과정**에 가장 큰 흥미를 느꼈습니다.

실제로 **실물 상품만 입점 가능한 환경에서 일부 가맹점이 교육·체험 등 비실물 상품을 실물 상품으로 등록한 사례**를 웹사이트 실사와 소명 절차를 통해 확인했고, 운영 정책에 맞게 정보를 수정하도록 조치한 경험이 있습니다. 이 과정에서 **시스템이 탐지한 결과를 운영 데이터와 교차 검증하여 정책 우회 행위를 식별하고 리스크를 선제적으로 통제하는 것**이 Anti-Fraud 업무의 핵심임을 체감했습니다.

또한 **AML Basic 자격을 취득**했으며, 향후 AML 전문 교육과 심화 자격을 통해 금융 범죄 대응 역량을 지속적으로 고도화할 계획입니다.

궁극적으로는 **토스뱅크 Anti-Fraud Manager**로서 **데이터 기반 분석과 정교한 Fraud Rule 설계, 그리고 운영 경험을 바탕으로 변화하는 사기 패턴을 선제적으로 탐지하고 대응하여 비대면 금융 서비스의 신뢰성과 안전성을 높이는 데 기여하고자 합니다.**

---

# 📫 Contact

- 📧 Email : sungjun12110@gmail.com
- 🐙 GitHub : sojo1211@naver.com
