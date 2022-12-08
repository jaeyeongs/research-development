## 정보 검색(IR) 엔진 평가 모듈 개발
    
|  | BM25 Okapi | BM25 Plus | BM25 L |
| :---: | :---: | :---: | :---: |
| MRR | 0.802 | 0.804 | 0.799 |
| Precision(k=10) | 0.898 | 0.898 | 0.898 |
    
자세한 내용은 [BM25](https://github.com/jaeyeongs/bm25) 레파지토리 참고
    
## 정보 검색(IR) 엔진 개발
    
![image](https://user-images.githubusercontent.com/87981867/205571830-7234c396-f4ae-4959-8399-e1ebe0e85922.png)

|  | BM25 Okapi+KoSentence-BERT | BM25 Plus+KoSentence-BERT | BM25 L+KoSentence-BERT |
| :---: | :---: | :---: | :---: |
| MRR | 0.727 | 0.727 | 0.726 |
| Precision(k=10) | 0.899 | 0.898 | 0.898 |

- BM25 알고리즘에서 나온 결과를 KoSentence-BERT 모델을 추가하여 검색된 문서를 재순서화하는 엔진 개발
        
## 정보 검색(IR) 엔진 고도화-1 : 모델 학습 & softmax
    
![image](https://user-images.githubusercontent.com/87981867/205571900-8637625d-691f-4bfa-b73c-4288f5ec98ee.png)
         
|  | BM25 Okapi+KoSentence-BERT |
| :---: | :---: |
| MRR | 0.835 |
| Precision(k=10) | 0.899 |

- KorQuAD v1.0 Dataset을 KorSTS Dataset 형식으로 가공 후 60만건 학습
- KorQuAD v1.0 Dataset이 학습된 모델에 Paired Question Dataset 6천건 추가 학습
- BM25에서 나온 각 문서의 Score 값을 softmax를 통해 0~1 사이의 값으로 변환
- 변환된 각 문서의 softmax 값과 KoSentence-BERT 모델에서 나온 코사인 유사도 값을 통해 최종 스코어 계산

## 정보 검색(IR) 엔진 고도화-2 : 형태소 분석
    
![image](https://user-images.githubusercontent.com/87981867/205571980-fb95067f-51c4-4da2-9fb4-fccc44f34ab8.png)
        
|  | Kkma | Nori |
| :---: | :---: | :---: |
| MRR | 0.9216 | 0.9374 |
| Precision(k=10) | 0.9846 | 0.9889 |

- 형태소 분석 모듈 추가(Kkma, Nori)
- Nori 형태소 분석기 사용



