from langchain_google_genai import ChatGoogleGenerativeAI #always remember ChatGoogleGenerativeAI are chat models while 
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview') 

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

#the difference here is simple, we made a class which define the schema of the LLM output and instead of calling the invoke() method on model, we called it on structured_model
structured_model = model.with_structured_output(Review) # type: ignore

result = structured_model.invoke("""The hardware is great, but software is bloated. There are too many pre-installed apps that I can't remove. Also the UI looks outdated compared to other brands. Hoping for a software update to fix.""")

print(result)