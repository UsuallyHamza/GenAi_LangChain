from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following question \n {question} from the following text -\n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://en.wikipedia.org/wiki/Apple_M2'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model2 | parser

print(chain.invoke({'question':'What is the product that we are talking about' , 'text': docs[0].page_content}))