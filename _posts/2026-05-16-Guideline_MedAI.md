# AI가 가이드라인을 만날 때

가이드라인은 전 세계의 의사들이 따르는 표준입니다. 한국어로는 진료지침이라고 번역되기도 하죠. Evidence of pyramid에서도 가이드라인은 거의 최상단의 높은 근거 수준에 위치합니다. 그렇다면 의료인공지능 제품들이 가이드라인에 들어간 것들에는 무엇이 있을까요? 그리고 그것들은 어떻게 해서 들어갔고 어디까지 임상적 역할을 부여받는 것일까요?

2021년 ACC/AHA 관상동맥 가이드라인에 HeartFlow의 FFR-CT가 Class 2a 권고로 정식 등재된 사건을 시작으로, 지난 5년간 주요 학회의 임상 가이드라인은 AI를 빠른 속도로 흡수해 왔습니다. NICE는 2024년 stroke imaging AI 3종에 조건부 사용을 권고했고, ADA와 AAO는 LumineticsCore를 비롯한 자율 AI 시스템을 당뇨망막병증 스크리닝의 대안으로 명문화했습니다. ESTI는 2025년 폐결절 관리 권고에서 volumetry와 Volume Doublint Time (VDT) 계산을 사실상 AI 의존적인 의사결정 변수로 만들었고, NCCN은 2026년 유방암 스크리닝 가이드라인에서 imaging-based AI risk model을 Gail Model과 동등한 위험 평가 도구로 등재했습니다.

이 글은 이 다섯 가지 가이드라인을 한 자리에 모아, 각 문서가 AI에 정확히 어떤 역할을 부여했는지 분석합니다. 다섯 사례를 한꺼번에 놓고 보면, 가이드라인이 AI에 부여하는 역할이 동일하지 않다는 점이 분명히 드러납니다. HeartFlow의 FFR-CT는 functional assessment 도구로, NICE의 stroke AI는 의료진 검토를 전제로 한 보조 도구(adjunct)로, LumineticsCore는 의사 감독 없이 진단을 내리는 자율 AI(autonomous AI)로, ESTI의 결절 관리 AI는 volumetric measurement의 표준 인프라로, NCCN의 유방암 AI는 future risk prediction이라는 별도의 임상적 진입점으로 자리잡았습니다.

# ACC/AHA 2021: HeartFlow - FFR-CT

