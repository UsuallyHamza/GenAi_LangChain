from langchain_community.document_loaders import PyPDFLoader
#pypdf loader does not work with scanned pdfs 

loader = PyPDFLoader('10.Document-Loaders/dl-curriculum.pdf')

docs = loader.load()

# print(docs)

print(docs[0].page_content)

print(docs[0].metadata)
