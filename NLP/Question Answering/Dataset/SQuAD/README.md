# SQuAD

**(1) SQuAD 1.0**

- SQuAD (Stanford Question Answering Dataset) 1.0은 스탠포드 대학교에서 제공하는 질문-답변 데이터셋
- 웹에서 수집된 500개 이상의 Wikipedia 문서에서 100,000개 이상의 질문-답변 쌍

```json
# SQuAD 1.0
{
    "data": [
        {
            "paragraphs": [
                {
                    "context": "Super Bowl 50 was an American football game...",
                    "qas": [
                        {
                            "answers": [
                                {
                                    "answer_start": 177,
                                    "text": "Denver Broncos"
                                }
                            ],
                            "question": "Which NFL team represented the AFC at Super Bowl 50?",
                            "id": "56be4db0acb8001400a502ec"
                        },
                        {
                            "answers": [
                                {
                                    "answer_start": 249,
                                    "text": "Carolina Panthers"
                                }
                            ],
                            "question": "Which NFL team represented the NFC at Super Bowl 50?",
                            "id": "56be4db0acb8001400a502ed"
                        },
                        ...
                    ]
                }
            ],
            "title": "Super_Bowl_50"
        }
    ],
    "version": "1.0"
}
```

**(2) SQuAD 2.0**

- SQuAD 2.0은 SQuAD 1.0과 마찬가지로 질문-답변 데이터셋이며 50,000개 이상의 질문-답변 쌍 추가
- 문서에서 답변이 없는 질문도 포함
- 하나의 질문에 대해 여러 개의 정답이 가능
- 질문에 대한 답변을 찾을 수 없는 경우 "is_impossible" 필드를 이용하여 이를 표시

```json
# SQuAD 2.0
{
  "version": "v2.0",
  "data": [
    {
      "title": "Normans",
      "paragraphs": [
        {
          "qas": [
            {
              "question": "In what country is Normandy located?",
              "id": "56ddde6b9a695914005b9628",
              "answers": [
                {
                  "text": "France",
                  "answer_start": 159
                },
                {
                  "text": "France",
                  "answer_start": 159
                },
                {
                  "text": "France",
                  "answer_start": 159
                },
                {
                  "text": "France",
                  "answer_start": 159
                }
              ],
              "is_impossible": false
            },
            {
              "question": "When were the Normans in Normandy?",
              "id": "56ddde6b9a695914005b9629",
              "answers": [
                {
                  "text": "10th and 11th centuries",
                  "answer_start": 94
                },
                {
                  "text": "in the 10th and 11th centuries",
                  "answer_start": 87
                },
                {
                  "text": "10th and 11th centuries",
                  "answer_start": 94
                },
                {
                  "text": "10th and 11th centuries",
                  "answer_start": 94
                }
              ],
              "is_impossible": false
            },
            {
              "question": "From which countries did the Norse originate?",
              "id": "56ddde6b9a695914005b962a",
              "answers": [
                {
                  "text": "Denmark, Iceland and Norway",
                  "answer_start": 256
                },
                {
                  "text": "Denmark, Iceland and Norway",
                  "answer_start": 256
                },
                {
                  "text": "Denmark, Iceland and Norway",
                  "answer_start": 256
                },
                {
                  "text": "Denmark, Iceland and Norway",
                  "answer_start": 256
                }
              ],
              "is_impossible": false
            },
            {
              "question": "Who was the Norse leader?",
              "id": "56ddde6b9a695914005b962b",
              "answers": [
                {
                  "text": "Rollo",
                  "answer_start": 308
                },
                {
                  "text": "Rollo",
                  "answer_start": 308
                },
                {
                  "text": "Rollo",
                  "answer_start": 308
                },
                {
                  "text": "Rollo",
                  "answer_start": 308
                }
              ],
              "is_impossible": false
            },
            {
              "question": "What century did the Normans first gain their separate identity?",
              "id": "56ddde6b9a695914005b962c",
              "answers": [
                {
                  "text": "10th century",
                  "answer_start": 671
                },
                {
                  "text": "the first half of the 10th century",
                  "answer_start": 649
                },
                {
                  "text": "10th",
                  "answer_start": 671
                },
                {
                  "text": "10th",
                  "answer_start": 671
                }
              ],
              "is_impossible": false
            },
            {
              "plausible_answers": [
                {
                  "text": "Normans",
                  "answer_start": 4
                }
              ],
              "question": "Who gave their name to Normandy in the 1000's and 1100's",
              "id": "5ad39d53604f3c001a3fe8d1",
              "answers": [],
              "is_impossible": true
            },
            {
              "plausible_answers": [
                {
                  "text": "Normandy",
                  "answer_start": 137
                }
              ],
              "question": "What is France a region of?",
              "id": "5ad39d53604f3c001a3fe8d2",
              "answers": [],
              "is_impossible": true
            },
            {
              "plausible_answers": [
                {
                  "text": "Rollo",
                  "answer_start": 308
                }
              ],
              "question": "Who did King Charles III swear fealty to?",
              "id": "5ad39d53604f3c001a3fe8d3",
              "answers": [],
              "is_impossible": true
            },
            {
              "plausible_answers": [
                {
                  "text": "10th century",
                  "answer_start": 671
                }
              ],
              "question": "When did the Frankish identity emerge?",
              "id": "5ad39d53604f3c001a3fe8d4",
              "answers": [],
              "is_impossible": true
            }
          ],
          "context": "The Normans (Norman: Nourmands; French: Normands; Latin: Normanni) were the people who in the 10th and 11th centuries gave their name to Normandy, a region in France. They were descended from Norse (\"Norman\" comes from \"Norseman\") raiders and pirates from Denmark, Iceland and Norway who, under their leader Rollo, agreed to swear fealty to King Charles III of West Francia. Through generations of assimilation and mixing with the native Frankish and Roman-Gaulish populations, their descendants would gradually merge with the Carolingian-based cultures of West Francia. The distinct cultural and ethnic identity of the Normans emerged initially in the first half of the 10th century, and it continued to evolve over the succeeding centuries."
        },
        
                },
```
