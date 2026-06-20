from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
#directory loader is used when we want to load a bundle of .txt or .pdf or any other file types
#it works with every type pf file .txt, .pdf, .csv etc

loader = DirectoryLoader(
    path='10.Document-Loaders/Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))