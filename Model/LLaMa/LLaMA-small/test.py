from llama import LLaMATokenizer, LLaMAForCausalLM

model_name = "decapoda-research/llama-13b-hf"
tokenizer = LLaMATokenizer.from_pretrained(model_name)
model = LLaMAForCausalLM.from_pretrained(model_name, low_cpu_mem_usage=True)

prompt = "표정이 안 좋아 보이는데 나랑 얘기좀 할까?"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(inputs.input_ids, max_length=100)
a = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
print(a)
