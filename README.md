# 📌 오성준 (Oh Sungjun) — Portfolio

<p align="center">
  <img src="./tossme.png" width="300" alt="오성준 프로필 사진" style="border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.1);" />
</p>

<p align="center">
  <strong>Financial Risk & KYC AI · Anti-Fraud Strategy · Business Risk Quantification · Stablecoin Research</strong>
</p>

<p align="center">
  📍 <strong>토스씨엑스(Toss CX) FDS Team 재직 중 (Operations Supporter / 리스크운영)</strong><br>
  🎯 <strong>Goal: 토스뱅크 Anti-Fraud Manager</strong>
</p>

<p align="center">
  📧 <a href="mailto:sungjun12110@gmail.com">sungjun12110@gmail.com</a> | 🎓 <a href="mailto:202278035@yiu.ac.kr">202278035@yiu.ac.kr</a> | 💻 <a href="https://github.com/sojo1211">GitHub</a>
</p>

---

## 💼 Professional Experience & Risk Operations

### 🔹 토스씨엑스 (Toss CX) FDS Team — Operations Supporter (리스크운영)
* **근무 기간:** 2026.07 ~ 현재 (연장 포함 운영 중)
* **주요 업무 및 성과:**
  * **온보딩 팩터 vs 실제 운영 갭 검수:** 가맹점 입점 시 등록된 6대 리스크 팩터(배송종류, 객단가, 판매형태, 실물/비실물 등)와 실제 웹사이트 및 거래 데이터 간의 불일치를 정밀 검수
  * **RMS 14대 기준 정량 라벨링:** RMS alert 발생 시 토스페이파트너스(TOI/Paybiz)를 통해 MID 기반으로 가맹점 웹사이트를 실사하고, 환금성·배송기간 초과·상품 변질 등 14가지 RMS 기준표에 의거해 리스크 사유 정량 라벨링 수행
  * **가입 시점 분기별 소명 및 공문 통제:** 
    * *2023년 07월 10일 이후 가입 건:* 약관 기준 전자 메일 소명 프로세스 집행
    * *2023년 07월 10일 이전 가입 건:* 내부 결재를 거친 공식 인감 공식 공문 발송 및 제재 통제
  * **선제적 자금 손실 차단:** 미소명 및 고위험 가맹점 대상 지급보류, 결제 OFF(연동 해제), 토스페이 비활성화 등 End-to-End 리스크 통제 실무 수행
  * **AML (Anti-Money Laundering) 역량 내실화:** 현직 리스크 운영 과정에서 자금세탁방지 및 이상거래 탐지/대응 프로세스 체득 완료

---

## 🔍 Data Deep Dive & Risk Quantification Philosophy

저에게 **Data Deep Dive**란 단순한 파이썬 문법 활용을 넘어, *데이터 이면의 이상 징후를 역추적해 실행 가능한 통제 Rule로 변환하는 분석적 사고*입니다.

1. **현장 모니터링 기반의 갭 포착 (Toss CX 실무)**
   * 온보딩 팩터와 실제 가맹점 운영 형태 간의 미스매치를 찾아내고, RMS 14대 기준으로 즉각적인 소명·공문 조치 및 결제 차단을 수행하는 실무형 통제 감각을 갖추고 있습니다.
2. **학술 연구를 통한 리스크 정량화 (SRHS 논문 주저자)**
   * 스테이블코인 붕괴 사례 데이터를 바탕으로 5개 핵심 리스크 지표(PD·LS·CR·TI·RR)를 정량화하는 프레임워크를 설계하여 한국경영컨설팅학회 최우수상 수상 및 KCI 등재지 게재를 달성했습니다.
3. **AI 및 데이터 검증 역량 (SafeFall & KB RAG)**
   * 파이썬(Pandas, PyTorch)과 RAG 기반 에이전트 파이프라인을 활용해 데이터 분석 타당성을 스스로 감사(Audit)하고 프로토타이핑할 수 있는 기술적 내실을 다졌습니다.

---

## 🚀 Core Projects (4대 핵심 프로젝트)

### 1️⃣ [Safe-Trade AI](https://sojo1211.github.io/2026_KB_AI_Challenge_Small-business-financial-agent_ohsungjun/) — 지능형 중고거래 사기 방지 시스템
* **프로젝트 성격:** KB AI Challenge (소상공인 금융 에이전트)
* **주요 내용:** 중고거래 플랫폼 내 빈번한 사기 피해를 방지하기 위해 금융권의 비대면 실명 확인(e-KYC) 프로세스를 이식한 안전 거래 시스템. 단순 이력 조회를 넘어 사기 이력 및 거래 패턴 맥락을 AI Agent(LangChain)가 분석하여 실시간 위험도를 산정하고 대응 가이드를 제공합니다.
* **수행 역할:** AI 구조 설계, LangChain 기반 위험 분석 Agent 프롬프트 엔지니어링, 신분증 OCR 추출 모듈 구현 및 민감정보 마스킹 설계.
* **사용 기술:** React 18, FastAPI (Python), LangChain (OpenAI GPT-4o), OCR 모듈, 공공데이터포털 API

