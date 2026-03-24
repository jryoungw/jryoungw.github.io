---
title: "폐암의 역사와 폐암 인공지능에 관하여 - 2"
tags:
  - medicine
tags:
  - AI
  - Artificial Intelligence
  - Medical Artificial Intelligence
  - Medical AI
  - Medicine
  - Computer-Aided Diagnosis
  - CAD
  - Lung Cancer
  - Pulmonary Nodule
---

# 들어가며

- [이전 글 읽기](https://jryoungw.github.io/posts/Lung_Cancer_History/)

의학에서 자연사라고 하는 것은 주로 어떠한 의학적 개입도 없이 어떤 질환을 가만히 놔두면 어떻게 그 질환이 진행되는지에 대한 내용을 다루는 것입니다. 죽는다 할 때의 자연사가 아니라 역사 할때의 사임에 주의하세요.

# 폐암의 자연사 (Natural Course of Lung Cancer)와 폐암 검진의 효용성 (Efficacy of Lung Cancer Screening)

## 폐암의 자연사 - 미국

[이전 글](https://jryoungw.github.io/posts/Lung_Cancer_History/)에서는 폐암 검진을 흉부 X선 사진으로 하려는 시도가 모두 실패했다고 말했고, NLST 연구와 NELSON 연구를 통해 흉부 CT 기반 폐암 검진이 조기 진단을 통해 사망률을 낮출 수 있다는 것을 확인했습니다. 그렇다면 다시 돌아가서, 폐암 검진 없이 임상적으로 진단되는 경우에는 어느 병기에 진단될까요?

[SEER 웹페이지의 Cancer Stat Fact](https://seer.cancer.gov/statfacts/html/lungb.html)를 통해 2015-2021년 사이 동안의 수치를 확인할 수 있는데요, 

![image.png](/img/natural_course_overdiagnosis/image.png)

검진(스크리닝과 같은 의미로 사용하기로 합니다.) 없이 폐암을 진단하게 되면 국소적으로 발견되는 경우가 23%, 근처 임파선(lymph node)까지 전이된 경우가 21%, 전이성으로 발견되는 경우가 52%로, 절반 이상이 폐암이 전이된다고 합니다. 불행히도, 각 상황에 따른 5년 생존률은

![image.png](/img/natural_course_overdiagnosis/image 1.png)

정도라고 합니다. 더 전이가 될수록 더 사망하는 구조인 것은 당연하지만, 전이가 된 경우에는 5년 생존률이 10% 남짓으로 좋지 않은 것을 확인할 수 있습니다.

## 폐암의 자연사 - 한국

한국의 경우에는 국립암센터 김혜영 선생님의 [폐암의 병기 결정 칼럼](https://synapse.koreamed.org/upload/synapsedata/pdfdata/0119jkma/jkma-51-1118.pdf)을 통해 수치를 확인할 수 있는데요:

![lunca_kor.png](/img/natural_course_overdiagnosis/lunca_kor.png)

로, 그래프로 도식화해보면 다음과 같습니다.

![lungca_kor_graph.png](/img/natural_course_overdiagnosis/lungca_kor_graph.png)

본 자료는 2008년 자료이기에 현재는 좀 더 나아졌긴 하지만, 최소한 폐암을 늦게 진다는하는 것이 비극적이라는 것은 충분히 전달이 되었을 것이라 생각합니다. 

## 폐암의 검출 시기

CT라는 것도 영상이기 때문에 해상도라는 것이 있을 것이고 당연히 암세포 하나하나를 검출하지는 못할 것입니다. 그렇다면 영상에서 보이기까지는 얼마나 시간이 걸릴지도 궁금해집니다. 간단하게 도식화하고 용어 정리를 하면 폐암의 자연사는 다음과 같이 진행됩니다.

![lungca_phases.png](/img/natural_course_overdiagnosis/lungca_phases.png)

[Ten Haaf et al, 2015 연구](https://aacrjournals.org/cebp/article/24/1/154/163827/Lung-Cancer-Detectability-by-Test-Histology-Stage?guestAccessKey=)의 모델링 결과에 따르면 평균적으로 암 발생부터 검출까지 걸리는 시간(mean sojourn time; MST)는 약 3.1년에서 6.0년 정도가 걸리고, 이는 병리학적인 특성과 성별을 포함한 다양한 요인에 영향을 받지만 IA 병기(폐암 초기)로 검출되기까지는 평균적으로 약 1.3년에서 2.4년 정도가 걸린다고 합니다.

(참고로, 폐암 검진은 1, 2년마다(상황따라 조금씩 다릅니다.) 수행하라는 것이 권고인데 폐암 발생부터 IA 병기 검출까지 평균적으로 1.3년에서 2.4년이 걸린다는 것은 1년 혹은 2년 단위의 페암 검진에 당위성을 부여하기도 합니다.)

이러한 결론은 Volume Doubling Time (VDT; 부피 배가 시간)이라고 해서 부피가 두 배 걸리는데 걸리는 시간을 모델링을 통해 추론하여 얻어진 결과입니다.

제가 [이전 글](https://jryoungw.github.io/posts/omakase_24_06_week10/)에서도 다루었지만 VDT의 수식은 다음처럼 주어집니다:

![image.png](/img/natural_course_overdiagnosis/image 2.png)

여기까지 보면 폐암은 매우 무시무시한 것을 확인할 수 있습니다. 그래서 2010년대부터 폐암 검진을 시작한 것이고요. 그런데, 우리, 정말 폐암 검진 잘 하고 있는 것일까요? 혹시나 암이 아닌, 멀쩡한 사람을 암으로 오진하지는 않고 있을까요?

# 과진단 (Overdiagnosis)

## NLST와 NELSON의 과진단

얻는 게 있으면 잃는 것도 있는  법. 폐암 검진에도 과진단에 대한 논란이 존재합니다. 과진단을 쉽게 말하면 어떤 환자가 살이 있는 동안에 병이 검진과 치료 없이도 문제를 안일으키지 않았을까? 라는 질문에 대한 대답을 해 나가는 과정입니다.

[체계적 문헌 고찰을 통해 8개의 연구에서 6998건의 부검을 통해 확인한 결과](https://link.springer.com/article/10.1186/s12885-023-11224-3)로는, 폐암과 폐암 관련 사망이 아니었던 사람들 중에서 0.87%는 폐암이 있었다고 합니다. 즉, **전 인구의 약 0.9%는 폐암이 있지만 폐암으로 죽지는 않는다는 것이지요.** 이것이 문제가 됩니다. 운명이 어떻게 흘러갈지는 모르지만 폐암 검진으로 폐암 관련 치료를 한 사람들이 사실은 폐암이 아닌 다른 이유로 죽을 사람들이었다면? 당뇨, 고혈압, 심장질환 등으로 죽을 운명이었다면? 같은 어렵고 철학적인 질문에 대해 대답하는 연구가 폐암의 과진단에 관한 연구들입니다. 

특히나 사람마다 면역, 생활습관, 유전자가 다 다르기 때문에 폐암이 있다 하더라도 폐암의 성장 속도가 획일적으로 동일하지는 않습니다. 어떤 사람의 폐암은 순식간에 커지고, 어떤 사람은 10년 동안 서서히 폐암이 자라기도 하고 그런 것이지요. 의학에서는 이렇게 천천히 자라는 폐암을 indolent cancer, indolent nodule이라고 부릅니다. 첫 검사에서 폐암으로 의심되는 병변이 발견되었는데 혹시 이 병변이 indolent한 것은 아닐까? 라는 질문을 던지는 것이지요.

전 세계의 폐암 검진 프로토콜들은 최대한 이러한 문제를 피해가려고 노력했습니다. 암은 고령에 많이 생기니까 고령을 대상으로 했고, 흡연으로 인해 생기니까 heavy-smoker이라고 불리는 흡연하는 고위험군을 대상으로 수행하는 것 등이지요.

결론적으로, 과진단에 대한 대답은 양성 종양(폐에 덩어리가 있지만 암은 아님)과 폐암을 잘 구분하고, 더 신경써서 관리하는 것에 있습니다. 따라서 추적 관찰을 하면서 얼마나 빨리 자라는지와 같은 VDT 수치들이 중요해지는 것이지요.

폐암에 관한 임상 시험들은 그렇다면 얼마나 과진단을 했을까요? [한 연구](https://pmc.ncbi.nlm.nih.gov/articles/PMC8021885/)에 따르면 마지막 screening 이후로 과진단이 생길 확률은 연차에 따라서 다음과 같다고 합니다:

![lungca_estim.png](/img/natural_course_overdiagnosis/lungca_estim.png)

NLST와 NELSON 모두 마지막 스크리닝 이후로부터 4.5년에는 약 20% 정도의 과진단이 생기지만, 이후에 5.5년에서 9년이 흐르고 나면 과진단의 비율이 감소하고 실제로 암이 발생하는 케이스가 는다고 합니다.

## Volume Doubling Time (VDT)

위에서 언급한 VDT와 같은 경우에는 CT 기반 연구는 잘 없고, CXR 기반 연구가 메인이었습니다. 폐암 검진의 창조자 중 한 분인 David Yankelevitz 선생님과 Claudia Henschke 선생님들의 [연구](https://acsjournals.onlinelibrary.wiley.com/doi/10.1002/cncr.11185)에 따르면 Mayo Lung Project (MLP)와 Memorial Sloan Kettering Cancer Center (MSK)에서, Stage I cancer들은 MLP는 101일의 VDT를 가졌고 MSK는 144일의 VDT를 가졌습니다. 이는 screening이 아닌 곳에서 검출된 adenocarcinoma의 VDT에 비해 작은 수치입니다.

## CT 기반 폐암 검진은 정말 과진단을 유발할까?

[2023년에 나온 I-ELCAP의 연구](https://pubs.rsna.org/doi/full/10.1148/radiol.231988)에서는 다음과 같은 그래프를 확인할 수 있는데요,

![image.png](/img/natural_course_overdiagnosis/image 3.png)

무려 20년을 추적관찰한 결과입니다. Staging이 T1aN0M0, 쉽게 말해서 초기 암의 경우에는 수술로 치료를 하고 나면 10년 후에 Kaplan-Meier 곡선이 생존률 95%로, 평탄해집니다. 그래프에서 확인할 수 있듯, 대조군에 비해서 높은 생존률을 보이기도 하지요. 이는 과진단이나, 과진료를 하지 않았다는 것을 시사하기도 합니다. 오히려, 잘 치료했다는 것을 시사하는 점이기도 하지요.

## 한국의 데이터

한국은 폐암 검진을 거의 세계 최초로 시작하며 폐암 검진의 선진 사례를 보여주고 있습니다. 제가 제일 흥미로워 하는 부분이 한국의 검진들을 비교하는 부분인데요, 한국은 국립암센터에서 검진들의 다양한 데이터를 보여주고 있습니다. 폐암의 연간 추이를 봅시다. [국립암센터에서 출간한 연구](https://pmc.ncbi.nlm.nih.gov/articles/PMC9016309/)의 그래프를 보면,

![lungca_incidence.jpg](/img/natural_course_overdiagnosis/lungca_incidence.jpg)

이런 그래프가 있습니다. 여기서 눈여겨 볼 것은 위쪽 그래프의 Lung이라고 적힌 보라색 사각형 선과, 아래쪽 그래프의 Thyroid(갑상선, 파란색 동그라미)입니다. 갑상선 암은 2000년부터 폭발적으로 증가했는데 비해서 폐암은 10만명당 50건 정도로 유지되고 있습니다. 초음파와 조직검사가 퍼지면서 갑상선 암이 폭발적으로 증가했다가, [2012-2014년경 갑상선 암 과잉 진단 논란](https://www.thyroid.kr/file/faq/faq01.pdf)이 퍼지자 오히려 검진을 덜 해서 갑상선 암을 덜 잡았다는 것을 상기합시다. 대조적으로 한국의 페암검진 시범사업(pilot project)이 [2017년에 시작](https://clinicaltrials.gov/study/NCT03394703)되었다는 것을 감안할 때, 유병률은 거의 변하지 않았다는 것에서 폐암 검진은 과잉진단을 유발하지 않고, 오히려 조기 암을 잘 찾아서 다음과 같이 생존률이 증가했다는 것을 간접적으로 입증할 수 있습니다.

![image_.png](/img/natural_course_overdiagnosis/image_.png)

폐(lung)암은 항암제와 치료 기술의 발달로 2000년 이후에 전체적으로 사망률이 감소하지만, 갑상선(thyroid) 암은 진단 건수가 폭발적으로 느는 것을 확인했음에도 사망률이 거의 변화가 없다는 것을 생각하면 폐암 검진은 과잉 진단을 하지 않는다는 것을 확실히 확인할 수 있었습니다.

이렇게 폐암의 자연사와 과진단 논란에 대해 알아보았고, 폐암 검진을 하는 것이 충분히 일리가 있다는 것을 확인할 수 있었습니다.

다음 글에서 또 더 폐암 검진과 폐암 인공지능에 대해 알아보기로 합니다.

To be continued...
