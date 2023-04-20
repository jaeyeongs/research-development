# MRC(Machine Reading Comprehension)


## 1. MRC 개념

### MRC (Machine Reading Comprehension)

: 기계 독해(Machine Reading Comprehension)란 주어진 지문(context)을 이해하고, 주어진 질의 (Query/Question)의 답변을 추론하는 문제

![image](https://user-images.githubusercontent.com/87981867/173344628-57ef282e-a1bd-41ee-a916-c5cf88d1695b.png)


## 2. MRC의 종류

### Extractive Answer Datasets

- 질의 (question)에 대한 답이 항상 주어진 지문 (context)의 segment (or span)로 존재

ex) Span Extraction: SQuAD, KorQuAD, NewsQA, Natural Questions, etc

### Descriptive/Narrative Answer Datasets

- 답이 지문 내에서 추출한 span이 아니라, 질의를 보고 생성 된 sentence (or free form)의 형태

ex) MS MARCO (Bajaj et al., 2016), Narrative QA

### Multiple choice Datasets

- 질의에 대한 답을 여러 개의 answer candidates 중 하나로 고르는 형태

ex) MCTest(Richardson et al., 2013), RACE, ARC, etc.

### Extraction-Based MRC

![image](https://user-images.githubusercontent.com/87981867/220810999-2e3b943f-dbc1-494f-8af9-5cdae6092e0d.png)

- 지문(Context) 내 답의 위치를 예측 -> 분류 문제(Classification)

### Generation-Based MRC

![image](https://user-images.githubusercontent.com/87981867/220811026-3d37f14b-33f5-4fd4-9bd9-ebd1ed11432c.png)

- 주어진 지문과 질의(Question)를 보고 답변을 생성 -> 생성 문제(Generation)

### Extraction VS Generation

**(1) Tokenization**

![image](https://user-images.githubusercontent.com/87981867/220811368-4d58ede5-a11e-42cd-9fa5-f6097e31a0ea.png)

- 토크나이저의 경우 WordPiece 방식으로 사용
- 미국이나 군대같은 단어는 자주 사용되므로 단어 자체가 그대로 토큰으로 유지되지만 직위같은 경우에는 직과 위로 나뉜것을 볼 수 있음

**(2) Special Token**

![image](https://user-images.githubusercontent.com/87981867/220811485-3ffb4b44-bfc0-40f9-85e7-1ce5ab39bae0.png)

- Generation에서 토큰을 사용하는지 또는 텍스트 포맷을 사용하는지는 사용하는 모듈에 달려있

**(3) 출력 표현 - 정답출력**

![image](https://user-images.githubusercontent.com/87981867/220811619-cb12fced-d574-42ef-b49d-ea713afa20e4.png)


## 3. 평가 방법

### Exact Match / F1 Score

: 답변이 지문 내에 존재하는 경우 (extractive answer)와 주어진 선택지 중 답을 고르는 경우 (multiple choice answer)에 쓰임

**(1) EM (Exact Match)**

- 예측한 답과 ground-truth이 정확히 일치하는 샘플의 비율
- 모델이 정답을 정확히 맞춘 비율
- Accuracy 측정 방식과 유사

![image](https://user-images.githubusercontent.com/87981867/173344742-63a974d0-1d6f-47b5-a13b-02cd00783470.png)

ex) 모범 답변 : 안녕하세요 -> 추론 답변 : 안녕하세요(정답) 

**(2) F1 Score**

- 예측한 답과 ground-truth&사이의 token&overlap을 F1으로 계산
- 모델이 낸 답안과 정답을 음절 단위로 비교해서 정답과 겹치는 부분을 고려하여 일종의 부분 점수를 인정한 점수

ex) 모범 답변 : 안녕하세요 -> 추론 답변 : 안녕하세(정답인정)
