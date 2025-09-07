---
title: "Medical AI는 돈이 될까요? - 2023년까지의 보험 청구 건수를 바탕으로"
tags:
  - medical AI
  - reimbursement
  - insurance
  - CPT code
use_math: true
---


# Introduction

(NEJM AI)[ai.nejm.org] 1호에 출간된 논문으로, 2024년 1월에 출간된 논문입니다. 좀 철이 지나기는 했지만, 많은 분들이 리뷰를 해 주셨음에도 불구하고 아직 모르는 분들이 종종 보이는 것 같아 저도 한 번 리뷰를 해 봅니다.

2023년 현재, 미국 FDA 인허가를 받은 medical AI 제품들은 500개가 넘습니다. 하지만 인허가 이후에 회사들은 언제 어디에 자신들의 제품이 쓰이는지 거의 공유하지 않기 때문에 본 글에서는 medical AI 제품의 real-world usage에 대해 고찰합니다.

AI 제품들이 의료에서 쓰이게 될 때 사용처와 적용 패턴이 임상적 영향력을 엄청나게 결정합니다. 먼저, AI 알고리즘의 성능은 알려진 바와 같이 domain adaptation 문제가 심각합니다. 예를 들어 20% 넘게 detection rate를 향상시켜주는 mammography CAD 제품들은 2000년대 초반에 많이 개발되었는데 실제로 여성에게 효과가 없음이 증명되었습니다. 즉 AI 제품은 특정 조건과 상황 하에서는 성능이 우수하겠지만, 현실 세계에서의 적용은 아주 다른 outcome을 야기할 수 있습니다. 둘째로, medical AI device의 영향력은 경제적인 요인에 의존합니다. FDA 인허가 승인 이후에, 회사들은 이러한 AI-driven health care system이 현실화되도록 판매 전략을 짜야 합니다. 서로 다른 보상 전략이 이 장비들을 사서 쓸 사람을 정의할 것이고, 어떠한 전략이 새로운 device에 대해 최선인지는 불명확합니다. 따라서 경험적으로 medical AI device들이 어떻게 쓰이는지를 이해하는 것이 의료에 있어서의 혁신을 이끄는데 도움이 되며 알고리즘부터 환자까지 이어지는 pipeline에 대한 전반적 이해를 돕습니다.

미국의 보험 수가 체계인 CPT 코드는 최근 medical AI 장비들에 적용되고 만들어지기 시작했습니다. 미국 보험청인 CMS는 CPT 코드 뿐 아니라 new technology add-on payment (NTAP)과 같은 제도를 만들어서 새로운 기술을 도입하는 것을 장려하기도 하였는데 NTAP과 같은 경우에는 입원 환자들만을 대상으로 하고 CPT 코드는 입원, 외래 환자 모두에게 적용이 가능합니다. 본 글에서는 더 일반적으로 사용이 가능한 CPT 코드만을 다루기로 합니다.

CPT 코드가 medical AI 장비들에 더 적용되고 있긴 하지만 이 코드들은 하나의 database에서 관리되지 않고 이들의 사용처에 대한 체계적인 분석이 이루어지지도 않았습니다. 따라서 본 글에서는 청구 건수와 관련하여 이러한 사용처를 분석해 봅니다.

# Methods

## Collecting CPT Codes for Medical AI Devices

### Official AMA Sources

미국의사협회(American Medical Association; AMA)는 CPT 코드를 만들고 관리합니다. 저자들은 인공지능 CPT 코드를 탐색하기 위해 AMA의 category III 코드를 리뷰했습니다. 이는 임시 코드로 새로운 기술, 서비스, 시술에 대한 코드이다. 임시 코드이므로 5년간 사용 허가를 받고, 5년 뒤에 다시 평가하여 정식 코드인 I로 넘어가거나 그렇지 않거나가 결정됩니다. 저자들은 category III의 artificial intelligence와 machine learning, 그리고 이들의 변이형 코드를 탐색했습니다.

또한 category I, II에 대해서는 수작업으로 관련 코드를 찾았다고 합니다.

### Determining AI Devices

다음 조건이 만족되어야 medical AI device로 포함시키고 조사를 하였습니다: 제조사가 인공지능, 머신러닝을 사용하였다고 명시적으로 마케팅을 하거나, 3rd party(보험사나 신문 기사)에 의해서 인공지능이나 머신러닝을 사용하였다고 홍보되는 경우. 더불어 non-AI device에 부여되는 CPT 코드는 제외하였습니다. 이것이 의미하는 바는 예를 들어 continuous glucose monitoring 기기와 같은 것에 AI 기능이 탑재되는 경우 기존의 CPT 코드를 받기 때문에 이런 경우는 제외하였습니다. 다른 예시로는 CAD mammography가 있는데 이는 고전 영상처리를 사용한 경우가 대부분이기 때문에 현대적 의미의 AI CAD와는 다르다고 판단하였습니다. 