### 2️⃣ [SRHS](https://github.com/sojo1211/SRHS-STABLECOIN-RISK-HEALTH-SCORE-) — Stablecoin Risk Health Score (스테이블코인 리스크 평가)
* **프로젝트 성격:** KCI 등재지 논문화 진행 중 & 학술대회 수상 프로젝트
* **주요 내용:** 스테이블코인 붕괴 사례 분석을 기반으로 실시간 리스크 평가를 수행하는 모니터링 시스템. USDT, USDC, DAI, PYUSD의 리스크를 5개 지표로 정량화합니다.
* **수행 역할:** 5대 핵심 리스크 지표(PD, LS, CR, TI, RR) 설계, 데이터 정량화 모델링 및 대시보드 차트 구현.
* **사용 기술:** React, CoinGecko API, DeFiLlama API, SVG Charting
* **주요 성과:** 🏆 **한국경영컨설팅학회 학술대회 최우수상**

### 3️⃣ [SafeFall Intelligence](https://github.com/sojo1211/SafeFall/tree/ict-safefall_project) — 낙상 사고 예측 AI 플랫폼
* **프로젝트 성격:** 창업경진대회 수상 프로젝트 (Code UP 동아리 활동)
* **주요 내용:** 다중 바이오신호(IMU·HRV·SpO₂) 기반 사고·위험 예측 실시간 모니터링 서비스. K-Means 알고리즘을 활용해 사용자별 낙상 전조 신호 경계를 규명하고 사고를 사전에 예방합니다.
* **수행 역할:** **팀장** / AI 구조 설계 / 센서 데이터 전처리 및 Feature Engineering / 의사결정 경계(정상·미끄러짐·낙상) 설계
* **사용 기술:** PyTorch, RandomForest, K-means, Linear Regression, IMU/HRV/SpO2 센서 데이터 분석
* **주요 성과:** 🏆 **용인대 제2회 창업아이디어 경진대회 최우수상**

### 4️⃣ [DSA Project](https://github.com/sojo1211/DSA_project) — IT 아웃소싱 플랫폼 소비자 분석
* **프로젝트 성격:** 실무 데이터 분석 프로젝트
* **주요 내용:** IT 아웃소싱 플랫폼 소비자 니즈 데이터를 분석하여 최적의 수수료율 책정 및 타겟 세그먼트별 마케팅 전략 도출.
* **수행 역할:** **단독 수행** / 거래 로그 및 프로필 데이터 병합 / 차등 수수료율 및 타겟 마케팅 세그먼트 정량 도출
* **사용 기술:** Python, Pandas, Matplotlib, Seaborn, 통계 분석
* **주요 성과:** 🏆 **데이터스테이션 실무 데이터 분석 프로젝트 최우수상**

---

## 🏆 Awards & Achievements

* **2026** | 🏆 **한국경영컨설팅학회 학술대회 최우수상** (SRHS 프로젝트)
* **2025** | 🏆 **용인대 제2회 창업아이디어 경진대회 최우수상** (SafeFall 프로젝트, 팀장)
* **2025** | 🏆 **데이터스테이션 실무 데이터 분석 프로젝트 최우수상** (DSA 프로젝트, 개인)
* **2025** | 🥉 **단국대학교 단국 창업 해커톤 장려상** (Agri-SCM Intelligence 프로젝트, G7 분야)

---

## 🛠️ Tech Stack & Domain

| 분류 | 보유 기술 |
| --- | --- |
| **Programming & Data** | Python, SQL, Pandas, NumPy, scikit-learn, PyTorch, TensorFlow, MySQL |
| **Backend** | Java, Spring Boot |
| **AI & Research** | LangChain, HuggingFace, Ollama, Chroma DB <br>*(Key Focus: RAG, 시계열 분석, Classification, Clustering)* |
| **Financial Domain** | Risk Quantification, KYC, AML, Stablecoin Risk, 정책자금 검증, PG Risk |
| **Frontend & Tools** | React (v18), Git, Figma, Notion, Claude Code *(바이브코딩 · AI-Native Dev)* |

---

## 🎓 Education & Certifications

### 🏫 Education
* **용인대학교** (2022.03 ~ 현재)
  * AI학과 & AI비즈니스 융합전공 (3학년 2학기 재학 중)
  * 학점(GPA): **3.85 / 4.5**
  * AI Service Lab 부원 및 팀장 (RAG 기반 질의응답 모델 개발, 시계열 생체신호 분석 연구)
  * Code UP 창업동아리 팀장

