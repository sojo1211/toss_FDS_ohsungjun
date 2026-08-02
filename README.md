# 📌 오성준 (Oh Sungjun)

<p align="center">
  <img src="./성준사진.jpg" width="260" alt="오성준 프로필"/>
</p>

# Risk Operations · AI Developer · Risk Analyst

> **Toss CX FDS/RMS 리스크 운영 경험과 금융 리스크 정량화 연구를 바탕으로 데이터 기반 리스크 분석 및 통제 역량을 쌓아온 오성준입니다.**

---

# 👤 Profile

- **Name** : 오성준 (Oh Sungjun)
- **Current** : Toss CX FDS Team / Pay Risk Management Team
- **Target Position** : Toss Bank Anti-Fraud Manager

---

# 🔍 Core Competencies

## Risk Operations

- Merchant Onboarding Risk Review
- RMS Labeling
- Merchant Risk Assessment
- Risk Review
- Pre-signal Risk Control

## Financial Risk Modeling

- Stablecoin Risk Health Score (SRHS)
- Risk Scoring Framework
- Financial Risk Quantification

## Data Analysis

- Python
- SQL
- Pandas
- NumPy
- scikit-learn

## AI Development

- LangChain
- Claude Code
- RAG
- Vector DB

---

# 💼 Current Work Experience

## Toss CX FDS Team / Pay Risk Management Team

### ① Merchant Onboarding Risk Review

가맹점 입점(Onboarding) 시 등록된 **6대 Risk Factor**와 실제 웹사이트 운영 정보를 교차 검증하여 정책 위반 가능성과 리스크 요소를 식별했습니다.

**주요 검수 항목**

- 배송 방식
- 배송 기간
- 최고 객단가
- 판매 형태
- 실물 / 비실물 여부
- 취소 및 환불 정책

등록 정보와 실제 운영 정보 간의 불일치를 확인하여 정책 위반 가능성을 검토하고 리스크를 사전에 식별하는 업무를 수행했습니다.

---

### ② RMS Labeling

RMS Alert 발생 건을 **MID 단위로 추적**하여 TOI / Paybiz에서 가맹점 정보를 확인하고, 실제 웹사이트 운영 현황을 조사한 뒤 **14대 RMS 기준**에 따라 리스크 사유를 라벨링했습니다.

**대표 검수 항목**

- 판매불가상품
- 환금성 판매
- 배송기간 초과
- 판매상품 불명확
- 운영 종료
- URL 확인
- 신용불량
- 기본 환불한도 과다
- 기업회생 / 파산
- 수익·환불 보장 문구
- 거래 미발생
- 취소주기
- 상품 변질

라벨링 결과를 기반으로 운영 정책에 따른 후속 리스크 검토 및 통제 절차를 지원했습니다.

---

### ③ Risk Control

계약 시점과 리스크 수준에 따라 다양한 운영 통제를 수행했습니다.

- 메일 소명 요청
- 공문 발송
- 지급보류
- 결제 OFF
- MID 분리

고위험 가맹점에 대해서는 운영 정책에 따라 선제적인 리스크 통제 업무를 수행했습니다.

---

### ④ Practical Risk Operations Experience

실무에서 가장 흥미를 느낀 부분은 **자동화된 RMS Alert를 그대로 처리하는 것이 아니라, 운영 데이터를 함께 검토하며 리스크를 재확인하는 과정**이었습니다.

대표 사례로 **신용불량으로 라벨링된 가맹점**을 검토한 경험이 있습니다.

해당 가맹점의 **EW 등급, 재무상태, 담보보증금 등 내부 관리 정보를 종합적으로 검토**하여 리스크 수준을 판단했고, 계약 기준에 따라 **최대 5일의 소명 기한**을 부여했습니다.

소명 회신이 지연되는 경우에는 **3일 경과 시점에 Outbound(OB) 연락을 요청**하여 회신을 독려했고, 최종적으로 제출된 소명 자료를 검토하여 내부 기준에 따라 후속 절차를 진행했습니다.

이 경험을 통해 **자동화된 Alert 결과뿐만 아니라 운영 데이터와 실제 정보를 함께 검토하여 사실관계를 확인하고, 내부 정책에 따라 리스크를 판단하고 의사결정을 지원하는 운영 역량**을 쌓을 수 있었습니다. 이 Merchant Risk 운영 경험을 토대로, **유저 단위 이상거래 탐지(User FDS) 및 Fraud Rule·시나리오 고도화로 확장할 수 있다**는 확신을 갖고 있습니다.

