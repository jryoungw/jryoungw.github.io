# Needleman-Wunsch Algorithm

# Introduction

두 DNA 염기서열, 혹은 string(문자열)이 있다고 하자. 이 두 문자열을 가장 비슷하게 정렬하는 알고리즘을 우리는 찾고 싶다. DNA의 경우 돌연변이가 일어난 상태의 두 DNA strand라도 원래 어떻게 매칭되어 있었는지 알고 싶기(추정하고 싶기) 때문이다. 예를 들어 다음 DNA double strand를 생각해보자.

$$
\text{ACCCGTATG}\\
\text{TGGGCATAC}
$$

이 DNA double strand는 잘 정렬되어 있다. 하지만 다음과 같은 mutation이 일어난 double strand를 생각해보자.

$$
\text{ACCCGTATG}\\
\text{TAGGCATAC}
$$

두 번째 자리가 $\text{C}-\text{G}$여야 하는데 $\text{C}-\text{A}$로 어긋나있다. Insertion(삽입), deletion(결실)이 경우에는 쉽게 한 자리가 어긋나있다는 사실을 알 수 있지만 어긋난 자리수가 많아지고, 길다란 double strand에서 다양한 위치에서 어긋남이 발생한다면 눈으로 봐서는 쉽게 알아챌 수가 없을 것이다. 그리고 무엇보다도 우리는 눈을 통한 어림짐작으로 수만자가 넘어가는 엄청나게 긴 DNA double strand가 잘 정렬되어 있는지 현실적으로 검토할 방법이 없다. 따라서 컴퓨터에게 이런 일을 시켜야 하는데, “가장 비슷한” double strand의 조합을 찾게 하는 것은 생각보다 까다로운 작업이다. 다음과 같은 double strand를 생각해보자.

$$
\text{ACCCGTATG}\\
\text{GCGGGCATA}
$$

위 strand를 살펴보면 제대로 위치한 부분이 9개의 base 중 2개밖에 없다. 하지만 이 double strand는 다음처럼 정렬할 수 있다:

$$
\text{ - ACCCGTATG}\\
\text{GCGGGCATA - }
$$

이렇게 빈 칸을 통해 한칸씩 밀게 되면 무려 7자리나 제대로 조합할 수 있게 된다! Needleman-Wunsch algorithm은 dynamic programming을 통해 컴퓨터가 이러한 well-alignedness를 자동으로 찾아주게 만드는 알고리즘이다. 여기까지 했으면 Needleman-Wunsch algorithm을 왜 하는지, 이 알고리즘이 무엇을 하는지는 잘 이해했을거라 생각하고 구체적인 알고리즘을 살펴보자.

# Algorithm

사실, 이론적으로야 best alignment는 항상 찾을 수 있다. Brute force로 모든 조합을 다 계산해보면 되기 때문이다. 하지만 한 자리가 증가할 때마다 4개의 base가 늘어나기 때문에 조합은 4배씩 증가할 것이고, 결국 $O(4^n)$정도의 복잡도를 가지게 되어 사실상 100 pair만 된다 하더라도 말도 안되게 경우의 수가 많아질 것이다. 이를 Needleman-Wunsch에서는 dynamic programming으로 해결한다.

먼저 두 염기 서열 $\text{GCATGCG}$와 $\text{GATTACA}$를 생각하자. 

|  |  | G | C | A | T | G | C | G |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |
| G |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |
| T |  |  |  |  |  |  |  |  |
| T |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |
| T |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |

그리고 scoring system을 하나 생각한다

- Match : 각 자리의 글자가 일치하면 $+1$을 메긴다.
- Mismatch : 각 자리의 글자가 불일치하면 $-1$을 메긴다.
- Indel : Insertion 혹은 Deletion의 경우에는 $-1$을 메긴다.

예를 들어 다음과 같은 alignment candidate는 (아무렇게나 설정했다.)

$$
\text{GCATG - CG}\\
\text{G - ATTACA}
$$

$+-++--+-$의 score를 가지므로 총 score는 $0$이 될 것이다.

이제 위 표를 채우자.

1행 1열에 먼저 0을 채우고

|  |  | G | C | A | T | G | C | G |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 |  |  |  |  |  |  |  |
| G |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |
| T |  |  |  |  |  |  |  |  |
| T |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |
| T |  |  |  |  |  |  |  |  |
| A |  |  |  |  |  |  |  |  |

1행과 1열에 indel의 누적점수를 추가해준다. 가로, 세로 방향은 indel을 의미하고 대각선 방향은 match/mismatch를 의미할 것이다.

