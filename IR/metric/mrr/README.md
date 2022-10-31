# MRR

## 1. MRR의 개념

* MRR (Mean Reciprocal Rank)은 우선순위를 고려한 평가 기준 중 가장 간단한 모델
* 시스템에서 가장 관련성이 높은 항목을 반환하고 해당 항목이 더 높은 위치에 결과를 보여주고자 할 때 유용한 Metric

## 2. MRR 알고리즘

![image](https://user-images.githubusercontent.com/87981867/189580005-ce125150-4d7f-4a2c-a440-37bc10f4bb70.png)
> *Q* : 총 쿼리 수

> *rank* : 첫 번째 관련 결과의 순위

* 각 사용자마다 제공한 추천 컨텐츠 중 관련 있는 컨텐츠 중 가장 높은 위치를 역수로 계산(1/rank)
* 사용자마다 계산된 점수를 모아 평균을 계산

![image](https://user-images.githubusercontent.com/87981867/189580035-e6ed61f1-1b70-4ed7-a0cf-73dbacb88eac.png)

* 예를 들어, 관련이 있는 컨텐츠 결과가 첫 번째에 나타날 경우, reciprocal rank는 1/1 = 1이 됨  

![image](https://user-images.githubusercontent.com/87981867/189580041-358ed4d3-ff04-4354-be1b-030b6d610e04.png)

* 이번에는 관련이 있는 컨텐츠 결과가 5번째에 나타날 경우에는 역수값을 취한 1/5 = 0.2가 됨

![image](https://user-images.githubusercontent.com/87981867/189580059-2d2fb5c3-eba6-41a2-9a8d-8f22324986c1.png)

* 만약 어떠한 관련 컨텐츠 결과가 나오지 않을 경우에는 reciprocal rank는 0이 됨

![image](https://user-images.githubusercontent.com/87981867/189580070-84b4f8ea-0640-4f9d-bf71-7323b4e0804b.png)

* 여러 질문(Query)을 하였을 때, 각 질문 별로 reciprocal rank 값을 구하고, 각 reciprocal rank의 평균 값이 바로 MRR 값임

## 3. MRR 특징

### 3.1 장점

(1) 간단하고 쉬움

(2) 제공된 목록 중 가장 상위의 관련된 컨텐츠에만 집중하기 때문에, 가장 관련있는 컨텐츠가 최상위에 있는가를 평가할 때 용이

(3) 새로운 컨텐츠가 아니라 이미 사용자가 알고 있는 컨텐츠 중, 가장 선호할만한 컨텐츠를 보여주고자 할 때 좋은 평가 기준이 됨

### 3.2 단점
 
(1) 제공된 목록 중 하나의 컨텐츠에만 집중하기 때문에 나머지 부분에 대해서는 평가하지 않음

(2) 관련 컨텐츠의 개수가 달라도 첫 번째 관련 컨텐츠의 위치가 같은 경우 같은 점수를 가지므로 변별력을 가지기 어려움


*참고 자료*
- https://amitness.com/2020/08/information-retrieval-evaluation/
- https://lamttic.github.io/2020/03/20/01.html