### ✍️ Certifications & Courses
* **SQLD (SQL Developer)** | 한국데이터산업진흥원 (자격번호: SQLD-054001255)
* **ADsP (데이터분석 준전문가)** | 한국데이터산업진흥원 (2026.02 취득)
* **AML (자금세탁방지) 기초 자격 취득**
* **융합보안 인력양성 교육(클라우드 심화)** | 한국정보보호산업협회 (2024.12)
* **대학생 기업경영체험스쿨 수료** | DB 인재개발원 (2025.02)
* **금융사관학교 68기 수료 & 서포터즈** | 금융사관학교 (2025.04)
* **퀀트 운용 직무 체험** | 코멘토 (현직 증권사 트레이더 지도, 2026.02)

---

## 🎯 Career Goal: 토스뱅크 Anti-Fraud Manager

### 💡 My Story: '설계'에서 '실무'로, 그리고 토스뱅크의 'Anti-Fraud 고도화'로

#### 1️⃣ 문제의식의 시작: "금융 거래와 자산의 신뢰성을 어떻게 사전에 검증할 것인가?"
저는 AI와 데이터를 공부하며 **“사고가 발생한 뒤 감지하는 것은 늦는다. 금융 자산과 거래의 신뢰성을 데이터 기반으로 사전 정량화하고 예방하는 것이 리스크 관리의 본질”**이라는 깊은 문제의식을 갖게 되었습니다. 

이 문제의식을 바탕으로 스테이블코인의 붕괴 리스크를 사전에 탐지하기 위해 **5대 핵심 리스크 지표(PD·LS·CR·TI·RR)를 설계**하고 정량화 모델을 수립하는 **SRHS 프로젝트**를 진행했습니다. 이 연구로 학술대회 최우수상을 수상하고 KCI 등재지 논문화(주저자)를 진행하면서, 데이터를 비즈니스 통제 지표로 가공하는 리스크 모델 설계의 초석을 다졌습니다.

#### 2️⃣ 실제 운영으로의 확장: "설계를 넘어, 실제로 작동하는 RMS(Risk Management System)의 현장으로"
하지만 리스크 모델은 이론에 머물러서는 안 되며, 실제 대규모 거래가 발생하는 금융 시스템 속에서 어떻게 작동하고 자금을 통제하는지 실증해야 한다고 믿었습니다. 이에 따라 **토스씨엑스(Toss CX) FDS Team의 Operations Supporter(리스크운영)**로 합류하여 생생한 실무에 뛰어들었습니다. 

가맹점 입점 시 등록된 6대 팩터와 실제 운영되는 실데이터 사이의 정교한 갭(Gap)을 포착하고, 14대 RMS 기준에 맞춰 리스크 사유를 정량 라벨링했습니다. 더 나아가 고위험 가맹점 대상의 소명 프로세스 집행, 인감 날인 공식 공문 발송 제재, 그리고 최종 결제 OFF 및 지급보류까지 리스크 통제의 최전선에서 전 과정을 직접 직접 운영했습니다.

#### 3️⃣ 현장에서 찾은 흥미: "자동화 룰의 틈새를 메우는 통제와 AML"
실무에서 데이터를 매일 모니터링하며 가장 큰 흥미를 느낀 지점은 **“시스템이 정의한 자동화 룰과 실제 우회/변칙 거래 데이터 사이에 존재하는 미세한 틈새를 포착하고 메워나가는 과정”**이었습니다. 

특히 이상거래 탐지뿐만 아니라 가맹점과 거래 흐름 전반의 규제 준수 여부를 검증하는 일에 깊은 매력을 느꼈습니다. 실무를 수행하며 리스크 통제 프로세스의 고도화에 큰 열정을 가져, 이미 **AML(자금세탁방지) 기초 자격을 취득**하였으며 향후 **전문 AML 교육 및 심화 자격 이수**까지 계획하고 있습니다.

#### 4️⃣ 미래의 도약: "토스뱅크 비대면 여신의 Anti-Fraud 고도화"
이러한 **이론적 리스크 설계(SRHS 논문) ➡️ 실제 FDS 운영 실무(Toss CX) ➡️ 고도화된 통제(AML 기초 자격 취득 및 심화 계획)**로 이어지는 저의 성장 스토리의 종착지는 **토스뱅크의 Anti-Fraud Manager**입니다.

현장에서 체득한 '실무형 리스크 운영 감각(Operations)'을 토스뱅크의 비대면 소매 여신(SOHO, 전월세대출 등) 심사 및 신청 단계에 이식하고 싶습니다. 신청 시점의 이상 패턴을 데이터 Deep Dive(Python/SQL)를 통해 분석하고, 트렌드를 즉각 반영하는 지능형 Fraud-Rule을 설계하여 토스뱅크의 금융 생태계를 가장 안전하게 지켜내고 고도화하겠습니다.
