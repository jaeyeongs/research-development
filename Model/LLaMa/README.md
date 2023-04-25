# LLaMA

## Model Architecture

**(1)Pre-normalization (from GPT-3)**

- 학습 안정성을 개선하기 위해 각 transformer sub-layer의 입력을 normalization함
- RMSNorm Normalizing 함수 사용

**(2)SwiGLU activation function (from PaLM)**

- 성능 개선을 위해 ReLU를 SwiGLU로 교체함

**(3)Rotary Embeddings(from GPTNeo)**

- 절대적인 positional embeddings을 제거하고 RoPE(Rotary Postional Embedding)을 사용함

## Optimization Hyper-Parameters

Meta는 LLaMA 학습에 AdamW optimizer를 사용

**AdamW optimizer**

- hyper-parameters: beta1=0.9, beta2=0.95
- weight decay = 0.1, gradient clipping = 1.0
- 2000 warmup steps

![https://miro.medium.com/v2/resize:fit:875/1*YfxWGIvYlrXS-eBHEkcXvw.png](https://miro.medium.com/v2/resize:fit:875/1*YfxWGIvYlrXS-eBHEkcXvw.png)

## 데이터셋

- Meta AI는 LLaMA 학습을 위해 다른 LLMs의 학습 데이터 소스를 재사용(총 4.75 TB)
- Wikipedia의 경우, 2022년 6월~8월까지의 20개국(bg, ca, cs, da, de, en, es, fr, hr, hu, it, nl, pl, pt, ro, ru, sl, sr, sv, uk) 데이터로 한국어는 제외

![https://miro.medium.com/v2/resize:fit:480/1*oGc-8V9H7TkMJSA5jNe8bw.png](https://miro.medium.com/v2/resize:fit:480/1*oGc-8V9H7TkMJSA5jNe8bw.png)

- BPE(Byte Pair Encoding) 알고리즘으로 데이터를 토큰화하였으며, 토큰화 후에 전체 학습 데이터셋은 1.4 T tokens을 포함
- 각 토큰은 거의 한 번만 학습되었으며, Wikipedia와 Books 데이터셋은 2 epoch 학습

## 예제

llama origin(LLaMA) : [https://github.com/facebookresearch/l...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazJJUjVFSU5lcW5aMk9tc0NabU1SZW1rOWRKd3xBQ3Jtc0ttMjNJSXBUSUR6cHpLLUgtVVNtOE9JZUJIdmUzT19FVVp3ZVczM2w1QnVJcGpmY1FuTERZaVoybGZTWUVPUUtLR2JxSDhBOFRwaFY4aXV1b3Vub0Iwci1VWVdiVEhZYUZ1ZDA1bHVVcnZJYXhOUVdESQ&q=https%3A%2F%2Fgithub.com%2Ffacebookresearch%2Fllama&v=jvYpv9VJBOA)

llama-hf(LLaMA-Small) : [https://github.com/ypeleg/llama](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUsxUTJSWE1YQ1RwTFczejNzVlJvOUxwYzZZUXxBQ3Jtc0ttd19qSmY4WklwOFNxNkQ5Rk5sUF9kSi1wSHpqR2wtRlIzaGVxQmtwd2NSRGdYS3Jqbm0zbVM4NFlwM1RzWUhkRDZES0VVc19mN2hMUEdacjlNUW0yVlBnMnlua2VyU09mSTZ4dzk5X3FZY1VORUh2bw&q=https%3A%2F%2Fgithub.com%2Fypeleg%2Fllama&v=jvYpv9VJBOA)

**LLaMA-Small**
```python
# inference_example.py
MODEL = 'decapoda-research/llama-7b-hf'

tokenizer = llama.LLaMATokenizer.from_pretrained(MODEL)
model = llama.LLaMAForCausalLM.from_pretrained(MODEL, low_cpu_mem_usage = True)
model.to('cuda')

batch = tokenizer("Paris is the capital of France", return_tensors = "pt")
print(tokenizer.decode(model.generate(batch["input_ids"].cuda(), max_length=100)[0]))
```
```
Paris is the capital of France and the most populous city in the country. It is situated on the river Seine, in northern France, at the heart of the Île-de-France region. The city of Paris, within its administrative limits (the 20 arrondissements), has approximately 2,2 million inhabitants. The Paris metropolitan area has more than 12 million inhabitants, and is one of the most populated metropolitan areas in Europe.
Paris
```

```python
# test.py
model_name = "decapoda-research/llama-13b-hf"
tokenizer = LLaMATokenizer.from_pretrained(model_name)
model = LLaMAForCausalLM.from_pretrained(model_name, low_cpu_mem_usage=True)

prompt = "표정이 안 좋아 보이는데 나랑 얘기좀 할까?"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(inputs.input_ids, max_length=100)
a = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print(a)
```
```
표정이 안 좋아 보이는데 나랑 얘기좀 할까?
저는 저는 저는 저는 저는 저는 저는 저는 저는 저는 저는
```