AI를 통틀어, [2021 ACC/AHA/SCAI Guideline for Coronary Artery Revascularization: A Report of the American College of Cardiology/American Heart Association Joint Committee on Clinical Practice Guidelines](https://www.jacc.org/doi/10.1016/j.jacc.2021.09.006)에서 최초로 AI를 가이드라인에 정식으로 등재하게 되었습니다.

## 권고 등급 및 적응증

가이드라인은 FFR-CT를 여러 임상 상황에서 Class 2a로, 그리고 광범위한 협착 범위(직경 기준 40%~90%)에 걸쳐 권고하고 있습니다. 근거 수준은 B-NR (비무작위 연구 기반 중등도 근거)이며, COR 2a로 이익이 위험을 상회한다는 중등도 강도의 권고에 해당합니다. [출처 (JACC)](https://www.jacc.org/doi/10.1016/j.jcmg.2022.02.021), [출처 (CMS)](https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?LCDId=38839)

급성·만성 안정형 흉통 증후군 전반에 대해 총 4개의 FFR-CT 관련 권고가 포함되었습니다. [출처 (PubMed Central)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8722020/)

## 구체적인 임상 적응증 (세 가지 환자군)

CMS LCD에 정리된 가이드라인 인용에 따르면, FFR-CT는 다음 환자군에서 vessel-specific ischemia 진단 및 ICA 결정에 유용합니다:

- 중등도 위험이고 기존에 알려지지 않은 근위부/중간부 관상동맥의 40–90% 협착 [출처 (CMS)](https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?LCDId=38839)
- 중등도 위험의 급성 흉통이면서 근위부/중간부 관상동맥의 40–90% 협착이 알려진 경우 [출처 (CMS)](https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?LCDId=38839)
- CCTA에서 40–90% 협착이 발견된 안정형 흉통의 알려진 비폐쇄성 관상동맥 질환 [출처 (CMS)](https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?LCDId=38839)

## HeartFlow의 위치

가이드라인 본문에서 HeartFlow를 상품명으로 명시하지는 않지만, 실질적으로 등재된 FFR-CT는 HeartFlow의 기술입니다. 관련 분석 논문은 FFR-CT가 현재 단일 회사(HeartFlow, Redwood City, California, USA)에서만 제공된다고 명시하고 있으며, CCTA 케이스 중 비교적 artifact-free한 일부에서만 가능하며, 이전 스텐트 삽입, 광범위 석회화, 중증 판막 질환, 순차적 협착 병변, 또는 CABG 과거력이 있는 환자에서는 제한적이라는 실용적 제약이 함께 제시됩니다. [SpringerSpringer](https://link.springer.com/article/10.1186/s12968-021-00835-z)

## 알고리즘 및 결정 흐름에서의 역할

- 평가 알고리즘에서 "High-risk CAD"의 정의에 left main 협착 ≥50% 또는 FFR-CT ≤0.80인 폐쇄성 CAD가 포함되어, FFR-CT 결과가 침습적 관상동맥조영술(ICA) 결정에 직접 활용되도록 구조화되었습니다. [JACC](https://www.jacc.org/doi/10.1016/j.jacc.2021.07.052)
- FFR-CT는 turnaround time이 신속한 임상 결정에 영향을 줄 수 있으나, 추가 검사가 필요한 stress testing과 달리 별도 검사 없이 사용 가능하다는 점이 명시됩니다. [AHA Journals](https://www.ahajournals.org/doi/10.1161/cir.0000000000001030)
- CCTA에서 근위부/중간부 혈관에 40–90% 협착이 있을 때 안정형 및 급성 흉통 환자 모두에서 후속 검사 옵션으로 Class 2a 권고로 제시되었습니다. [JACC](https://www.jacc.org/doi/10.1016/j.jcmg.2021.10.005)

이 가이드라인은 FFR-CT를 CT angiography (CTA)에서 검출된 40–90% 병변에 대한 허혈 가능성 평가 및 의사결정의 견고한 도구로 폭넓게 기술하고, flow chart 전반에서 다른 기능적 영상 modality와 동등한 Class 2a 권고로 배치함으로써, CCTA 기반 anatomical assessment를 functional assessment로 확장하는 핵심 도구로서 FFR-CT를 공식적으로 자리매김시켰다는 점에서 의의가 있습니다. 이는 사실상 HeartFlow의 기술이 미국 주요 학회 가이드라인에 처음으로 본격 등재된 사건으로 평가됩니다. [PubMed CentralPubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC8722020/)

# NICE DG57 2024: Stroke Imaging

NICE는 2024년 1월 23일에 DG57을 발표했고, 5월 2일 업데이트를 거쳐 현재는 HealthTech guidance 708(HTG708)로 이관되었습니다. 가이드라인 내용 자체는 변경되지 않았고, NHS HealthTech 프로그램 체계 정비에 따른 재분류가 된 것입니다. [NICE](https://www.nice.org.uk/guidance/htg708)

핵심 메시지는 명확합니다: 의심 뇌졸중 환자의 CT 뇌 영상 분석·판독을 보조하는 데 e-Stroke, RapidAI, Viz 3가지 AI 소프트웨어 사용을 권고하되, CT 스캔은 항상 의료진의 검토를 함께 거쳐야 한다는 것입니다. [NICE](https://www.nice.org.uk/guidance/dg57/informationforpublic)

## **AI가 담당하는 임상적 역할**

크게 네 가지 축으로 정리됩니다.

1. CT 영상에서의 자동 분석. AI 알고리즘이 CT 뇌 영상을 분석해 변화 및 이상 소견을 찾고 결과를 보고하면, 의료진이 스캔과 결과를 검토하는 구조입니다. 구체적으로 RapidAI를 예로 들면 Rapid ICH(비조영 CT에서 뇌내출혈 검출), Rapid ASPECTS(대혈관 폐색에 의한 허혈성 뇌졸중에서 비조영 CT 기반 병변 범위 평가), Rapid CTA, Rapid LVO(CTA에서 대혈관 폐색 검출 및 위치 파악), Rapid CTP(CT 관류영상 분석으로 구제 가능 뇌조직 정보 제공)로 구성됩니다. Viz도 Viz ICH(비조영 CT 두개내 출혈 검출), Viz LVO(CTA 대혈관 폐색 검출), Viz CTP(CT 관류영상의 구제 가능 조직 분석) 모듈을 제공합니다. [NICE](https://www.nice.org.uk/guidance/dg57/informationforpublic)
2. 치료 결정의 가속화. AI 소프트웨어는 의료진의 CT 판독과 함께 사용되어 뇌졸중에서의 의사결정-예를 들어 thrombolysis와 thrombectomy 결정-을 안내하고 가속화하는 데 쓰입니다. [NICE](https://www.nice.org.uk/guidance/dg57/chapter/1-Recommendations)
3. 센터 간 영상 공유 및 원격 판독. 서로 다른 뇌졸중 센터 간에 공유된 영상이 원격에서 검토 가능하도록 보장해야 하며, 이를 통해 다른 부지의 의료진이 의사결정에 참여할 수 있도록 합니다. 1차 뇌졸중 센터(Primary Stroke Center; PSC)에서 영상을 찍고 종합 뇌졸중 센터(Comprehensive Stroke Center; CSC)의 전문가가 즉시 판단하는 hub-and-spoke 모델에서 결정적입니다. [NICE](https://www.nice.org.uk/guidance/dg57/chapter/1-Recommendations)
4. 보조적 역할의 명확한 한계. AI는 단독 판독 도구가 아니며, 소프트웨어는 의료진 검토와 함께만 사용되어야 하고, 잘못된 결과의 위험을 줄이기 위해 기존 영상 판독 프로토콜을 유지해야 합니다. [NICE](https://www.nice.org.uk/guidance/dg57/chapter/1-Recommendations)

## **분류 - 단계별 접근**

세 갈래로 나뉩니다.

### 첫째, **근거 생성 조건부 사용 권고**(use with evidence generation)

e-Stroke, RapidAI, Viz는 적절한 Digital Technology Assessment Criteria (DTAC) 승인을 받은 후에만 NHS에서 사용 가능합니다. [NICE](https://www.nice.org.uk/guidance/dg57/chapter/1-Recommendations)

### 둘째, **연구 목적 한정**

Accipio, Aidoc, BioMind, BrainScan CT, Cercare, CINA Head, CT Perfusion 4D, icobrain ct, Neuro Solution, qER 등 10개 소프트웨어는 추가 연구가 필요한 단계입니다. [NICE](https://www.nice.org.uk/guidance/dg57/informationforpublic)

### 셋째

Viz는 2024년 5월 업데이트에서 CE mark 등급이 충분히 높아져 recommendation 1.1에 포함되었습니다. [NICE](https://www.nice.org.uk/guidance/htg708)

## **근거 수준에 대한 NICE의 솔직한 평가**

소프트웨어에 대한 임상 근거의 질은 제한적이며, 의료진 검토와 병행 사용 시 진단 정확도에 대한 근거는 리뷰 포함 기준을 충족하는 것이 없다고 명시합니다. 3개 기술(e-Stroke, RapidAI, Viz)에 대한 일부 임상연구는 소프트웨어 사용 후 환자들이 더 빠르거나 더 많은 치료 접근성을 얻었음을 시사하지만, 이것이 어느 정도까지 소프트웨어의 효과인지는 불명확합니다. 경제성 모델에서는 AI 소프트웨어로 인해 thrombectomy를 받는 사람이 소폭 증가한다면 비용효과적일 가능성이 높습니다. [NICE](https://www.nice.org.uk/guidance/dg57/chapter/1-Recommendations)
NICE는 "엄격한 RCT 근거 부재"를 인정하면서도 "이미 NHS 96% 센터에서 사용 중"이라는 현실과 "잠재적 임상 이익"을 고려해 조건부 사용 + 실세계 근거 생성이라는 절충안을 택했습니다.

### **근거 생성 계획 (Evidence Generation Plan)**

NICE는 후속 평가를 위한 데이터 수집 경로를 함께 제시했습니다. 기존 영상 데이터를 활용한 실험적 일치도 연구(experimental concordance study)와 SSNAP(Sentinel Stroke National Audit Programme) 데이터 평가가 두 축입니다. 구체적으로는 뇌졸중 센터에서 익명화된 대표 영상 세트를 제공받아 e-Stroke, RapidAI, Viz로 처리한 결과와 AI 미사용 결과를 비교하고, 자격을 갖춘 의료진이 후향적으로 평가해 무치료/혈전용해/혈전제거 권고를 비교하는 full factorial 설계가 제안되었습니다. [NICE](https://www.nice.org.uk/guidance/dg57/resources/evidence-generation-plan-for-artificial-intelligence-ai-software-to-help-clinical-decision-making-in-stroke-13306020301/chapter/3-Approach-to-evidence-generation)
또한 2023년 6월 DHSC가 발표한 £2,100만 규모의 AI Diagnostic Fund와 NIHR, NHS England 협력하의 in-service evaluation, 그리고 2개 NHS 영상 네트워크에서 시범 운영 중인 AI Deployment Platform이 근거 생성을 뒷받침합니다. [NICE](https://www.nice.org.uk/guidance/dg57/resources/evidence-generation-plan-for-artificial-intelligence-ai-software-to-help-clinical-decision-making-in-stroke-13306020301/chapter/1-Purpose-of-this-document)

# ADA, AAO Diabetic Retinopathy PPP: Digital Diagnostics - LumineticsCore

LumineticsCore는 다음 두 주요 가이드라인에 명시적으로 이름이 등재되어 있습니다.

1. ADA Standards of Care in Diabetes (American Diabetes Association)
2025년판(Section 12: Retinopathy, Neuropathy, and Foot Care) 및 2026년판 모두
    1. "FDA 승인을 받은 mild DR 이상 및 diabetic macular edema(DME)를 검출하는 AI 시스템은 전통적 스크리닝 접근법에 대한 대안을 나타낸다. 당뇨망막병증 스크리닝 및 검사를 위해 FDA가 승인한 3개의 AI 플랫폼은: AEYE diagnostic screening technology(AEYE-DS, AEYE Health), EyeArt AI screening system(Eyenuk), 그리고 LumineticsCore(구 IDx-DR, Digital Diagnostics)이다." [Diabetes Journals](https://diabetesjournals.org/care/article/48/Supplement_1/S252/157552/12-Retinopathy-Neuropathy-and-Foot-Care-Standards)
    2. 2026년판에서도 동일하게 유지되었고, 한 가지 추가된 문구는 "이 서비스들은 대부분의 보험 플랜에서 보장된다. 각 플랫폼에 대해 진단 정확도에 관한 prospective multicenter clinical trial이 출판되었다"는 점입니다. [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690177/)
2. AAO Diabetic Retinopathy Preferred Practice Pattern (PPP)
    1. 2025년 2월 7일 Ophthalmology 저널에 출판된 American Academy of Ophthalmology Preferred Practice Pattern Retina/Vitreous Committee의 Diabetic Retinopathy PPP(Lim JI 등, 2025)는 자율 AI 시스템을 DR 스크리닝의 대안 도구로 인정하고 있으며, LumineticsCore가 대표 사례로 인용됩니다. [Guideline Central](https://www.guidelinecentral.com/guideline/10563/)

## 가이드라인 안에서 AI의 정확한 역할

ADA Standards of Care 텍스트를 그대로 보면 AI의 역할이 매우 명확히 규정되어 있습니다.

### 역할 1 - 전통적 안과 검사의 "대안적 스크리닝(alternative screening)" 도구

핵심 단어가 "alternative to traditional screening approaches"입니다. 이는 NICE DG57의 stroke AI가 "보조 도구(adjunct)"로 규정된 것과 본질적으로 다른 위치입니다. AI가 dilated comprehensive eye exam을 완전히 대체하지는 않지만, **스크리닝 단계에서는 독립적인 진단 경로**로 인정된다는 의미입니다.

### 역할 2 - Mild DR 이상 및 DME 검출

가이드라인이 명시하는 AI의 임상 task는 "FDA 승인을 받은 mild DR 이상 및 diabetic macular edema를 검출"입니다. 즉 모든 DR 단계를 정밀 분류하는 것이 아니라, **치료가 필요할 수 있는 임계점(mild 이상)을 넘었는지 여부를 판별**하는 binary 의사결정 지원입니다. [Diabetes Journals](https://diabetesjournals.org/care/article/48/Supplement_1/S252/157552/12-Retinopathy-Neuropathy-and-Foot-Care-Standards)

### 역할 3 - 후속 조치를 위한 트리아지(Triage)

ADA는 AI 결과 후 워크플로우를 명확히 정의합니다. "망막사진의 품질이 부적절한 경우, 그리고 이상 소견이 검출된 경우 후속 조치를 위해서는 in-person 검사가 여전히 필요하다. 망막사진은 dilated comprehensive eye exam을 대체할 수 없으며, 후자는 최소 초기에 그리고 그 후 매년 또는 안과 전문의 권고에 따라 더 자주 시행되어야 한다"고 명시합니다. [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690177/)

즉 AI의 역할은:

- 양성(actionable disease 검출) → 안과 의뢰
- 음성 → AAO 연간 검사 가이드라인에 따라 12개월 후 재검사 권고 [Digital Diagnostics](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/)
- 영상 품질 불충분 → 대면 검사

이라는 3-way triage 게이트키퍼입니다.

### 역할 4 - Point-of-care 자율 진단

LumineticsCore 제품 자체의 작동 방식이 가이드라인이 AI에 부여한 역할의 본질을 보여줍니다. "안저카메라를 사용해 시술자가 환자 눈의 고품질 영상을 촬영합니다. 영상은 LumineticsCore에 제출되어 당뇨망막병증 징후가 분석됩니다. 환자와의 만남 동안 진단 결과가 제공되며, 진단에 기반한 후속 지침이 환자에게 전달됩니다. Actionable disease가 검출되면 환자는 안과 전문의에게 의뢰되며, 이는 환자가 의뢰 약속을 이행할 가능성을 높이는 것으로 나타났습니다. Actionable disease가 검출되지 않으면 환자는 AAO 연간 검사 가이드라인에 따라 12개월 후 재검사를 받도록 안내됩니다." [Digital Diagnostics](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/)

핵심은 "LumineticsCore는 22세 이상의 당뇨병 진단을 받은 성인 중, 이전에 당뇨망막병증 진단을 받지 않았고 현재 안과 전문의의 진료를 받고 있지 않은 환자를 대상으로 합니다"는 점입니다. **안과 의료 시스템 외부**에 있는 환자를 안과 진료 경로로 끌어들이는 게이트웨이 역할입니다. [Digital Diagnostics](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/)

### 역할 5 - 불필요한 전문의 의뢰 회피

"중추적 임상시험에서 LumineticsCore는 91%의 불필요한 전문의 진료를 줄였다 - 환자를 음성으로 표시함으로써 point-of-care에서 진단 결과를 제공한 결과"입니다. [Digital Diagnostics](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/)

이는 가이드라인이 AI에 부여한 또 하나의 역할입니다: 안과 전문의 자원을 더 복잡한 사례와 치료에 집중시키는 효율화 도구.

## 가이드라인이 요구하는 AI 성능 - 정량적 근거

가이드라인이 LumineticsCore를 인정하는 근거는 pivotal trial 데이터입니다.

"임상시험에서 이 시스템들은 높은 민감도와 특이도를 보여주었다. 예를 들어 LumineticsCore(구 IDx-DR)의 FDA 승인을 이끈 900명의 완전 스크리닝된 환자 연구는 mild DR 이상에 대해 87% 민감도, 90% 특이도를 보였다." [American Academy of Ophthalmology](https://www.aao.org/eyenet/article/artificial-intelligence-for-diabetic-retinopathy)

이는 ADA가 "FDA-authorized" AI 시스템에 부여하는 신뢰의 정량적 기반입니다.

---

## 가이드라인이 부여하지 *않은* 역할 - 명확한 한계선

ADA 텍스트는 AI가 대체할 수 없는 영역도 함께 정의합니다.

Dilated comprehensive eye exam을 대체할 수 없음. "망막사진은 dilated comprehensive eye exam을 대체할 수 없다" - AI는 스크리닝 도구이지 진단 확진 도구가 아닙니다. [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC12690177/)

영상 품질 불충분 시 대면 검사 필수. AI의 한계를 인정하고 fallback 경로를 의무화합니다.

이상 소견 검출 시 후속 조치 필수. AI가 양성 결과를 내면 인간 안과의의 in-person evaluation이 의무입니다.

---

## 종합 - AI 역할의 5단 구조

가이드라인 안에서 LumineticsCore형 AI의 역할을 한 문장으로 압축하면:

"FDA 승인된 자율 AI 시스템은, 안과 진료를 받고 있지 않은 당뇨병 환자를 대상으로 point-of-care에서 mild DR 이상/DME를 검출해, 안과 의뢰가 필요한 환자와 12개월 후 재스크리닝하면 되는 환자를 triage하는 대안적 스크리닝 도구"

# ESTI 2025: Lung Cancer Screening

## 문서의 목표

문서의 목표는 "ESTI 결절 관리 권고의 임상적 의의는 후속 검사 횟수를 줄이면서도 주요 stage shift와 과치료를 예방하는 데 있다"는 것입니다. 즉 AI를 도입하는 이유 자체가 - 불필요한 follow-up 감소 + stage shift 위험 최소화 + 과진단/과치료 방지라는 세 가지 균형점을 맞추기 위함입니다. [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

또한 ESTI 위원회 보드가 2024년 6월에 이 문서를 공식 endorsement 했고, 2025년 4월 9일 최종 수락되어 출판되었습니다. [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

## ESTI가 제시한 결절 위험 분류의 3가지 접근법

ESTI 문서는 결절 위험 분류 방식을 다음 세 가지로 명확히 구분하며, 여기에 AI가 직접 등장합니다.

1. 형태학적 분류 (Morphological classification). 결절의 상세한 형태에 따라 일련의 특정 형태학적 특징 조합으로 분류. 가장 상세한 예가 LungRADS v2022로, 다양한 밀도의 결절, 폐 낭종, 기도 결절을 포함하는 고정된 정의에 의존. 약 6개의 주요 카테고리(category 1에서 category 4X) 중 가장 "대표적인 카테고리"를 찾아내야 함. [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
2. Model-based classification. 다변량 로지스틱 회귀 모델 등 수학적 모델로 결절 위험을 분류. ILST(International Lung Screen Trial)와 British TLHC가 Brock model을 통합해 인구학적, 임상적, 영상학적 특징을 위험 계산에 사용. [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
3. Deep learning-based classification. "심층 학습 기반 분류 모델에 의한 결절 위험의 분류. 이러한 모델은 일반적으로 결절 주변의 영상 또는 부분 영상과 선택적으로 몇 가지 임상 매개변수를 입력받아, 일반적으로 deep convolutional neural networks를 사용해 영상을 처리하여 자동으로 확률을 계산. 아직 어떤 가이드라인이나 관리 프로토콜도 이러한 deep learning 기반 모델을 통합하지 않았지만, 여러 학술적·상업적 솔루션이 존재하며 문헌에 기술되었고, 전향적으로 테스트되고 있음". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

이 분류가 중요한 이유는, ESTI가 AI를 별도의 부록이 아닌 위험 분류의 한 축으로 명시했다는 점입니다.

## AI의 핵심 역할 - Volumetry

ESTI 권고안 전체에서 AI가 가장 직접적으로 임상 결정에 개입하는 영역입니다.

### Volumetry가 manual measurement보다 우선

"출판된 근거에 기반해, 컴퓨터 보조 부피 평가가 수동 2차원 측정보다 명확히 선호된다. 기하학적 이유로 부피가 두 배가 되어도(100% 부피 증가) 직경은 26%만 증가. 직경의 수동 측정은 상당한 intra-observer(±1.4 mm, 95% 일치 한계) 및 inter-observer(±1.7 mm, 95% 일치 한계) 변동성에 노출됨". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

이 점이 결정적입니다. ESTI 가이드라인 표 1의 모든 follow-up 결정 기준이 volumetry를 1차로 가정하고, manual measurement는 "if volumetry fails"의 fallback으로만 위치합니다.

### Volumetry로부터 도출되는 Volume Doubling Time (VDT)가 핵심 의사결정 변수

"부피 측정(VDT 평가)이 성장률의 척도로 사용될 수 있다. 성장은 짧은 VDT, 긴 follow-up 간격, 더 정확한 volumetry에서 더 정확하게 추정 가능"합니다. [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

ESTI 결정 트리에서 VDT 임계값:

- Positive (workup): VDT < 250 days at 3 months, VDT < 400 days at 6 months, VDT < 500 days at 12 months [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
- Indeterminate: VDT ≥ 250 d at 3 months [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
- Negative: VDT ≥ 400 d at 6 months OR VDT ≥ 500 d at 12 months [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

이 VDT는 volumetry software 없이는 계산이 불가능합니다. 따라서 ESTI 가이드라인은 사실상 AI/CAD volumetry를 의사결정의 전제 조건으로 만들었습니다.

### 신규 결절의 경우 - 부피 절대값이 의사결정

Positive: New nodule follow-up - Solid (component) > 15% volume growth at 3 months, > 1.5 mm diameter growth at 3 months. [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

15% volume growth는 manual로 측정 불가능합니다. 이 기준 자체가 volumetric AI를 가정합니다.

## AI Volumetry의 알려진 한계 - ESTI가 명시한 주의사항

ESTI는 AI를 무비판적으로 채택하지 않습니다. 구체적 한계를 다음과 같이 명시합니다.

- 한계 1: 비고형 성분 분할 취약. "대부분의 시스템은 density thresholding과 shape recognition의 조합을 사용. Volumetry 소프트웨어는 주변 정상 폐와 감쇠 차이가 작은 비고형 성분 분할에 덜 효율적. 또한 낭성 결절 또는 part-solid 결절은 고형 성분만 분할하더라도 문제를 야기". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
- 한계 2: 흉막/혈관 인접 결절에서 과대평가. "흉막이나 폐혈관에 인접한 고형 결절의 분할은 인접 구조물 포함으로 인해 결절 크기를 과대평가할 수 있음". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
- 한계 3: 획득/재구성 파라미터 민감성. "Follow-up 동안 acquisition과 reconstruction 파라미터는 가능한 한 일정하게 유지되어야 함. Density thresholding이 요구되는 경우, hard kernel보다 soft kernel에서 volume 분석을 수행하는 것이 바람직. Hard kernel의 높은 노이즈 수준이 volumetry 변동성을 증가시키므로, soft kernel이 고형 및 subsolid 결절 모두에 대해 더 정확하고 재현 가능한 부피 측정을 위해 선호됨". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)
- 한계 4: 벤더 간 비호환성. "서로 다른 vendor의 소프트웨어는 서로 다른 결과를 제공. 일부는 분할 오류를 수동으로 수정할 수 있게 하지만 다른 일부는 그렇지 않음. 동일한 소프트웨어가 lung cancer screening 프로그램 전체에서, 또는 최소한 개별 참가자의 follow-up의 일부로 사용되어야 함. 새 소프트웨어가 설치되면, 관리에 영향을 미칠 수 있는 경우 이전 측정을 반복해야 함". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933) 이 한계는 매우 실무적으로 중요합니다. ESTI는 사실상 "AI vendor 변경 시 baseline 재측정 의무"를 권고하고 있습니다.
- 한계 5: 분할 정확도에 따른 측정 신뢰구간. "두 부피 측정 간 차이의 95% 신뢰구간은 완전히 분할된 결절의 경우 약 ±12%였지만, 불완전하게 분할된 결절의 경우 약 ±30%로 증가". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

## ESTI가 제시한 AI의 미래 전망 (Future perspectives 섹션)

이 부분이 ESTI가 AI의 향후 역할을 어떻게 보는지 정확히 보여줍니다.

### AI 검출 도구의 현재 위치

"폐 결절 검출 및 부피 평가를 위한 컴퓨터 보조 검출 도구 및 AI 기반 알고리즘은 유망한 성능을 보여줬지만, 후향적 연구에 기반함. 현재 유럽에서 15개 이상의 CE 인증 알고리즘이 임상 사용 가능. 그러나 대부분의 유럽 국가에서 체계적인 보험수가가 없음". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

이는 두 가지 함의를 가집니다: 첫째, regulatory clearance(CE)는 이미 다수 확보되어 있다. 둘째, reimbursement는 여전히 미해결이다.

### Deep learning 모델이 Brock model을 능가

"최근 연구는 이미지 데이터만 사용하는 deep learning 기반 모델이 악성도 위험 추정에서 Brock와 같은 다변량 위험 모델을 능가할 수 있음을 보여줬다. 결과적으로, 전향적으로 검증된 경우, 이러한 모델은 향후 결절 관리를 안내하여 악성 결절을 더 빨리 인식하고 양성 결절에 대한 follow-up CT 스캔을 줄이는 데 사용될 수 있다". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

여기서 ESTI는 명확한 입장을 취합니다: DL 기반 위험 예측 모델이 Brock 같은 기존 통계 모델을 능가한다는 근거가 충분하며, 전향적 검증을 거치면 결절 관리를 직접 안내하게 될 것이라는 전망입니다.

### Radiomics/DL의 invasive vs preinvasive adenocarcinoma 구별

"Radiomics와 deep learning 접근법은 subsolid 결절로 나타나는 선암종의 pre-invasive와 invasive 형태를 구별하기 위해 개발됨. 그러나 그 성능은 고형 성분 크기에 대한 방사선과 의사의 측정보다 아직 우수하지 않음". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

여기서는 ESTI가 현재 시점에서는 AI가 인간 방사선과 의사의 형태학적 판단을 아직 능가하지 못한다는 점도 솔직히 명시했습니다.

### Big 3 동시 평가

"흡연은 폐암의 주요 위험 인자일 뿐만 아니라 COPD와 심혈관 질환의 주요 위험 인자. 이 셋("BIG 3")이 스크리닝 참가자의 사망의 대부분을 차지하며, non-contrast, ungated chest CT로 검출 및 정량 평가 가능. 이는 스크리닝 참가자의 전체 사망률을 추가로 감소시키는 길을 열 수 있지만, 정량화 및 추가 관리를 위한 적절한 가이드라인은 정의되어야 함". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

LDCT 한 번으로 폐암 + COPD(폐기종) + 심혈관(관상동맥 석회화) 동시 정량 평가 - 이는 AI 정량화 도구의 자연스러운 확장 영역입니다.

## 결론에서의 AI 위치 - ESTI의 공식 입장

ESTI 결론을 그대로 보면:

"진행 중인 implementation trial은 이 접근법을 더 검증하고 정제하며, lung cancer screening에서 인공지능의 영향을 전향적으로 평가할 기회를 제공할 것이다". [longkankernederland](https://www.longkankernederland.nl/media/1/Downloads/Nodule-management-recommendation-European-Society-of-Thoracic-Imaging-2025.pdf?v=1759326933)

즉, AI는 현재 ESTI 권고에 부분적으로 통합되어 있지만(volumetry, VDT 계산), 향후 prospective trial을 통해 더 깊이 통합될 예정이라는 입장입니다.

# NCCN 2026: Breast Cancer Screening

2026년 4월 NCCN Breast cancer screening 가이드라인에 AI가 도입되었습니다.

## 주요 AI 관련 신설 사항: 영상 기반 위험 평가 모델 (BSCR-4, MS-15~16)

이번 버전에서 가장 중요한 AI 관련 변화는 "5-year risk of invasive breast cancer ≥1.7% as calculated by an imaging-based risk assessment model" 항목이 Increased Risk 카테고리에 새롭게 등재된 것입니다.

BSCR-4 페이지를 보면, 이 새로운 위험군에 대한 권고는 기존 Gail Model 기반 ≥1.7% 위험군과 동일한 screening/follow-up pathway를 따릅니다:

- Clinical encounter every 6–12 mo
- Annual screening mammogram with tomosynthesis
- Consider annual breast MRI with and without contrast (CEM/MBI/whole breast US 대안)
- Consider risk reduction strategies
- Breast awareness

## AI 기반 위험 평가 모델의 근거 (MS-15~16, Discussion)

Discussion 섹션에서 AI 모델의 효용성에 대한 구체적 근거가 제시됩니다:

> "Artificial intelligence (AI)-based risk assessment models are emerging as another effective tool in assessing risk of invasive breast cancer. These deep-learning algorithms utilize features of negative screening mammograms to generate risk assessment scores."
> 

성능 비교 데이터 (systemic review, ref. 143):

- AI image-only 모델: median AUC 0.72 (range 0.62–0.90)
- 기존 모델 (breast density, Gail, Tyrer-Cuzick): median AUC 0.61 (range 0.54–0.69)
- AI image + clinical risk factor 결합 모델: median AUC 0.73 (range 0.66–0.84)

즉, AI 기반 모델이 기존의 통계적 risk model보다 명확히 우수한 변별력을 보였다는 점이 등재의 핵심 근거입니다.

## 임상 워크플로우상 AI 모델의 적용 방식

가이드라인은 AI 모델의 적용 방식을 다음과 같이 구체화합니다:

- 적용 시점: ≥35세에서 5년 invasive breast cancer 위험도 ≥1.7%로 계산되는 경우 (Gail Model과 동등한 컷오프 사용)
- 재평가 권고: footnote m에서 "Periodic reassessment of risk is recommended, particularly when risk factors change"로, AI risk score 역시 정기적 재평가 대상으로 명시
- 위험 모델 선택: 가이드라인은 Gail, Tyrer-Cuzick, BRCAPRO, BOADICEA/CanRisk, BCSC Invasive Breast Cancer Risk Calculator와 함께 AI 기반 모델을 동등한 위험 평가 옵션으로 인정

## 하지만…

가이드라인의 다른 영역에서는 AI에 대한 언급이 의외로 제한적입니다:

- CAD (Computer-Aided Detection): 별도 권고 없음
- AI 기반 mammogram triage/판독 보조: 임상 알고리즘에 미반영
- MRI/CEM/MBI AI 분석: 언급 없음
- Tomosynthesis AI: 등재 없음

오직 위험 평가(risk assessment) 영역에서만 AI가 공식적으로 등재된 점이 특징적입니다.

## 임상적 의미

NCCN Breast Cancer Screening v1.2026에서 AI는 screening recall이나 lesion detection 보조도구로서가 아니라, "screening mammogram을 이용한 future cancer risk prediction"이라는 별도의 임상적 진입점으로 등재되었습니다. 이는 의료 AI의 가이드라인 진입 경로 측면에서 매우 의미 있는 변화로, 다음 두 가지를 시사합니다:

1. Negative mammogram의 가치 재정의: 종래 BI-RADS 1–2로 종결되었던 정상 mammogram이 AI를 통해 추가적 위험 정보를 생성하는 자원으로 전환됨
2. 위험 모델 다원화의 공식 인정: family history 기반 통계 모델만이 아닌, imaging texture/feature 기반 deep learning이 동등한 위험 평가 도구로 가이드라인화

# Outro

각 가이드라인을 따라가다 보면 공통된 패턴이 보입니다. 첫째, 좁고 명확하게 정의된 단일 clinical unmet needs가 가이드라인 진입의 전제 조건입니다. 둘째, FDA, CE, DTAC 같은 규제 라벨이 가이드라인 인용의 트리거로 기능합니다. 셋째, prospective multicenter validation의 출판이 가이드라인 텍스트에 명시적 근거로 인용됩니다. 그러나 동시에 각 가이드라인이 AI에 부여하는 권한의 폭은 매우 다르고, 어떤 경우에는 AI가 의사결정의 전제가 되는 반면 다른 경우에는 보조적 역할에 머무릅니다. 이 차이가 어디서 오는지, 그리고 향후 의료 AI가 가이드라인에 진입하려면 어떤 경로를 밟아야 하는지를 이 다섯 사례가 함께 보여줍니다.