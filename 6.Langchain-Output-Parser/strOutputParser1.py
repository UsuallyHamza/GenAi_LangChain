from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# here we are actually using output parsers

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
    task= "text-generation"

)

model = ChatHuggingFace(llm=llm)

#1st promy -> dtailed report
template1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd prompt -> summary
template2= PromptTemplate(
    template='Write a 5 line summary on the following text./n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({"topic": "balck hole"})

result = model.invoke(prompt1)

prompt2= template2.invoke({"text": result.content})

result1 = model.invoke(prompt2)

print(result1.content)