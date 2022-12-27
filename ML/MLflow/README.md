# Pytorch Lightning을 활용하여 모델 성능 극대화하는 방법

## 1. User workers in DataLoaders


```
DataLoader(dataset, num_workers=8)
```

- DataLoaders 에서 **num_workers**를 활용
- num_workers를 설정함으로써 프로세스를 동시에 여러개 올릴 수 있음
- 데이터 로딩 과정에서 몇 개의 멀티프로세스를 올릴 건지 설정
- 내 PC가 사용하는 GPU 개수에 4를 곱한 값을 추천

```
✅ num_workers= 4 * num_GPU
```

## 2. Pin memory


```
DataLoader(dataset, pin_memory=True)
```

- DataLoaders 에서 **pin_memory**를 활용
- 예를 들어, 식당의 테이블을 예약해두는 것과 같음
- 식당 주인은 예약 잡아둔 테이블을 다른 손님들에게 내어줄 수는 없을 것
- 여기서 **'식당의 테이블을 예약하는 것'**이 **'pin_memory 를 True** 로 설정해주는 것'

```
✅ 식당: CPU, 테이블: GPU와 통신하기 위한 CPU의 메모리 공간
```

- CPU가 GPU에 데이터를 전송하기 위해서는 GPU와 통신이 되어야 함
- 이 통신 역할을 담당하는 프로세스도 당연히 CPU 메모리를 필요
- 이 CPU와 GPU 간 통신 목적의 메모리를 무조건적으로 일정량 이상 확보해둔다는 의미

