![image](https://user-images.githubusercontent.com/87981867/212082015-7755192f-49cb-460b-af89-475378aeb9ed.png)

## 1. BentoML이란?

- 머신러닝 모델을 만들면 해당 모델을 쉽게 배포 및 테스트를 할 수 있게 해주는 라이브러리
- 간단한 코드로도 쉽게 API 서버를 구성할 수 있고, Dockerfile 제공과 함께 Docker Image를 간편하게 만들 수 있게 함

## 2. 주요 기능 및 특징

### (1) ML 프레임워크

- 다양한 머신러닝 프레임워크들을 지원(scikit-learn, tensorflow, pytorch, xgboost 등)

### (2) Yatai 서버

- Yatai 서버를 실행하여 저장된 모델, 배포된 모델을 보여줌과 동시에 관리도 가능

### (3) 컨테이너화

- docker 컨테이너 생성 및 docker image 생성 가능

### (4) 다양한 파일 생성

- 도커 파일, 학습 모델 정보, environment 등 모델 배포에 필요한 여러 파일을 자동으로 생성

### (5) API 생성

- 생성된 도커 이미지를 활용해서 도커 명령어를 통해 API serving이 가능

## 3. 사용 예시

### (1) 설치방법

```python
pip install bentoml
```

### (2) 라이브러리 구성

```
💡
1) main.py
: 전체 코드를 실행하는 main을 담당하며, 모델을 return 함 또한 가져온 모델을 BentoML에 packing 가능(*packing : 머신러닝 또는 딥러닝 모델을 저장하는 개념) 

2) bentoml_process.py
: 생성한 모델을 입력 받아 classifier 객체를 생성해서 packing을 진행한 후 이러한 환경값들을 저장하여 docker 등의 다양한 파일을 생성

3) classifier.py
: 각종 bentoml 기능을 담고 있는 파일이며, BentoService를 상속하여 사용(실행 시 Web UI 화면 호출)
```

### (3) 실행방법 및 결과

```python
bentoml serve {classifier}:{version}
>>> Running on http://127.0.0.1:5000
```

![image](https://user-images.githubusercontent.com/87981867/212082268-949a4781-5cfb-40d1-9d5b-14b07cc29d82.png)

- 이 화면을 통해서 모델에서 나온 결과값을 확인 가능

![image](https://user-images.githubusercontent.com/87981867/212082331-3ae18fbb-60a2-4f87-a5aa-49f4f6135e53.png)

- dockerfile, requirements, setup 등 배포에 필요한 여러 파일들이 자동으로 생성 됨

![image](https://user-images.githubusercontent.com/87981867/212082391-02b53450-9b18-4ff9-9851-12723383d86e.png)

- 도커 빌드를 통해 도커 이미지 생성 가능

```python
docker run -p 5000:5000 {dockerimage}
```

- 도커 이미지를 활용하여 BentoML API Serving이 가능
- docker run 명령어로 실행하고 port만 열어주면 간단히 실행 가능

```python
bentoml yatai-service-start {classifier}:{version}
>>> Running on http://127.0.0.1:5000
```

![image](https://user-images.githubusercontent.com/87981867/212082481-33922931-973f-4808-8ed4-0548df490b6b.png)

- Yatai를 실행하면 그림과 같이 Web UI를 활용하여 머신러닝 및 딥러닝 모델 관리 가능

## 4. BentoML이 API Serving에 가지는 장점

### (1) Online / Offline Serving

- BentoML은 요청(request)이 올 때마다 실시간으로 서비스가 가능
- Batch로 주기적으로 많은 양의 데이터를 한꺼번에 처리

### (2) Adaptive Micro Batching

```jsx
# latency 단위 : milliseconds
bentoml.api(mb_max_batch_size=1000, mb_max_latency=10000)
```

- BentoML은 HTTP 처리 데이터 처리 과정까지 Micro batching(작은 배치 처리를 무한히 하는 방식) 지원
- 최대 배치 사이즈와 모델 추론의 latency 제한을 설정할 수 있음

### (3) packing

- 머신러닝 모델이 준비되면 그 모델을 BentoML 환경에 맞게 packing 해주는 기능이 있음
- BentoML 실행 시 자동으로 모델 Serving에 필요한 파일들을 생성 해줌
- [setup.py](http://setup.py/), requirements.txt, config, [README.md](http://readme.md/), Dockerfile 등

![image](https://user-images.githubusercontent.com/87981867/221738884-66710762-3c1c-4070-92f2-e33f176e8bed.png)

### (4) API 코드

- API 서비스 코드 작성을 하려면 Django 또는 FastAPI 등의 프레임워크로 API 호출에 필요한 여러 스크립트를 작성해야 함
- BentoML은 decorator(데코레이터)를 사용하여 bentoml의 다양한 환경 등을 설정할 수 있음
- @env, @api, @artifacts 등 다양한 decorator 옵션을 주어 API 서비스 코드를 간단히 작성할 수 있음

```python
@env(requirements_txt_file="./requirements.txt")
@artifacts([PickleArtifact('rf_model'), PickleArtifact('lgbm_model'), PickleArtifact('mapping')])
class TitanicSKlearnClassifier(BentoService):
    def __init__(self):
        super().__init__()
        self.columns_list = ['Sex', 'Age_band', 'Pclass']

    def mapping_df(self, df):
        df['Sex'] = df['Sex'].map(self.artifacts.mapping)
        return df

    @api(input=DataframeInput(), batch=True)
    def rf_predict(self, df: pd.DataFrame):
        df.columns = self.columns_list
        print(df.head())
        print(self.artifacts.mapping)
        df = self.mapping_df(df)
        return self.artifacts.rf_model.predict(df)

    @api(input=DataframeInput(), batch=True)
    def lgbm_predict(self, df: pd.DataFrame):
        df.columns = self.columns_list
        print(df.head())
        print(self.artifacts.mapping)
        df = self.mapping_df(df)
        return self.artifacts.lgbm_model.predict(df)
```

### (5) 도커 이미지화

- BentoML은 packing된 파일들을 docker image로 생성해주는 기능이 있음
- packing 시 생성된 dockerfile을 이용하여 docker image를 build 하는 과정만 진행해주면 됨

```jsx
# docker image build 명령어
docker build -t {user} {Dockerfile이 있는 폴더 경로}
```

![image](https://user-images.githubusercontent.com/87981867/221738923-769e48af-6aea-461f-a618-5ea53f158a06.png)

- docker 환경에서 이미지 리스트를 불러올 때 사용하는 docker images 명령어를 입력하면 위 그림과 같이 도커 이미지가 생성된 것을 확인할 수 있음
- 이런 점을 비추었을 때 개발 환경이 컨테이너 환경이라면 bentoml로 도커 이미지 빌드가 유리함

## (6) API Serving 및 호출

- 기존 API Serving 및 호출 시에는 위에서 언급한 것처럼 Django, FastAPI 등의 프레임워크로 코드를 작성하고 url 정보를 받아 API Serving을 실시한 후, postman tool로 api 호출 결과를 확인했었음
- BentoML은 이러한 복잡한 과정이 아닌 빌드한 도커 이미지로 API Serving 및 호출이 가능함

```jsx
# API Serving 명령어
docker run -p 5000:5000 {dockerimage}
```

- 도커 run 명령어를 통해 API Serving 실행됨

![image](https://user-images.githubusercontent.com/87981867/221738956-198adc74-8780-463a-8e90-c88ded2fd2d6.png)

- 호출 결과를 확인하고 싶으면 위 그림과 같은 명령어를 통해 곧 바로 결과를 확인할 수 있음

출처 : [https://lsjsj92.tistory.com/621](https://lsjsj92.tistory.com/621)
