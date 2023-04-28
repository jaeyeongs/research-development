import llama

MODEL = 'decapoda-research/llama-7b-hf'
# MODEL = 'decapoda-research/llama-13b-hf'
# MODEL = 'decapoda-research/llama-30b-hf'
# MODEL = 'decapoda-research/llama-65b-hf'

tokenizer = llama.LLaMATokenizer.from_pretrained(MODEL)
model = llama.LLaMAForCausalLM.from_pretrained(MODEL, low_cpu_mem_usage = True)
model.to('cuda')

batch = tokenizer("Paris is the capital of France", return_tensors = "pt")
print(tokenizer.decode(model.generate(batch["input_ids"].cuda(), max_length=100)[0]))
