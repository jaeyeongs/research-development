![image](https://user-images.githubusercontent.com/87981867/211442559-94926bcf-5c95-4df2-b819-000b2403905e.png)

## MLflow란?

- MLflow는 머신러닝 모델의 실험을 추적하고 모델을 공유 및 배포할 수 있도록 지원하는 라이브러리
- 머신러닝 학습과 관련된 전반적인 Lifecycle을 지원해주는 라이브러리

## 주요 기능 및 특징

### (1) MLflow Tracking

- 머신러닝 모델을 학습시킬 때 생기는 각종 파라미터 관리와 머신러닝 모델 훈련이 끝난 후 metric의 결과 등을 logging하고 그 기록 결과를 Web UI로 확인 가능

### (2) MLflow Projects

- 생성한 모델을 재생성 하고 실행할 수 있도록 코드 패키지 형식으로 지원
- 생성된 모델 환경을 재사용할 수 있음

### (3) MLflow Models

- 동일한 모델을 Docker, Apache Spark, AWS 등의 인프라에서 쉽게 배치할 수 있도록 지원

### (4) MLflow Model Registry

- MLflow 모델의 전체 Lifecycle을 공동으로 관리하기 위한 모델 저장소, API, UI

## 사용 예시

### (1) 설치방법

```jsx
pip install mlflow
```

### (2) 라이브러리 구성

<aside>
💡 1) main.py

: 전체 코드를 실행하는 main을 담당하며, model.py에서 넘겨온 model 정보 등을 받아서 MLflow에서 제공해주는 metric,  파라미터, 모델 등에 정보를 저장하여 관리될 수 있도록 함

2) model.py

: 머신러닝 모델을 가지고 데이터를 훈련시키고 훈련된 모델과 모델 하이퍼파라미터 정보를 저장함

</aside>

### (3) 실행방법 및 결과

```jsx
mlflow ui
>>> Starting gunicorn 20.1.0
>>> Listening at: http://127.0.0.1:5000
>>> Using worker: sync
>>> Booting worker with pid: 4122
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/63181c12-70bb-47a5-95e3-0a066e7a3640/Untitled.png)

- start time, user, source, version, models, metrics 등을 확인할 수 있음
- 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a939614-02c3-4376-b2ad-3b7c8c4c7578/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4839d97-29a0-41cf-bd09-163be45948b1/Untitled.png)

- 모델에 사용된 파라미터 값과 사용된 모델의 metric(accuracy, f1-score, precison 등) 결과 확인 가능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/01841541-88c6-42e7-a749-680c8a6ea9e2/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8fa37aa4-88d8-4725-b1ef-59d70f8ab281/Untitled.png)

- prediction으로 만들 수 있는 방법에 대한 설명과 머신러닝 모델 파일 내용 확인 가능

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/47cdb1e3-5f05-4839-b67e-b877d62f9f3f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8de5e963-66dd-4fc6-854a-b9a73cf668d3/Untitled.png)

- 딥러닝 모델 또한 모델 정보, metric, prediction 정보 확인 가능

출처 : [https://lsjsj92.tistory.com/623](https://lsjsj92.tistory.com/623)
