![image](https://user-images.githubusercontent.com/87981867/212082015-7755192f-49cb-460b-af89-475378aeb9ed.png)

## BentoML이란?

- 머신러닝 모델을 만들면 해당 모델을 쉽게 배포 및 테스트를 할 수 있게 해주는 라이브러리
- 간단한 코드로도 쉽게 API 서버를 구성할 수 있고, Dockerfile 제공과 함께 Docker Image를 간편하게 만들 수 있게 함

## 주요 기능 및 특징

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

## 사용 예시

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

출처 : [https://lsjsj92.tistory.com/621](https://lsjsj92.tistory.com/621)
