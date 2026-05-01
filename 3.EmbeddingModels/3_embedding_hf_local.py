from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Lahore is the capital of punjab"

documents = [
    "Lahore is the capital of punjab",
    "Islamabad is the capital of Pakistan"
]

vector = embedding.embed_documents(documents)

print(str(vector))