---

# 🎓 Research & Projects

## 🏆 Stablecoin Risk Health Score (SRHS)

스테이블코인의 건전성을 **사전에 평가하기 위한 Financial Risk Scoring Framework**를 연구했습니다.

### 연구 배경

Terra-LUNA 붕괴와 FTX 파산 등 연이은 시장 사건은 디지털 자산에 대한 신뢰를 크게 훼손했고, 대규모 자금 인출(Bank Run)과 유동성 위기를 초래했습니다.

이러한 사례는 **위험이 현실화된 이후 대응하는 방식만으로는 투자자와 시장을 보호하기 어렵다**는 점을 보여주었으며, 스테이블코인의 건전성을 **사전에 객관적으로 평가할 수 있는 정량적 기준**의 필요성을 시사했습니다.

기존 평가는 담보비율(Collateral Ratio)이나 페그(Peg) 유지 여부 등 일부 지표 중심으로 이루어져 **유동성, 준비자산의 신뢰성, 정보공개 수준 등 다양한 리스크 요인을 종합적으로 반영하지 못하는 한계**가 있었습니다.

이에 **사고 발생 이후의 사후 분석이 아닌, 사고 이전에 스테이블코인의 건전성을 정량적으로 평가할 수 있는 금융 리스크 평가 프레임워크인 SRHS(Stablecoin Risk Health Score)를 설계**했습니다.

### 주요 내용

SRHS는 스테이블코인의 건전성을 다음 **5개의 핵심 리스크 지표**로 평가하는 금융 리스크 모델입니다.

- **PD (Peg Deviation)** : 목표 가격 유지 안정성
- **LS (Liquidity Stability)** : 유동성 안정성
- **CR (Collateral Risk)** : 담보 건전성
- **TI (Transparency Index)** : 정보공개 투명성
- **RR (Reserve Reliability)** : 준비자산 신뢰성

각 리스크 요인을 정량화하여 하나의 **Risk Health Score**로 통합하고, 스테이블코인의 건전성을 객관적으로 비교·평가할 수 있는 **Risk Scoring Framework**를 제안했습니다.

### 연구 의의

이 연구를 통해

- 금융 리스크 정의
- Risk Factor 설계
- Risk Scoring Framework 구축
- 금융 리스크 정량화 모델 설계
- 데이터 기반 의사결정 지표 설계

역량을 쌓을 수 있었습니다.

이러한 경험은 현재 Toss CX에서 수행하고 있는 **Merchant Risk Review, RMS Labeling, Risk Assessment** 업무와도 자연스럽게 연결되고 있습니다.

### 연구 성과

🏆 **한국경영컨설팅학회 최우수 논문상**

📖 **KCI 등재지 『경영컨설팅연구』 제26권 제3호 논문 게재**

👨‍💻 **공동 저자**

📄 **Paper (PDF)**  
https://github.com/sojo1211/toss_FDS_ohsungjun/blob/master/SRHS.pdf

---

## 🏆 SafeFall Intelligence

**웨어러블 생체신호 기반 이상탐지(Anomaly Detection) 프로젝트**

### 역할

- 시계열(Time Series) 데이터 전처리
- 이상탐지(Anomaly Detection) 모델 설계
- Decision Label 기준 정의

### 사용 기술

`Python` `PyTorch` `LSTM` `Time Series Analysis`

### 성과

🏆 용인대학교 창업경진대회 최우수상

### 프로젝트 의의

사람마다 패턴이 달라 고정 임곗값이 통하지 않는 문제는, 고객·거래마다 정상 패턴이 제각각인 **이상 거래 탐지(FDS)** 문제와 본질적으로 같은 구조라고 생각합니다. 정해진 규칙이 아니라 데이터 안에서 위험의 경계를 알고리즘이 스스로 찾도록 설계했던 경험은, 토스뱅크에서 **고정 룰만으로 잡히지 않는 신종 사기 패턴을 비지도 학습으로 조기에 포착**하는 데 활용할 수 있습니다. 또한 센서 데이터 지연 0.5초가 사고를 막지 못하는 상황을 겪으며 "데이터 오류가 곧 실제 피해로 이어지는 도메인"의 무게를 체감했고, 이는 **실시간성이 중요한 결제·여신 FDS 운영**에도 동일하게 적용됩니다.

---

