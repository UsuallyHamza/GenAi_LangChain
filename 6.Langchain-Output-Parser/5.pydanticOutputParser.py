from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
# here we are learning pydantic output parser
# diff btw pydantic and structured parser is simply that in structured parser we cant do data validation but we can do in pydantic ouput parser
# downside = unknown

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-26B-A4B-it",
    task= "text-generation"

)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str =Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fiactional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place':'pakistani'})

print(result)