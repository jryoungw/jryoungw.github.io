# Brief History of DICOM

DICOM은 Digital Imaging and Communications in Medicine의 약자로, 의료 영상에 관련된 이미지 파일 형식을 의미한다. 본 절에서는, DICOM의 개략적인 역사를 살펴본다.

Reference: [Digital Imaging and Communications in Medicine (DICOM): A Practical Introduction and Survival Guide](https://www.springer.com/gp/book/9783642108495)

약자

DICOM : Digital Imaging and Communications in Medicine

ACR : American College of Radiology

NEMA : National Electrical Manufacturers Associations

AAPM : American Association of Physicists in Medicine

HTML : Hypertext Markup Language

XML : Extensible Markup Language

WG : Working Group

DICOM은 약 25년 이상의 역사를 갖고 있기 때문에, 그 역사를 아는 것이 DICOM의 존재를 이해하는데 도움이 될 것이다. DICOM 표준은 계속해서 개량되고 있고, 하나로 고정된 정적인 산물이 아니다.

# 1. How Did This All Get Started?

DICOM 표준은 1983년에 최초로 만들어졌다. ACR이 DICOM 표준을 만드는 것을 주도했으며, NEMA와 협업 하에 진행하였다. 최초의 목적은 기기 회사에 관계없는 국제 표준 이미지 프로토콜을 만들자는 취지였고, 이로부터 디지털 영상의학과 PACS를 촉진하기 위해서였다. 

ACR-NEMA Digital Imaging and Communications Standards Committee로 불리는 이 연합 위원회는 많은 다른 국제 표준들을 참고하며 DICOM 표준을 만들어나가기 시작했다. (Horill et al. 2004) AAPM은 당시 자극 테이프(magnetic tape)에 이미지를 기록하는 표준을 만들어나가기 시작했다. AAPM은 모든 정보를 데이터 원소로 분할하는 방식을 선택했는데, 각 원소는 가변 길이(size)에 해당하는 유일한 이름(tag)를 부여하는 방식을 선택했다. 이 아이디어는 ACR-NEMA 그룹에 의해서 채택되었다. HTML이나 XML에 경험이 있다면, 이러한 접근 방식이 현재 널리 쓰이고 유명한 표준들에서 자주 발견됨을 알 수 있을 것이다.

ACR-NEMA 300-1985 혹은 ACR-NEMA 1.0이라고 불리는 최초 버전은 오류와 불완전함을 내포하고 있었다. 따라서 곧 사람들은 더 개량이 필요하다는 것을 알게 되었고 이러한 이유에서 ACR-NEMA는 WGs라는 아이디어를 수용했다. 이 WGs 아이디어는 표준의 각 부분을 쪼개서 전문성이 있는 소그룹으로 나누어 편찬하겠다는 아이디어를 의미한다. 최초의 WG-VI (현재는 WG-06으로 알려져 있다.)는 ACR-NEMA 1.0을 개량하기 위해 만들어졌다. 이로부터 두 번째 버전인 ACR-NEMA 300-1988 혹은 ACR-NEMA 2.0이 1988년 출간되었고 이 버전은 실제 기기들에 시나브로 스며들어갔다. 실제로 오늘날까지 ACR-NEMA 2.0으로 돌아가는 기기들을 찾을 수 있다고 한다. 현재의 버전도 ACR-NEMA 2.0을 큰 뼈대로 가진다.

컴퓨터 네트워크가 아니었다면 ACR-NEMA 2.0은 의학 세계에 더 오래 지배자로 남아있었을 수 있었을 것이다. ACR-NEMA 2.0의 컴퓨터간 전송은 매우 한정적이었다. 예를 들어서, 유저가 이미지를 원격의 다른 장비로 보낼 수는 있었겠지만, 이 표준은 이미지를 받은 기기가 그 이미지로 무엇을 해야 하는지에 대한 프로토콜을 전혀 알려주지 않았다. 따라서 단순히 이미지를 생성하고 저장하는것 이외의 프로토콜에 대한 필요성이 인식되었다.

주요한 내용들에 대한 개편의 또다른 니즈는 영상 장비들의 다양성이 증가하고 그것들 사이의 호환 프로토콜에 대한 요소였다. 즉, 이미지를 잘 만들고 저장하는것 이외에도 기기끼리 소통하는 필요성이 증대되었다는 말이다.

이러한 변화하는 요구에 발맞춰서, ACR-NEMA 표준의 세 번쨰 버전이 1992년 RSNA에서 발표되었다. 비록 프로토타입이었고 기초적이긴 했지만 말이다. 이듬해는 월간 WG 미팅으로 가득 찼었다. 1993년 9월에 ACR-NEMA 표준의 새 버전의 첫 9 부분이 출간되었고 1993 RSNA에 더 기능적으로 풍성한 형태로 발표되었다. 이 버전은 ACR-NEMA DICOM 혹은 세 번째 버전이기에 DICOM 3.0이라고 불린다.(DICOM 2.0이나 DICOM 1.0이 없음에 주의하라.) 관용적으로 3.0은 생략되기에 우리도 그냥 DICOM이라고 3.0 버전을 칭할 것이다.

아직도 DICOM 2.0을 DICOM으로 바꾸지 않은 기기들이 있다고 한다.

DICOM 3.0은 아직까지는 DICOM 4.0으로 바뀌지 않았다. 대신, 매년 DICOM WG에 의해서 DICOM이 개편되고 있으며, 이들은 PS3.X-YYYY라는 이름으로 출간된다. 여기서 3은 3.0이라는 것을 의미하고, X는 몇 번째 권인지를 나타내며 YYYY는 그 버전이 출간된 해를 의미한다. 예를 들어 PS3.5-2021은 2021년에 발간된 DICOM 3.0의 5권을 의미한다.

1. 모든 DICOM 장비들은 이들이 개발될 당시의 DICOM 스냅샷을 따르는 것이 일반적이다. 이는 매 해마다 다를 수 있다.
2. DICOM 단위들은 함께 작동해야한다. 따라서, 새로운 DICOM 장비를 과거의 장비들과 호환되게 하는 것은 최신 DICOM 특징을 반영하는 것보다 중요하다. 이 이유때문에 DICOM 제조사들은 최신 DICOM에 열광하는 편은 아니다. 심지어 대부분의 DICOM 생성 장비들은 1990년대 중반 DICOM 프로토콜을 따른다.
3. 아주 복잡한 환경에서 DICOM 솔루션을 다뤄야 할 때는, 최신 버전보다는 가장 호환이 잘 되는 버전을 고려하는 것이 바람직하다. 따라서 새로운 압축 알고리즘을 다루는 DICOM 최신 버전은 구형 DICOM 버전과 호환이 되지 않을 수 있다.

DICOM 단위의 호환성은 항상 그러하듯 DICOM Conformance Statement에 반영되어있다. DICOM 장비는 많은 옵셔널한, 그리고 차선의 특성들을 지원할 것이다.

DICOM 국제 표준은 [NEMA 홈페이지](https://www.dicomstandard.org/)에서 찾을 수 있다.
