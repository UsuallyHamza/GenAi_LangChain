from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

documents = [
    "Lahore is the capital of punjab",
    "Islamabad is the capital of Pakistan"
]

result = embedding.embed_documents(documents)

print(str(result))