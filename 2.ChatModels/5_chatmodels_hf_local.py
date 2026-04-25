from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = '/Users/hamzaanjum/.cache/huggingface'

llm = HuggingFacePipeline.from_model_id(
    model_id = 'Qwen/Qwen2.5-Coder-3B-Instruct',
    task = 'text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a Python function to reverse a string.")

print(result.content)
