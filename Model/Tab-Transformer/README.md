# Tab-Transformer

## **1. Introduction**

- tabular 데이터에 대해 tree-based 모델이 뛰어난 성능을 보이는 것은 사실이지만, 한계점 또한 분명히 존재
- tabular 데이터와 image/text를 한 번에 학습시키는 multi-modality를 확보할 수 없고, 스트리밍 데이터에 대해 지속적인 학습 또한 불가능한 측면이 있음
- 단순한 MLP로 임베딩을 한다고 하면, 그 얕은 구조와 context-free 임베딩이라는 특성 때문에 성능 측면에서 아쉬운 부분이 많음
- 본 논문에서는 tree-based 모델에 필적하면서도 MLP보다 뛰어난 구조의 알고리즘

## **2. TabTransformer**

![https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/str.PNG](https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/str.PNG)

- `DLRM` 처럼 연속형 변수와 범주형 변수의 처리 방법가 다름
- 연속형 변수는 **layer normalization**를 거치고 난 후 최종 layer로 바로 투입되는 형태이지만, 범주형 변수의 경우 **Column Embedding** 과정을 거친 후 **Transformer** 구조를 통과 한 후에 최종 layer로 투입 됨
- Column Embedding은 범주형 변수가 m개가 존재한다고 할 때, 각각의 변수에는 또한 여러 class가 존재하며, Column Embedding을 통과하게 되면, m개의 범주형 변수는 m개의 임베딩 벡터로 변환 됨
- 만약 길이가 d라고 한다면, 길이 d를 갖는 m개의 벡터를 갖게 될 것
- i번째 범주형 변수가 di개의 class를 갖고 있다면, 임베딩 테이블 eϕi는 di+1 개의 임베딩을 갖게 되며, 1개가 추가된 것은 결측값에 대응하기 위함임
- 해당 범주형 변수에 결측값이 많은 경우 별도의 임베딩을 생성하면 되고, 만약 충분하지 않다고 하면 다른 임베딩 벡터의 평균 값 등을 이용할 수도 있음
- 모든 범주형 변수의 각 class에 대해 독립적인 임베딩 벡터를 만들 수도 있지만, 각 범주형 변수는 분명 다른 특성을 갖게 됨
- 예를 들어 성별, 직업 이란 2개의 범주형 변수가 있다고 하면, 남성/여성이라는 특성은 분명 직업과는 다른 종류의 의미를 갖고 있을 것이며, 이 때문에 같은 변수 내에서 일부 같은 parameter를 공유하게 설정할 수 있음
- i 변수의 j class에 대한 변환을 식으로 표현하면 아래와 같음

![image](https://user-images.githubusercontent.com/87981867/223962606-c091c353-8ada-4e34-98c3-96429d9cabd9.png)

- 이 때 c라고 하는 각 변수 내에 존재하는 공유되는 parameter를 어느 정도 비중으로 가져갈 지는 실험의 영역
- 즉, l은 hyper-parameter에 해당하며, 적정한 l을 찾는 것은 실험으로 해결해야하는 부분이지만 논문에서는 1/4 또는 1/8이 가장 적절한 비율이라고 판단
- tabular 데이터에서는 변수 간 순서라는 것이 존재하지 않는 경우가 많기 때문에, positional encoding을 쓰는 대신 이런 식으로 다른 중요한 정보를 활용할 수 있음
- 이렇게 Column Embedding을 통해 생성된 벡터는 Transformer layer를 통과하게 되고, 통과한 결과물은 아래와 같이 표현할 수 있음

![image](https://user-images.githubusercontent.com/87981867/223962666-77e240da-18fe-4729-82a5-c4dcb52aacfe.png)

- 이 벡터들을 **Contextualized Embedding**이라고 부르며, top MLP에 투입되기 전 연속형 변수인 xcont 와 합쳐지게 되고, 이 concatenated 벡터의 차원은 (d∗m+c)
- top MLP를 거치면 최종 output이 산출

## **3. Experiments**

- 기본적인 MLP와의 성능 비교는 아래와 같음

![https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/01.PNG](https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/01.PNG)

- noisy 데이터와 결측값이 있는 데이터에 대해서도 `TabTransformer`는 기본적인 MLP 보다 더 높은 성능을 보여줌(robust)

![https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/TWO.PNG](https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/TWO.PNG)

- 지도 학습 상의 모델 성능을 보면, `TabTransformer`는 GBDT에 필적하는 성능을 보임을 알 수 있음

![https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/03.PNG](https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/03.PNG)

- 부록에 보면 Column Embedding에서 cϕi의 비율에 대한 실험이 나오는데, Transformer Layer의 수에 따라 조금씩 다르지만 보통 1/4 ~ 1/8의 비율이 높은 성능을 보여줌을 알 수 있음
- Column Embedding이 아예 없는 경우가 제일 좋지 않은 성능을 보여준 것도 확인해 봐야할 점

![https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/04.PNG](https://greeksharifa.github.io/public/img/Machine_Learning/2022-03-13-tab-transformer/04.PNG)

## **4. Conclusion**

- `TabTransformer`는 tabular 데이터를 이용한 딥러닝 알고리즘으로 MLP, GBDT에 비해 차별화된 장점을 갖고 있는 방법론
- 다양한 유형의 데이터를 소화할 수 있으면서도 안정적인 성능을 낼 수 있는 알고리즘으로 평가할 수 있음