![https://velog.velcdn.com/images/jaylnne/post/c2f01bdd-90ec-4e87-b325-0b9b60815318/image.png](https://velog.velcdn.com/images/jaylnne/post/c2f01bdd-90ec-4e87-b325-0b9b60815318/image.png)

> *그런데 왜 그렇게 하면 좋은 걸까?*
> 
- pin_memory 를 활성화했을 때 CPU가 GPU로 데이터를 전송하는 속도가 빨라지기 때문
- 속도 차이가가 의미 없을만큼 데이터가 작거나, 애초에 처음부터 데이터를 GPU에 로드했다면 상관이 없음

## 3. Avoid CPU to GPU transfers or vice-versa

```
# BAD
.cpu()
.item()
.numpy()

# GOOD
.detach()
```

- CPU와 GPU 사이에 데이터가 전송되는 과정을 피하라고 하면서 추천하는 메소드와 추천하지 않는 메소드를 구분
- BAD에 해당하는 코드들은 데이터를 CPU 에 올리는 역할을 함
- CPU에서 GPU로 데이터를 전송하는 일에도 시간이 걸리기 때문에 GPU의 데이터를 굳이 CPU로 옮기는 해당 코드들은 비추천한다고 함
- 반대로 GOOD에 해당하는 코드는 사용을 추천하고 있는데, 모델이 학습하는 과정에서 back propagation을 하기 위해 사용하는 계산 그래프를 없애고 싶다면 **.detach()** 코드를 이용

## 4. Construct tensors directly on GPU

```
# BAD
t = tensor.rand(2, 2).cuda()

# GOOD
t = tensor.rand(2, 2, device=torch.device('cuda'))
```

- CPU 와 GPU 사이에 데이터를 전송하게 되면 속도가 많이 느려짐
- 가장 좋은 방법은 GPU에 곧장 데이터를 로드하는 방법

## 5. Use DistributedDataParallel not DataParallel


- 여러 개의 GPU 를 이용할 때 도움이 되는 방법으로 DataParallel(DP)이 아닌 DistributedParellel(DDP) 을 사용
- **DP** 방식은 multi-threading 이고 **DDP** 방식은 multi-processing이다.
- 프로세스(process)란 엄밀히 말해 작업을 위해 실행되어야 할 명령어의 목록(그 목록을 가지고 있는 메모리)을 뜻하는 말이며, 이 명령어 목록의 명령어 하나하나를 실행하는 실제 작업자가 스레드(thread)
- 멀티 스레딩이란 프로세스는 하나, 이 프로세스의 명령어를 실행하는 스레드는 여럿이라는 뜻이고, 멀티 프로세싱이란 반대로 프로세스가 여러 개, 각 프로세스를 실행하는 스레드는 하나씩이라는 뜻

```
# DP
Trainer(distributed_backend='dp', gpus=8)

# DDP
Trainer(distributed_backend='ddp', gpus=8)
```

> *그런데 왜 multi-processing인 DDP 방식이 multi-threading인 DP 방식보다 빠른 걸까?*
> 

그 답은 바로 python 의 GIL(Global Interpreter Lock) 때문이다. 또 모르는 용어가 나왔다고 당황하지 말자. Lock 이라는 단어가 포함되어 있으니 무언가를 못하도록 '잠그는' 기능일 것이다. 무엇을 못하도록 할까? 여러 개의 스레드가 동시에 실행되지 못하도록 막는 기능이라고 생각하면 된다. 그래서 python 언어를 기반으로 하는 pytorch 에서는 DP 방식이 아닌 DDP 방식을 추천하는 것이다.

## 6. Use 16-bit precision

- 32-bit로 구성된 데이터를 16-bit 로 변환하여 사용
- 32-bit 데이터를 16-bit 로 변환하면 데이터가 차지하는 메모리 용량이 절반으로 줄어 모델 학습의 배치 사이즈를 두 배로 늘려서 학습 속도를 더 빠르게 향상시킬 수가 있음
- 또한 특정한 GPU 모델(C100, 2080Ti)은 16-bit 계산에 특화되어 있기도 하다고 하여 32-bit 계산을 시행할 때보다 16-bit 데이터를 계산할 때 속도가 3배에서 많게는 8배까지도 빨라질 수 있음

```
Trainer(precision=16)
```

> *pytorch ligntning 을 사용하면 간단하게 설정 가능*
> 

```
Note) pytorch 1.6 이전 버전에서는 Nvidia Apex 도 함께 설치해주어야 한다. 하지만 그 이후 버전에서는 pytorch ligntning 을 사용할 때 자동으로 pytorch 버전을 인식해 32-bit 로 진행할지 16-bit 로 진행할지 결정해 준다고 한다.
```

## 7. Profile your code

- 코드가 실행한 프로세스가 어떻게 돌아가고 있는지를 자세히 분석하여 보여주는 것
- 작업마다 시간이 얼마나 걸렸고 메모리를 얼마나 차지했는지 등을 한눈에 보여주니까, 모델의 학습 속도가 너무 느리다고 생각될 때 이 프로파일링을 이용하면 어디서 병목이 발생하고 있는지 쉽게 찾아낼 수가 있을 것

```
Trainer(profile=True)
```

- 위 코드와 같이 **profile=True**을 활성화시켜주면, 아래 그림과 같은 결과를 얻을 수 있음

![https://velog.velcdn.com/images/jaylnne/post/1621e393-1ef5-4325-9c63-c1dc59b192fb/image.png](https://velog.velcdn.com/images/jaylnne/post/1621e393-1ef5-4325-9c63-c1dc59b192fb/image.png)

- 아래 코드 처럼 다른 종류의 profiler를 지정해주면 아래와 같이 다른 형태의 결과물이 나올 수도 있음

```
profiler = AdvancedProfiler()
Trainer(profiler=profiler)
```

![https://velog.velcdn.com/images/jaylnne/post/42e1e8b5-4ab0-4d35-8ed7-d9a335c4550e/image.png](https://velog.velcdn.com/images/jaylnne/post/42e1e8b5-4ab0-4d35-8ed7-d9a335c4550e/image.png)

출처 : [https://velog.io/@jaylnne/Pytorch-머신러닝-모델의-성능을-극대화하는-7가지-팁](https://velog.io/@jaylnne/Pytorch-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8%EC%9D%98-%EC%84%B1%EB%8A%A5%EC%9D%84-%EA%B7%B9%EB%8C%80%ED%99%94%ED%95%98%EB%8A%94-7%EA%B0%80%EC%A7%80-%ED%8C%81)