## 🏆 KB국민은행 제8회 AI Challenge

**소상공인 비대면 정책자금 사전검증 AI Agent 개발**

### 역할

- RAG 기반 AI Agent 개발
- LangChain 활용
- PDF/HWP 데이터 파이프라인 구축
- React 기반 UI/UX 개발

### 사용 기술

`LangChain` `RAG` `Python` `ChromaDB` `React`

### 프로젝트 의의

정책 문서를 기반으로 비대면 정책자금 신청 자격을 빠르게 검토할 수 있는 AI Agent를 개발했습니다. 이 RAG 아키텍처는 **이상거래 탐지 후 리스크 분석관의 판독 생산성을 높이는 'FDS 내부 규정·판례 탐색 RAG Agent'나 'Rule 가이드라인 자동 탐색 시스템'**으로 직접 확장 가능하다고 생각합니다.

---

# 🛠 Tech Stack

## Financial Risk

`FDS` `RMS` `AML` `TOI` `Paybiz`

## Data Analysis

`Python` `SQL` `Pandas` `NumPy` `scikit-learn`

## AI

`LangChain` `Claude Code` `RAG` `Vector DB`

## Collaboration

`Git` `React` `Tailwind CSS` `Figma` `Slack` `Notion`

---

# 📜 Certifications

- AML Basic
- SQLD · SQL Developer
- ADsP · 데이터분석 준전문가

---

# 💡 My Story

저는 **"사고를 탐지하는 것보다 사고를 예방하는 것이 리스크 관리의 본질"** 이라는 문제의식을 바탕으로 금융 리스크를 연구해왔습니다.

이러한 문제의식은 **SRHS(Stablecoin Risk Health Score)** 연구로 이어졌습니다. 스테이블코인의 건전성을 사전에 평가하기 위해 **5개의 핵심 리스크 지표(PD · LS · CR · TI · RR)** 를 설계하고, 이를 하나의 **Risk Health Score**로 통합하는 금융 리스크 정량화 모델을 제안했습니다. 해당 연구는 **한국경영컨설팅학회 최우수 논문상**과 **KCI 등재 논문 게재**라는 성과로 이어졌습니다.

연구를 통해 **리스크를 정의하고 정량화하는 방법**을 익혔다면, Toss CX에서는 **실제 금융 서비스에서 리스크를 운영하고 통제하는 경험**을 쌓았습니다.

현재는 **Merchant Onboarding Risk Review, RMS Labeling, 지급보류, 결제 OFF, MID 분리** 등 다양한 리스크 운영 업무를 수행하고 있으며, 특히 **자동화된 RMS Alert를 운영 데이터와 함께 재검토하고, 소명 절차와 운영 정보를 종합적으로 확인하여 리스크를 판단하는 과정**에서 가장 큰 흥미를 느꼈습니다.

이러한 경험을 통해 **데이터를 기반으로 리스크를 분석하고, 운영 관점에서 사실관계를 검증하며 의사결정을 지원하는 역량**을 쌓을 수 있었습니다.

또한 실무를 수행하면서 **거래 데이터뿐 아니라 가맹점의 신용도, 재무상태, 소명 자료 등 다양한 정보를 종합적으로 검토하여 리스크를 판단하는 과정에서 금융 범죄 예방과 규제 준수의 중요성**을 깊이 느꼈습니다. 이러한 경험을 계기로 **AML Basic 자격을 취득**했으며, 앞으로도 AML 전문 교육과 심화 학습을 통해 금융 범죄 대응 역량을 지속적으로 강화해 나갈 계획입니다.

앞으로는 **금융 리스크 모델링 연구 경험과 Toss CX에서의 리스크 운영 경험, 그리고 AML에 대한 이해를 바탕으로** 토스뱅크 **Anti-Fraud Manager**로서 데이터 기반 분석과 Fraud Rule 고도화에 기여하겠습니다. 특히 Merchant Risk 운영 경험을 토대로, **유저 단위 이상거래 탐지(User FDS), 대포통장·보이스피싱 예방, Fraud Rule·시나리오 고도화로 역량을 확장**하여 더욱 안전한 금융 서비스를 만드는 데 기여하고 싶습니다.

---

# 📫 Contact

📧 **Email**

**sungjun12110@gmail.com**

🐙 **GitHub**

https://github.com/sojo1211

📂 **Portfolio**

https://sojo1211.github.io/toss_FDS_ohsungjun/
