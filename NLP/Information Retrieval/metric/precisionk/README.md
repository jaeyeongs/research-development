# Precision@k

## 1. Precision@k의 개념

* Precision@k는 상위 k개 결과에서 관련성이 있는 항목이 얼마나 있는지 나타냄
* 즉, 추천한 아이템 k개 중에 실제 사용자가 관심있는 아이템의 비율을 의미

## 2. Precision@k 알고리즘

![image](https://user-images.githubusercontent.com/87981867/189897578-8d07e002-d75d-4de5-9a2c-339e15226120.png)

* 기존의 머신러닝 평가 지표인 Precision 개념과 유사
* k=1일 경우, 관련 컨텐츠가 첫 번째 결과에 나오는 비율을 말함
* Precision@k의 값은 0~1 사이의 값을 가지며, 1에 가까울 수록 좋은 성능을 의미

![image](https://user-images.githubusercontent.com/87981867/189897602-d67363d1-b2b3-406a-8cc7-b41fccf637d9.png)

* Precision@1의 경우, 관련 컨텐츠가 첫 번째에 1개 나왔기 때문에 1/1 = 1이 됨 

![image](https://user-images.githubusercontent.com/87981867/189897623-bd398062-539c-4fa9-b439-1c1911c498ac.png)

* Precision@2의 경우, 관련 컨텐츠가 2번째 결과 중에 1개의 관련 컨텐츠가 나왔기 때문의 그 비율은 1/(1+1) = 0.5

![image](https://user-images.githubusercontent.com/87981867/189897645-66e636a2-bd18-4341-83cf-e1e46c95c031.png)

* k값에 따라 Precision@k 값은 위와 같이 계산됨 

![image](https://user-images.githubusercontent.com/87981867/189897656-4f2ca371-320f-4aea-9579-24294295a869.png)

* Model A와 Model B 모두 k=5일 때, 각 모델의 결과 비교
* Model A의 경우, 관련 컨텐츠가 1~3번째 결과에 나타났고, 5번째까지 관련 컨텐츠의 비율은 3/5 = 0.6
* Model B의 경우, 관련 컨텐츠가 3~5번째 결과에 나타났고, 5번째까지 관련 컨텐츠의 비율은 Model A와 동일하게 3/5 = 0.6
* Precision@k은 관련 컨테츠의 비율만을 고려하기 때문에 몇 번째에 결과가 등장했는지 크게 중요하지 않음

*참고 자료*
- https://amitness.com/2020/08/information-retrieval-evaluation/
- https://sungkee-book.tistory.com/11
