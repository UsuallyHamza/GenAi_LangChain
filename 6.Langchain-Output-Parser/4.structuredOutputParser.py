from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
# here we are learning structured output parser
# diff btw this one and json output parser is simply that in json parser we cant specify schema of json but we can in structured ouput parser
# downside = no data validation, thats why we use pydantic output parser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-4-26B-A4B-it",
    task= "text-generation"

)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result= chain.invoke({'topic':'black hole'})

print(result)