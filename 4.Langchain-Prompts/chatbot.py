from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

# how to send list of messages (but static)
#useful for the chatbots keeping the history of the chatm

model = ChatGoogleGenerativeAI(model= 'gemini-3-flash-preview')

chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input)) # type: ignore
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content)) # type: ignore
    print("AI: ", result.content)

print(chat_history)