# ElectraSpacer

## 1. Data Architecture

### (1) Dtata Format

* ElectraSpacer 모델을 거치기 위한 데이터 포맷은 csv 파일 형식
* 파일을 DataFrame으로 읽고, DataFrame의 feature는 'wrong_sentence'와 'correct_sentence'를 입력 값으로 받음
* correct_sentence는 올바른 띄어쓰기가 된 문장이고 wrong_sentence는 띄어쓰기 공백을 모두 제거한 문장

<pre>
# example
wrong_sentence = '나는걸어가고있는중입니다.나는밥을먹고있는중입니다.'
correct_sentence = '나는 걸어가고 있는 중입니다. 나는 밥을 먹고 있는 중입니다.'
</pre>

### (2) Dataset
![image](https://user-images.githubusercontent.com/87981867/190845165-51a092e7-7df7-454d-8256-13be4715339b.png)

- train.csv : 15,876
- dev.csv : 1,060
- test.csv : 1,060

## 2. Model Architecture

### (1) Preprocessing

#### 1) Tokenizer
* 보통 Tokenizing은 WordPiece(단어) 단위로 토큰화
* ElectraSpacer는 아래와 같이 KoCharElectraTokenizer를 사용하여 character(음절) 단위로 토큰화
* 음절 단위로 Tokenizing 할 경우 띄어쓰기의 위치를 더 정확히 판단

<pre>
from tokenization_kocharelectra import KoCharElectraTokenizer
tokenizer = KoCharElectraTokenizer.from_pretrained("monologg/kocharelectra-base-discriminator")
tokenizer.tokenize("나는 걸어가고 있는 중입니다.")

['나', '는', ' ', '걸', '어', '가', '고', ' ', '있', '는', ' ', '중', '입', '니', '다', '.']
</pre>

#### 2) [CLS]&[SEP] Token 추가
<pre>
tokens :  [CLS] 나 는   걸 어 가 고   있 는   중 입 니 다 . [SEP] 나 는   밥 을   먹 고   있 는   중 입 니 다 . [SEP]
</pre>

#### 3) Token to Index
<pre>
input_ids: 2 40 8 5 374 38 14 13 5 36 8 5 75 142 57 7 10 3 40 8 5 733 11 5 445 13 5 36 8 5 75 142 57 7 10 3 0 0 0 0
token_type_ids: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
attention_mask: 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
</pre>

### (2) Model : ELECTRA

<pre>
[Last layer hidden state]
Size: torch.Size([1, 40, 768])
Tensor: tensor([[[ 0.1453, -0.0629,  0.2065,  ...,  0.5304, -0.4602,  0.6803],
         [ 0.8824, -0.3448, -0.3342,  ...,  0.4652, -0.2378,  0.2560],
         [ 0.3114, -0.3019, -0.1159,  ...,  0.4712, -0.6678,  0.3425],
         ...,
         [-0.0830, -0.2008,  0.2107,  ..., -0.2890, -0.0297,  0.5241],
         [ 0.0587, -0.2498,  0.4193,  ..., -0.2537,  0.1526,  0.5394],
         [ 0.1337, -0.2736,  0.6251,  ..., -0.1580,  0.2323,  0.5248]]]) 
</pre>

* Token to Index 한 결과 값들을 ELECTRA 모델을 거치기 전에 Embedding layer를 거침
* outputs.last_hidden_state 찍어보면 위와 같은 결과가 나옴
* torch.Size([1, 40, 768]) -> [1문장, 문장의 길이, 차원]
* 문장 한 개에 속한 각각의 토큰(최대 길이 10)을 768 차원의 벡터로 변환했다는 의미

### (3) BiLSTM-CRF

* LSTM 모델 input 값으로 last_hidden_state을 받아 새로운 Embedding Vector를 출력
* 이 과정에서 Overfitting 방지를 위해 dropout을 해줌
* 최종적으로 문장의 인덱스가 0이면 'B', 나머지 인덱스 값은 'I'로 태그

<pre>
sentence : 나는 걸어가고 있는 중입니다. 나는 밥을 먹고 있는 중입니다.
BI tag : B I B I I I B I B I I I I B I B I B I B I B I I I I
</pre>

## 3. Train Architecture

### (1) Train Model

#### 1) Model Config
<pre>
tokenizer_name: "monologg/kocharelectra-small-discriminator"
model_name: 'monologg/kocharelectra-small-discriminator'
train_data_path: '../data/train.csv'
val_data_path: '../data/dev.csv'
test_data_path: '../data/test.csv'
model_path: './models'

# training arguments
output_dir: './results'
max_len: 256
epochs: 5
steps: 100
batch_size: 32
</pre>

#### 2) Optimizer
<pre>
# Optimizer : Adam
# Learning Rate : 0.00001
optimizer = torch.optim.Adam(params=model.parameters(), lr=1e-05)
</pre>

### (2) Metrics

#### 1) Calculate
![image](https://user-images.githubusercontent.com/87981867/190845241-ca8a6b9e-506b-46d1-b29d-f222037d2356.png)

#### 2) Example
![image](https://user-images.githubusercontent.com/87981867/190845290-a0097b9f-bae7-4b34-a609-cfa3e1a66bfc.png)
![image](https://user-images.githubusercontent.com/87981867/190845291-f0021380-c747-4813-89ce-0e760d2471e7.png)
![image](https://user-images.githubusercontent.com/87981867/190845292-cb45996e-0167-4bd6-9b3f-64bab5ecfee2.png)

</pre>

## 4. Output

### (1) Inference

<pre>
{
    "0": [
        "나는철수에게공을던져다주었다.",
        "나는 철수에게 공을 던져다 주었다.",
        " 나는 철수에게 공을 던져다 주었다."
    ],
    "1": [
        "먹은것을다소화시켜야한다.",
        "먹은 것을 다 소화시켜야 한다.",
        " 먹은 것을 다소화시켜야 한다."
    ],
    "2": [
        "그가노래를부르고는내가피아노를쳤다.",
        "그가 노래를 부르고는 내가 피아노를 쳤다.",
        " 그가 노래를 부르고는 내가 피아노를 쳤다."
    ],
    "3": [
        "철수가영수의손을잡아서눈물을글썽거렸다.",
        "철수가 영수의 손을 잡아서 눈물을 글썽거렸다.",
        " 철수가 영수의 손을 잡아서 눈물을 글썽거렸다."
    ],

...

    "1057": [
        "그는나를바보여긴다.",
        "그는 나를 바보 여긴다.",
        " 그는 나를 바보여긴다."
    ],
    "1058": [
        "수호는모든일에전혀무감각하다.",
        "수호는 모든 일에 전혀 무감각하다.",
        " 수호는 모든 일에 전혀 무감각하다."
    ],
    "1059": [
        "나는할아버지가제일무서우시다.",
        "나는 할아버지가 제일 무서우시다.",
        " 나는 할아버지가 제일 무서우시다."
    ]
}
</pre>

* inference.py 실행하면 results 경로에 prediction.json 파일 생성 
* 추론 결과는 위에서 wrong_sentence, correct_sentence, predict_sentence 순으로 출력

### (2) Predict

#### 1) Method #1
![image](https://user-images.githubusercontent.com/87981867/190845398-fa8e88a2-5fc7-463c-a03b-b3297d0564bc.png)

* predict.py를 실행하면 results 경로에 prediction.csv 파일 생성
* wrong_sentence를 input 값으로 받아서 곧바로 띄어쓰기를 예측해줌

#### 2) Method #2
<pre>
electraspacer = ElectraSpacer()
</pre>
![image](https://user-images.githubusercontent.com/87981867/190845403-c89cc70f-2a97-4f3e-bff3-052b872e5735.png)

* predict.py를 실행하면 results 경로에 prediction.json 파일 생성
* 클래스를 직접 불러와 문장을 입력하여 곧 바로 띄어쓰기 예측