|  |  | G | C | A | T | G | C | G |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | -1 | -2 | -3 | -4 | -5 | -6 | -7 |
| G | -1 |  |  |  |  |  |  |  |
| A | -2 |  |  |  |  |  |  |  |
| T | -3 |  |  |  |  |  |  |  |
| T | -4 |  |  |  |  |  |  |  |
| A | -5 |  |  |  |  |  |  |  |
| T | -6 |  |  |  |  |  |  |  |
| A | -7 |  |  |  |  |  |  |  |

이제 2행 2열부터 채워나가보자. 먼저 2행 2열의 $(\text{G,G})$ pair에 들어올 숫자는 다음 세 가지 가능성으로부터 출발한다:

1. 왼쪽 위 대각선의 score는 0이다. 또한 2행 2열은 $(\text{G,G})$이기 때문에 match이고 따라서 1점을 부여받아 점수는 0점에 1점을 추가한 1점이 된다.
2. 위쪽의 score는 -1이다. 또한 위에서 아래로 내려오게 되면 indel을 의미하기로 했으므로 점수는 -1점에 -1점을 부여받아 -2점이 된다.
3. 왼쪽의 score는 -1이다. 또한 왼쪽에서 오른쪽으로 가게 되면 indel을 의미하기로 했으므로 점수는 -1점에 -1점을 부여받아 -2점이 된다.

이렇게 선택하는 세 가지 경우 중 우리는 점수가 가장 큰 1번 경우의 1점을 선택하게 되고 따라서 matrix는

|  |  | G | C | A | T | G | C | G |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | -1 | -2 | -3 | -4 | -5 | -6 | -7 |
| G | -1 | 1 |  |  |  |  |  |  |
| A | -2 |  |  |  |  |  |  |  |
| T | -3 |  |  |  |  |  |  |  |
| T | -4 |  |  |  |  |  |  |  |
| A | -5 |  |  |  |  |  |  |  |
| T | -6 |  |  |  |  |  |  |  |
| A | -7 |  |  |  |  |  |  |  |

이 된다. 이 과정을 반복한다. 2행 3열은

1. (가로) 1점에 indel을 추가하여 1+(-1)=0점
2. (세로) -2점에 indel을 추가하여 (-2)+(-1)=-3점
3. (대각선) -1점에 mismatch를 추가하여 (-1)+(-1)=-2점

이므로 0점을 선택하게 되어

|  |  | G | C | A | T | G | C | G |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 0 | -1 | -2 | -3 | -4 | -5 | -6 | -7 |
| G | -1 | 1 | 0 |  |  |  |  |  |
| A | -2 |  |  |  |  |  |  |  |
| T | -3 |  |  |  |  |  |  |  |
| T | -4 |  |  |  |  |  |  |  |
| A | -5 |  |  |  |  |  |  |  |
| T | -6 |  |  |  |  |  |  |  |
| A | -7 |  |  |  |  |  |  |  |

이 되는것과 같은 식이다.

# Code Implementation

이를 파이썬 코드로 짜면 다음과 같다.

```python
def needleman_wunsch(string1:str,
                     string2:str,
                     match:Union[int, float]=1,
                     mismatch:Union[int, float]=-1,
                     indel:Union[int, float]=-1
                    ) -> Tuple[str, str]:

    scores = [[-i-j for i in range(len(string1)+1)] for j in range(len(string2)+1)]

    for idx in range(1, len(string1)+1):
        for jdx in range(1, len(string2)+1):
            candidates = []
            if string1[idx-1] == string2[jdx-1]:
                candidates.append(scores[jdx-1][idx-1] + match)
            else:
                candidates.append(scores[jdx-1][idx-1] + mismatch)
            candidates.append(scores[jdx-1][idx] + indel)
            candidates.append(scores[jdx][idx-1] + indel)
            scores[jdx][idx] = max(candidates)
    scores = [i[1:] for i in scores][1:]

    idx = len(string1)-1
    jdx = len(string2)-1

    newstr1 = string1[-1]
    newstr2 = string2[-1]

    while idx>0 and jdx>0:
        mv = [scores[jdx-1][idx], scores[jdx][idx-1], scores[jdx-1][idx-1]]
        f = lambda i: mv[i]
        index = max(range(len(mv)), key=f)
        assert index in [0,1,2]
        if index == 2:
            newstr1 = string1[idx-1] + newstr1
            newstr2 = string2[jdx-1] + newstr2
            idx -= 1
            jdx -= 1
        elif index == 1:
            newstr1 = string1[idx-1] + newstr1
            newstr2 = '-' + newstr2
            idx -= 1
        else:
            newstr1 = '-' + newstr1
            newstr2 = string2[jdx-1] + newstr2
            jdx -= 1
            
    return newstr1, newstr2
```

그리고 입력을 넣으면

```python
one = "GCATGCG"
two = "GATTACA"
new1, new2 = needleman_wunsch(one, two)
print(new1)
print(new2)
>>> GCATG-CG
>>> G-ATTACA
```

을 얻는다.