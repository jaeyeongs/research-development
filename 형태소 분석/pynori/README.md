# Pynori를 활용한 형태소 분석

## Pynori

ElasticSearch에 내장된 형태소 분석기 **Nori**의 파이썬 버전 & 순수 파이썬 스크립트로 작성된 라이브러리

Pynori에 대한 자세한 내용은 [Github](https://github.com/gritmind/python-nori, "Github") 참고

## Install

```
$ pip install pynori
```

## Usage

아래는 KoreanAnalyzer 기본값으로 설정하여 형태소 분석

```
from pynori.korean_analyzer import KoreanAnalyzer
nori = KoreanAnalyzer(
           decompound_mode='DISCARD', # DISCARD or MIXED or NONE
           infl_decompound_mode='DISCARD', # DISCARD or MIXED or NONE
           discard_punctuation=True,
           output_unknown_unigrams=False,
           pos_filter=False, stop_tags=['JKS', 'JKB', 'VV', 'EF'],
           synonym_filter=False, mode_synonym='NORM', # NORM or EXTENSION
       ) 

print(nori.do_analysis("아빠가 방에 들어가신다."))
```

```
{'termAtt': ['아빠', '가', '방', '에', '들어가', '시', 'ᆫ다'],
 'offsetAtt': [(0, 2), (2, 3), (4, 5), (5, 6), (7, 10), (10, 12), (10, 12)],
 'posLengthAtt': [1, 1, 1, 1, 1, 1, 1],
 'posTypeAtt': ['MORP', 'MORP', 'MORP', 'MORP', 'MORP', 'MORP', 'MORP'],
 'posTagAtt': ['NNG', 'JKS', 'NNG', 'JKB', 'VV', 'EP', 'EF'],
 'dictTypeAtt': ['KN', 'KN', 'KN', 'KN', 'KN', 'KN', 'KN']}
```

KoreanAnalyzer의 옵션을 동적으로 제어 가능

```
print(nori.do_analysis("가벼운 냉장고")['termAtt'])
# ['가볍', 'ᆫ', '냉장', '고']

## 토크나이저 옵션 세팅
nori.set_option_tokenizer(decompound_mode='MIXED', infl_decompound_mode='MIXED')
print(nori.do_analysis("가벼운 냉장고")['termAtt'])
# ['가벼운', '가볍', 'ᆫ', '냉장고', '냉장', '고']

## POS 필터 옵션 세팅
nori.set_option_filter(pos_filter=True, stop_tags=['ETM', 'VA'])
print(nori.do_analysis("가벼운 냉장고")['termAtt'])
# ['냉장고', '냉장', '고']

## 동의어 필터 옵션 세팅
nori.set_option_filter(synonym_filter=True, mode_synonym='NORM')
print(nori.do_analysis("NLP 개발자")['termAtt'])
# ['자연어처리', '자연어', '처리', '개발자', '개발', '자']

nori.set_option_tokenizer(decompound_mode='DISCARD', infl_decompound_mode='DISCARD') # DISCARD 로 변경.
nori.set_option_filter(mode_synonym='EXTENSION')
print(nori.do_analysis("AI 개발자")['termAtt'])
# ['인공', '지능', 'ai', 'aritificial', 'intelligence', '개발', '자', 'developer']
```
