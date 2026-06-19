from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
#runnable Lambda turns any function into a runnable

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id = "deepseek-ai/DeepSeek-V3.1",
    task= "text-generation"

)

model = ChatGoogleGenerativeAI(model= 'gemini-3-flash-preview')

model2 = ChatHuggingFace(llm=llm1)

prompt =PromptTemplate(
    template='Write a summary for the following poem -\n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('10.Document-Loaders/cricket.txt', encoding='utf-8')

docs = loader.load()

# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))