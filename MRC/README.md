# MRC(Machine Reading Comprehension)


## 1. MRC 개념

**MRC (Machine Reading Comprehension)**

: 기계 독해(Machine Reading Comprehension)란 주어진 지문(context)을 이해하고, 주어진 질의 (Query/Question)의 답변을 추론하는 문제

![image](https://user-images.githubusercontent.com/87981867/173344628-57ef282e-a1bd-41ee-a916-c5cf88d1695b.png)


## 2. MRC의 종류

**(1) Extractive Answer Datasets**

: 질의 (question)에 대한 답이 항상 주어진 지문 (context)의 segment (or span)로 존재
ex) Span Extraction: SQuAD, KorQuAD, NewsQA, Natural Questions, etc

**(2) Descriptive/Narrative Answer Datasets**

: 답이 지문 내에서 추출한 span이 아니라, 질의를 보고 생성 된 sentence (or free form)의 형태
ex) MS MARCO (Bajaj et al., 2016), Narrative QA

**(3) Multiple choice Datasets**

: 질의에 대한 답을 여러 개의 answer candidates 중 하나로 고르는 형태
ex) MCTest(Richardson et al., 2013), RACE, ARC, etc.


## 3. 평가 방법

**Exact Match / F1 Score**

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
