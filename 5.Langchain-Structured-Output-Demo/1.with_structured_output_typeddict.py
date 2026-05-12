from langchain_google_genai import ChatGoogleGenerativeAI #always remember ChatGoogleGenerativeAI are chat models while 
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

# typeddit is only for representational puporses it does not provide data validation like pydantic

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview') 

#schema
class Review(TypedDict):

    key_themes : Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Returned sentiment of the review, either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

#the difference here is simple, we made a class which define the schema of the LLM output and instead of calling the invoke() method on model, we called it on structured_model
structured_model = model.with_structured_output(Review) # type: ignore

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors""")

print(result)
print(result[0]['args']['summary'])
print(result[0]['args']['sentiment'])