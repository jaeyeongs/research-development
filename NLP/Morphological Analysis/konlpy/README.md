# KoNLPy를 활용한 형태소 분석

## 1. KoNLPy

한국어 정보처리를 위한 파이썬 라이브러리

https://konlpy.org/ko/latest/index.html

### KoNLPy 형태소 분석기
- Hannanum(한나눔) : KAIST Semantic Web Research Center 개발(http://semanticweb.kaist.ac.kr/hannanum/)
- Kkma(꼬꼬마) : 서울대학교 IDS(Intelligent Data Systems) 연구실 개발(http://kkma.snu.ac.kr/)
- Komoran(코모란) : Shineware에서 개발(https://github.com/shin285/KOMORAN)
- Mecab(메카브) : 일본어용 형태소 분석기를 한국어를 사용할 수 있도록 수정(https://bitbucket.org/eunjeon/mecab-ko)
- OpenKoreanText(Okt): 오픈 소스 한국어 분석기, 과거 트위터(Twitter) 형태소 분석기(https://github.com/open-korean-text/open-korean-text)

### Installation
```
# KoNLPy 라이브러리 설치
!pip install konlpy
```

```
# Window 환경은 아래 스크립트로 Mecab 설치
!curl -s https://raw.githubusercontent.com/teddylee777/machine-learning/master/99-Misc/01-Colab/mecab-colab.sh | bash
```

### Usage
```
from konlpy.tag import Kkma, Komoran, Okt, Hannanum, Mecab

okt = Okt()
kkm = Kkma()
kom = Komoran()
han = Hannanum()
mecab = Mecab()
```

## 2. Morpheme Analysis

### 형태소(Morpheme)
- 형태소는 '뜻을 가진 가장 작은 말의 단위'
- '책가방' -> '책', '가방'
- 명사, 대명사, 수사, 조사, 동사, 형용사, 관형사, 부사, 감탄사

### Dataset
- 네이버 영화 리뷰 데이터(ratings_test.txt)
- Naver sentiment movie corpus v1.0
- 출처 : https://github.com/e9t/nsmc

![image](https://user-images.githubusercontent.com/87981867/189907072-22d89689-7f26-441f-bb9c-2ff16d68a839.png)

### Example
```
print(okt.pos(sentence))

>>[('걸작', 'Noun'), ('은', 'Josa'), ('몇', 'Noun'), ('안되고', 'Adjective'), ('졸작', 'Noun'), ('들', 'Suffix'), ('만', 'Josa'), ('넘쳐', 'Adjective'), ('난다', 'Verb'), ('.', 'Punctuation')]
```

## 3. Evaluation

리뷰 데이터 1000개에 대해서 각 형태소 분석기별 형태소 분석 소요 시간 측정

```
100%|██████████| 1000/1000 [00:15<00:00, 63.24it/s]
100%|██████████| 1000/1000 [00:32<00:00, 31.04it/s]
100%|██████████| 1000/1000 [00:01<00:00, 533.54it/s]
100%|██████████| 1000/1000 [00:05<00:00, 167.06it/s]
100%|██████████| 1000/1000 [00:00<00:00, 5247.95it/s
```
![image](https://user-images.githubusercontent.com/87981867/189909140-2b2943fb-14a8-45da-b45b-c40e5b4f817b.png)
