# TextRank

## 1. Introduction

* TextRank는 Mihalcea(2004)이 제안한 알고리즘으로 텍스트에 관한 graph-based ranking model로써, Google의 PageRank를 활용한 알고리즘
* 텍스트 요약에는 크게 추출적 요약(Extractive Summarization)과 추상적 요약(Abstractive Summarization)으로 나뉘는데, TextRank는 추출적 요약(Extractive Summarization)에 해당

## 2. Background

### 2.1 Graph

- Graph는 vertex와 edge로 구성되었으며, vertex는 정점, edge는 정점과 정점을 연결하는 간선을 의미

![image](https://user-images.githubusercontent.com/87981867/200122520-aaf273f0-6944-4449-8e98-a4a13566823d.png)

- 그래프 구조는 edge의 방향 유무에 따라 undirected graph와 directed graph로 나뉨

![image](https://user-images.githubusercontent.com/87981867/200122522-1ec8cdfb-d7e3-4df6-bbc9-b98360bd9f38.png)

- edge를 동일한 값으로 가정하는 unweighted graph와 가중치를 갖도록 하는 weighted graph(가중 그래프)가 존재

![image](https://user-images.githubusercontent.com/87981867/200122529-5431043e-40bc-4b56-975e-b13aef9edea9.png)

### 2.2 Graph-based ranking

- 그래프 기반의 랭킹 알고리즘은 vertex(정점)의 local한 정보만 반영하지 않고, 전체 그래프의 global information을 재귀적으로 반영하여 vertex(정점)의 중요도를 결정하는 방법론
- 그래프 기반의 랭킹 모델은 쉽게 설명하면 **voting** 혹은 **recommendation** 과 같음
- 그래프의 vertex가 다른 vertex와 연결되어 있다면, 이는 서로에게 **voting** 했음을 의미하며, 더 많은 연결은 갖는 vertex는 많은 **voting** 을 받은 것으로 간주
- 또한 **voting** 자체의 중요도는 **voting** 을 행사하는 vertex의 중요도에 의해 결정
- 따라서 vertex의 중요도는 '얼마나 중요한 vertex들로 부터 voting을 받았는가'로 부터 판단이 가능하며, 이러한 중요도는 vertex의 랭킹을 결정할 수 있는 요소

![image](https://user-images.githubusercontent.com/87981867/200122536-7a196b08-8958-4ef6-b490-b5b858181b5e.png)

## 3. Model Architecture

* TextRank 알고리즘은 PageRank를 text 데이터에 적용하기 위한 variation 구조
* Keyword Extraction과 Sentence Extraction을 위한 두 개의 TextRank 방법론을 제시

![image](https://user-images.githubusercontent.com/87981867/200122543-530fc1f7-a63f-4619-b7e8-cfb1f2ff29ba.png)

- PageRank는 vertex의 중요도를 위와 같이 계산
- 기본적으로 unweighted, directed graph를 구성하여 vertex의 중요도를 계산

![image](https://user-images.githubusercontent.com/87981867/200122547-efba2693-a292-4833-8423-26cf03a68791.png)

- 반면에 TextRank는 weighted graph와 undirected graph 또한 중요도를 계산할 수 있도록 개념을 확장
- 이는 복잡한 연관 관계를 갖는 text data의 특성을 반영하기 위한 것이며, TextRank의 그래프를 구성할 때에는 directed/undirected, weighted/unweighted의 형태 중 자유롭게 선택이 가능
- weighted graph를 고려한다면, TextRank의 vertex 중요도는 위와 식과 같이 가중합 과정을 통해 계산

## 4. TextRank for Keyword Extraction

* TextRank의 keyword extraction 알고리즘은 다음과 같이 비지도 학습으로 진행

(1) Text를 토큰화 하고, 필터링을 위해 POS 태깅을 진행

![image](https://user-images.githubusercontent.com/87981867/200122554-47cc12fc-12b7-4711-9311-8ff290afd80f.png)

(2) 필터링을 진행한 vertex를 그래프에 추가하고, Co-occurrence를 고려하여 edge 또한 추가

(3) 초기 vertex 중요도를 1로 설정하고 수렴할 때까지 알고리즘을 반복

![image](https://user-images.githubusercontent.com/87981867/200122560-03013699-8923-4d1a-a840-b6c5c1e49782.png)

(4) 최종적으로 얻은 중요도를 정렬하여 Top-N개의 vertex를 문장의 keyword로 정의

![image](https://user-images.githubusercontent.com/87981867/200122564-9efa56c5-c738-4a2a-ab60-da2ea1d6c790.png)

## 5. TextRank for Sentence Extraction

* Sentence Extraction을 위한 TextRank는 문장에 중요도를 부여

![image](https://user-images.githubusercontent.com/87981867/200122566-ce4f19b2-91be-4749-9bc0-fee1a4b070e3.png)

(1) 각 문장에 대한 인덱스를 지정

![image](https://user-images.githubusercontent.com/87981867/200122579-de410817-8ab0-4555-9593-88a2b2ceec4f.png)

(2) 그래프에 문장을 vertex로 추가하고, 주어진 수식을 이용하여 vertex 사이의 edge또한 정의

(3) Vertex의 중요도를 초기화하고 수렴할 때까지 알고리즘을 반복

![image](https://user-images.githubusercontent.com/87981867/200122594-80cbc2d8-517e-42e7-9d14-e3b69132791b.png)

(4) 최종적으로 정렬을 통해 중요도가 높은 문장들을 사용하여 문서에 대한 요약을 생성

![image](https://user-images.githubusercontent.com/87981867/200122607-8bd7c7a0-f7ee-4115-83cf-3534279b36d4.png)
