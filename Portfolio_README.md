# 📌 오성준 (Oh Sungjun) – Portfolio

<p align="center">
  <img src="https://raw.githubusercontent.com/sojo1211/toss_FDS_ohsungjun/master/성준사진.jpg" width="260" alt="오성준 프로필"/>
</p>

### Yongin University · AI & AI Business Convergence Major
### Toss CX FDS Team / Pay Risk Management Team (Operations Supporter)
### Target Position: Toss Bank Anti-Fraud Manager / Risk Operations & Analyst

> **Toss CX FDS/RMS 리스크 운영 실무 경험, 금융 리스크 정량화 모델링 연구(SRHS 최우수 논문상·KCI 등재), 그리고 AI/RAG 파이프라인 설계 역량을 갖춘 리스크 통제 전문가 오성준입니다.**

---

## 📧 Contact & Channel

* **Personal Mail**: sungjun12110@gmail.com
* **School Mail**: 202278035@yiu.ac.kr
* **GitHub**: [github.com/sojo1211](https://github.com/sojo1211)
* **Web Portfolio**: [sojo1211.github.io/toss_FDS_ohsungjun](https://sojo1211.github.io/toss_FDS_ohsungjun/)

---

## 🚀 About Me

* **이론적 연구와 실무 제재 프로세스의 융합**: 금융 리스크 정량화 모델(SRHS)을 직접 설계하고 백테스팅으로 **오탐률(False Positive)과 정상 유저 UX 마찰을 최소화하는 최적 임곗값(Threshold)**을 검증한 연구 경험과, Toss CX 현장에서 가맹점 리스크(Merchant Risk) 및 제재 업무를 직접 운영한 실무 감각을 모두 갖추고 있습니다.
* **비지도 학습 & 유저 시계열 로그 이상 탐지 역량**: 유저의 서비스 이용/이체 로그(시계열) 및 IP/디바이스 식별자 전처리 역량을 바탕으로, 사람이 고정된 규칙(Rule)으로 정의할 수 없는 이상 패턴을 데이터 군집화(K-Means, RandomForest 등) 알고리즘을 통해 탐지 경계선을 스스로 도출해내는 모델을 설계했습니다.
* **설명 가능하고 신뢰할 수 있는 RAG Agent 설계**: 환각(Hallucination)을 제어하고 근거 문서에 기반해 정확히 검수·답변하는 AI RAG 파이프라인 개발 경험을 가지고 있습니다.

---

## 💼 Work Experience

### 🔥 2026.07 ~ 2027.01.19 (6개월) | Toss CX FDS Team / Pay Risk Management Team
**Operations Supporter (리스크 운영supporter)**
* **Merchant Onboarding Risk Review**: 가맹점 입점 검수 시 6대 Risk Factor(배송 방식/기간, 최고 객단가, 판매 형태 등)와 웹사이트 운영 상태 교차 검증 및 선제적 리스크 차단.
* **RMS Labeling & Control**: TOI / Paybiz 시스템을 활용해 RMS Alert 발생 건을 MID 단위로 추적하고, 14대 RMS 기준에 따라 리스크 등급 라벨링 및 조치 집행(지급보류, 결제 OFF, MID 분리).
* **Practical Risk Assessment & Rule 고도화**: 일 60여 건 이상 유입되는 RMS Alert 중 주요 건을 선별하여 **4단계 재검토 프로세스(Moderate 등급 검토·테마점검·뉴스동향 모니터링·소명 및 OB 검증, 월 400건 이상 수행)**를 수행하고, 지급보류/MID 분리 등 선제적 운영 통제를 집행. 오탐 감소 및 판독 효율화를 위한 3가지 FDS/RMS 룰 개선 방안(복합 조건 스코어링, 소명 완결 건 예외 필터링, 테마 연계 Dynamic Rule)을 제안 및 공유.
* **Anti-Fraud 확장성**: 현장 리스크 통제 노하우와 유저 로그 데이터(IP/디바이스 식별자, 이체 시계열) 전처리 역량을 바탕으로 유저 단위 이상거래 탐지(User FDS: 보이스피싱/명의도용/대포통장 예방), Fraud Rule 고도화 역량 확보.

---

## 🎖️ Awards & Achievements

| 연도 | 대회/학술명 | 주관/게재지 | 수상/성과 | 관련 프로젝트 |
| :--- | :--- | :--- | :--- | :--- |
| **2026** | **한국경영컨설팅학회 춘계학술대회** | 한국경영컨설팅학회 | 🥇 **최우수 논문상** | Stablecoin Risk Health Score (SRHS) |
| **2026** | **KCI 등재지 논문 게재** | 『경영컨설팅연구』 (제26권 제3호) | 📄 **주저자 등재** | SRHS 프레임워크 연구 |
| **2025** | **용인대 제2회 창업아이디어 경진대회** | 용인대학교 | 🥇 **최우수상** | SafeFall Intelligence |
| **2025** | **단국대학교 창업 해커톤** | 단국대학교 | 🥉 **장려상 (G7 분야)** | Agri-SCM Intelligence |
| **2025** | **실무 데이터 분석 프로젝트** | 데이터스테이션 | 🥇 **최우수상** | DSA IT 아웃소싱 분석 |

---

## 🧑💻 Featured Projects

### 1️⃣ Stablecoin Risk Health Score (SRHS)
* **내용**: B2B 무역결제 등에서 활용되는 스테이블코인의 건전성을 사전에 평가하기 위한 **Financial Risk Scoring Framework** 연구.
* **담당 역할**: 5대 핵심 리스크 지표(PD·LS·CR·TI·RR) 설계, Ridge Regression을 활용한 가중치 설계 및 FTX·Terra-Luna 등 실제 위기 데이터를 복원한 백테스팅 및 민감도 분석(위기 5일 전 조기 경보, 오경보 0건 검증 완료).
* **Anti-Fraud 적용**: 여신·대출 심사 단계에서 신청 데이터로 사전 이상 거래 점수를 산출하고, 실제 사기 사례 데이터를 통한 룰 백테스팅으로 **정상 유저 UX 마찰을 최소화하는 오탐률(False Positive) 관리 및 최적 임곗값(Threshold) 설계**에 기여.
* **Paper (PDF)**: [SRHS.pdf](https://github.com/sojo1211/toss_FDS_ohsungjun/blob/master/SRHS.pdf)

### 2️⃣ SafeFall Intelligence
* **내용**: 다중 바이오센서 시계열 데이터를 활용해 사고 이전 단계의 이상 징후를 예측하는 **비지도 학습 기반 이상탐지(Anomaly Detection) 시스템**.
* **담당 역할**: 시계열 센서 데이터 노이즈 필터링 및 상관분석 시각화, 비지도 학습(K-Means) 기반 정상/전조증상 라벨링 기준 도출, Transfer Learning(특징 추출 방식)을 통한 Anomaly Detection 모델 설계 (F1-Score 82% 달성).
* **Anti-Fraud 적용**: 유저의 서비스 이용/이체 로그(시계열) 및 IP/디바이스 식별자 전처리 경험을 바탕으로, 사용자별로 정상 거래 패턴이 제각각인 **개인 유저 단위 이상거래 탐지(User FDS)** 영역에서 **비지도 학습 군집화 모델을 통한 보이스피싱, 명의도용, 대포통장, 작업대출 등 신종/우회 금융 사기 패턴 조기 포착**에 활용.
* **Repo**: [SafeFall Repository](https://github.com/sojo1211/SafeFall/tree/ict-safefall_project)

### 3️⃣ KB국민은행 제8회 AI Challenge (현직자 PICK)
* **내용**: 흩어진 오프라인 정책 문서로부터 환각 없이 신뢰성 있는 금융 근거를 인용해 답변하는 **RAG 기반 금융 AI Agent**.
* **담당 역할**: PDF/HWP 문서의 Markdown 구조화 데이터 전처리 파이프라인 개발, ChromaDB 벡터DB 구축, 시스템 프롬프트(안내 지침서) 설계 및 React UI 구축.
* **Anti-Fraud 적용**: 리스크 분석관의 FDS/AML 의사결정 생산성을 높이기 위한 **'내부 FDS 가이드라인 및 규정 자동 검색 RAG Agent'** 혹은 **'이상거래 탐지 사유 설명 생성 시스템'**으로 확장.
* **Demo**: [데모 사이트 보기](https://sojo1211.github.io/2026_KB_AI_Challenge_Small-business-financial-agent_ohsungjun/)

---

## 🛠 Tech Stack

### 🛡️ Risk & Compliance
* `FDS (이상거래탐지)` `RMS (가맹점리스크관리)` `AML (자금세탁방지)` `TOI` `Paybiz`

### 📊 Data Analysis & Model
* `Python` `SQL` `Pandas` `NumPy` `scikit-learn` `PyTorch` `LSTM` `RandomForest` `K-Means`

### 🤖 Generative AI
* `LangChain` `ChromaDB (Vector DB)` `RAG System` `Claude Code`

### 🤝 Collaboration & Frontend
* `Git` `React` `Tailwind CSS` `Figma` `Slack` `Notion`

---

## 📚 Education & Certifications

### 🎓 Education
* **용인대학교 (2022.03 ~ 현재)**: AI학과 · AI비즈니스 융합전공 (GPA 3.81)
* **AI Service Lab (2025.03 ~ 현재)**: 연구실 팀장 (RAG QA, 시계열 분석, ML/DL 모델링)
* **Code UP 창업동아리 (2025.09 ~ 2026)**: 팀장 (SafeFall Intelligence 프로젝트 리드)
* **금융사관학교 (2025.04)**: 68기 수료 및 서포터즈 활동 (리스크 관리 체계 수록)
* **DB 인재개발원 (2025.02)**: 대학생 기업경영체험스쿨 (데이터 기반 의사결정 체험)
* **한국정보보호산업협회 (2024.12)**: 융합보안 인력양성 클라우드 심화 과정 이수
* **금융 퀀트 직무체험 (2026.02)**: 현직 증권사 트레이더 연계 퀀트 운용 직무 이수

### 📜 Certifications
* **AML Basic** (한국금융연수원 자금세탁방지 핵심요원 기초 과정 이수)
* **SQLD · SQL Developer** (한국데이터산업진흥원, 자격번호: `SQLD-054001255`)
* **ADsP · 데이터분석 준전문가** (한국데이터산업진흥원 수여)

---

## 🌟 포부 (Aspiration)

> **"지능형 통제와 완벽한 실무 운영으로 금융의 신뢰를 지킵니다."**

데이터 분석과 AI 모델링을 통해 보이스피싱, 낙상, 공급망 리스크 등 다양한 위험 예측 프로젝트를 총괄하며, 데이터의 작은 오차가 사람의 안전과 실제 금융 피해로 이어질 수 있다는 사실을 체감했습니다.

이 과정에서 금융 도메인의 핵심 리스크 통제 시스템에 깊은 흥미를 가지게 되었고, **Toss CX FDS Team / Pay Risk Management Team**에 합류하여 가맹점 심사, RMS Alert 분류, 4단계 재검토 프로세스(월 400건 이상) 수행 및 FDS/RMS 룰 개선 방안을 제안하며 금융 혁신의 최전선에서 리스크 운영 실무를 성공적으로 수행해 냈습니다.

앞으로 토스뱅크의 **Anti-Fraud Manager**로서,
1. **정량적 분석 능력**: Python/SQL Deep Dive 및 유저 시계열 로그(IP/디바이스, 이체 패턴 등) 전처리를 통한 소매 여신 및 전월세대출 심사 사기 패턴 사전 탐색
2. **실무 운영 감각**: 가맹점과 개인 유저 단위를 아우르고 오탐률(False Positive)과 유저 UX 마찰을 최소화하는 실용성 높은 FDS/RMS Rule의 지속적인 설계 및 업데이트
3. **지능형 통제 역량**: 비지도 학습을 접목한 변칙 사기 패턴 선제 규명 및 규제 준수(Compliance/AML) 체계 고도화

이 세 가지 축을 토대로 오탐을 최소화하면서 탐지 정확도를 극대화하여, 사용자가 가장 안심하고 사용할 수 있는 금융 플랫폼 토스뱅크를 만드는 리스크 관리 주역이 되고 싶습니다.
