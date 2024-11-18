# https://python.langchain.com/docs/concepts/structured_outputs/
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class AddNumbers(BaseModel):
    """Use this tool to add two numbers together."""
    num1: float = Field(description="The first number")
    num2: float = Field(description="The second number")

class GetTime(BaseModel):
    """Use this tool to get the current time."""
    pass

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# Bind responseformatter schema as a tool to the model
model_with_tools = model.bind_tools([AddNumbers, GetTime])
# Invoke the model
ai_msg = model_with_tools.invoke("What is the time?")

print(ai_msg.model_dump()['tool_calls'])