### Grouping CPT codes

다양한 CPT code들이 같은 제품 및 시술에 연관될 수 있습니다. 예를 들어 0648T와 0649T는 조직 구성을 분석하기 위한 정량적 MRI 분석 코드인데 0648T는 MRI 진단이 완료되지 않은 경우 부여되고 0649T는 완료된 시점에 부여되는 등과 같은 식입니다. 이러한 방식으로 함께 그룹핑된 코드들의 청구 건수를 분석하였습니다.

# Results

![스크린샷 2023-11-19 오후 1.47.41.png](/img/reimbursement/1.png)

위 표는 2023.6.1. 기준의 청구 건수입니다.

위 표가 논문에 나와 있는 표이고, 이를 좀 더 자세히 분석하면 다음과 같습니다. (논문엔 나와있지 않은 내용)

## 일 평균 청구 건수

괄호 안의 금액은 청구 금액을 제가 직접 조사한 후 달러로 환산하였을 때 **일 평균 청구되는 비용**입니다. 청구 금액이 조사 결과 미상인 경우 기입하지 않았고, 정확한 금액이 아니라 범위로 주어진 경우는 범위로 표시하였습니다.

- HeartFlow : 총 67,306건 → 36.88건/일 (검사당 1450.5 달러 → 일 평균 53,494.44 달러; [reference](https://www.heartflow.com/newsroom/heartflow-announces-decision-by-centers-for-medicare-medicaid-services-to-assign-a-new-technology-payment-classification-to-heartflow-ffrct-analysis/))
- LumineticsCore : 총 15,097건 → 16.54건/일 (검사당 45.36 달러 → 일 평균 750.25 달러; [reference](https://www.reviewofophthalmology.com/article/medicare-whats-new-for-2022))
    
    ![IMG_1225.jpeg](/img/reimbursement/1.1.jpeg)
    
- Cleearly : 총 4,459건 → 4.88건/일 (검사당 약 900-1000 달러 → 일 평균 4,392-4,880 달러)
    
    ![IMG_1226.jpeg](/img/reimbursement/2.jpeg)
    
- Perspectum LiverMultiScan : 총 2,428건 → 2.66건/일
- Perspectum CoverScan : 총 591건 → 1.08건/일
- Koios DS : 총 552건 → 1.01건/일
- Anumana : 총 435건 → 2.38건/일
- CADScor : 총 331건 → 0.6건/일
- Perspectum MRCP+ : 총 237건 → 0.43건/일
- CompuFlo : 총 67건 → 0.36건/일
- Optellum : 총 4건 → 0.01건/일 (검사당 약 $600-$700 → 일 평균 $6-7, [reference](https://optellum.com/2022/06/press-release-cms-assigns-new-technology-payment-classification-for-optellums-lung-cancer-prediction-score/))
- 1건 이하인 것들은 계산하지 않았습니다.

## 지역에 따른 차이

![스크린샷 2023-11-19 오후 2.31.32.png](/img/reimbursement/3.png)

## AI 제품이 CPT 코드를 받는 시간에 따른 증가율

![스크린샷 2023-11-19 오후 2.31.47.png](/img/reimbursement/4.png)

## AI제품을 더 쓰는 요인들

![스크린샷 2023-11-19 오후 2.32.03.png](/img/reimbursement/5.png)

# Discussion

## 논문 자체의 결과

HeartFlow가 가장 많은 일 평균 수입을 올렸고(약 53,494.44 달러), 이후가 Cleerly(약 4,392-4,880 달러), 그 다음이 Digital Diagnostics 사의 LumineticsCore (약 750.25 달러) 순이었습니다. CPT코드를 받는다고 전부 다 수익이 발생하는 것은 아니었습니다(Optellum 이후의 제품들은 6개월~1.5년동안 청구 건수가 0건에 달했습니다).

## 개인적 고찰

물론 시장성이 있는 제품을 디자인하면 좋겠으나 현실적으로 미래의 수요를 예측할 수는 없으므로 만들어진 제품을 적절히 시장과 임상 현장에 녹여내는 것이 중요한 지점이 됩니다.

HeartFlow는 AHA (미국심장협회; American Heart Association) 의 가이드라인을 바꿀 정도로 많은 노력과 임상시험을 진행하였습니다. 
