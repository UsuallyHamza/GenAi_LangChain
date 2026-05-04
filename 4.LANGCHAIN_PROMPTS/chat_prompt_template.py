from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# ChatPromptTemplate is for multi turn conversation messages
#list of messages dynamic (dynamic set of messages)
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket', 'topic': 'Dosra'})

print(prompt)