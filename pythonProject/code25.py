from typing import Annotated, Optional

from langchain_core.messages import HumanMessage
from langchain_core.tools import StructuredTool
from langchain_core.utils.function_calling import tool_example_to_messages
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")


# def add(a: int, b: int) -> int:
#     """返回两个整数的和"""
#     return a + b
#
#
# class AddInput(BaseModel):
#     a: Annotated[int, ..., "第一个加数"]
#     b: Annotated[int, ..., "第二个加数"]
#
#
# tool = StructuredTool.from_function(
#     func=add,
#     args_schema=AddInput,
#     description="两数相加",
#     name="add"
# )
#
# tools = [tool]
# model_with_tool = model.bind_tools(tools=tools)
#
# message = [HumanMessage("5加8等于多少？")]
# print(model_with_tool.invoke(message))

class ExtractPersonInfo(BaseModel):
    """提取关于人的信息"""
    name: str = Field(description="这个人的名字")
    age: Optional[str] = Field(default=None, description="这个人的年龄")


message = tool_example_to_messages(
    input="我叫张三，已经生活50年了，时间过的真快呀",
    tool_calls=[ExtractPersonInfo(name="张三", age="50")], #  这里直接
)

print(message)
# [HumanMessage(content='我叫张三，已经生活50年了，时间过的真快呀', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '6996c7b8-92d4-4bfa-bf21-ec4165887a6c', 'type': 'function', 'function': {'name': 'ExtractPersonInfo', 'arguments': '{"name":"张三","age":"50"}'}}]}, response_metadata={}, tool_calls=[{'name': 'ExtractPersonInfo', 'args': {'name': '张三', 'age': '50'}, 'id': '6996c7b8-92d4-4bfa-bf21-ec4165887a6c', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='6996c7b8-92d4-4bfa-bf21-ec4165887a6c')]
