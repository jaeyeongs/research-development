## BM25 (Best Match 25)

### (1) 개념

* 주어진 쿼리에 대해 문서와의 연관성을 평가하는 랭킹 함수로 사용되는 알고리즘으로, 검색 알고리즘 중 SOTA로 알려짐
* BM25 알고리즘은 기존에 IR(information retrieval)분야에서 사용되는 TF-IDF 알고리즘을 변형 시킨 형태
* ElasticSearch 5.0부터 기본(default) 유사도 알고리즘으로 BM25 알고리즘을 채택

### (2) TF (Term Frequency)
![image](https://user-images.githubusercontent.com/87981867/190080374-28755046-05c5-4a83-94d9-dc31f32a5060.png)

> *freq*: 문서에 매칭된 키워드 수

> *k1*: 1.2(default)

> *b*: 0.75(default) 

> *dl*: 실제 문서가 검색된 문서의 길이

> *avgdl*: 평균 필드의 길이

* 특정 용어가 하나의 문서에 얼마나 많이 등장했는지 의미하는 지표
* 일반적으로 특정 용어가 문서에서 많이 등장한다면 그 용어는 문서와 연관되어 있을 확률이 높음 

### (3) IDF (Inversed Document Frequency)
![image](https://user-images.githubusercontent.com/87981867/190080438-efd7b126-240d-4e83-b43d-4160165e8669.png)

> *n*: 문서에 나타난 키워드 수

> *N*: 전체 문서의 수

* 특정 용어가 얼마나 자주 등장했는지 의미하는 지표
* 문서 내에서 발생 빈도가 적을수록 가중치를 높게 줌
* 문서 안에서 용어가 몇 번 등장하는지는 고려하지 않고, 전체 문서 중 해당 용어가 등장하는 문서 수를 고려

### (4) Score 계산
![image](https://user-images.githubusercontent.com/87981867/190080461-231ca613-2f81-4e8e-baee-3275252d72ec.png)

### (5) TF-IDF vs BM25

#### 1) TF

![image](https://user-images.githubusercontent.com/87981867/190080485-74b445f9-0f39-4397-ad45-c17b8cbfb6ee.png)

* TF에서는 단어 빈도가 높아질수록 검색 점수도 지속적으로 높아지는 반면, BM25에서는 특정 값으로 수렴

#### 2) IDF

![image](https://user-images.githubusercontent.com/87981867/190080504-37322644-42ef-424f-aa78-41f97c85ef32.png)

* BM25에서는 DF가 높아지면 검색 점수가 0으로 급격히 수렴하므로, 불용어(stop words)가 검색 점수에 영향을 덜 미침

#### 3) norm

![image](https://user-images.githubusercontent.com/87981867/190080536-5b9bdc0a-ece2-441f-9bf0-0a039f5c7fa3.png)

* BM25에서는 문서의 평균 길이(avgdl)를 계산에 사용하며, 문서의 길이가 검색 점수에 영향을 덜 미침
