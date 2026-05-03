from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-3-flash-preview')

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", result.content)

print(chat_history)