from typing import Annotated

from langchain_core.messages import HumanMessage
from langchain_core.tools import StructuredTool, tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

base_url = "https://api.laozhang.ai/v1"

# 创建一个 ChatOpenAI 实例
model = ChatOpenAI(base_url=base_url)


# 定义一个工具函数，并使用 @tool 装饰器进行装饰
@tool
def add(
        a: Annotated[int, ..., "第一个加数"],
        b: Annotated[int, ..., "第一个加数"]
) -> int:
    """两数相加"""
    return a + b


# 定义一个普通函数，并使用 StructuredTool.from_function 方法将其转换为工具
class DivideInput(BaseModel):
    a: int = Field(..., description="被除数")
    b: int = Field(..., description="除数")


def divide(a: int, b: int) -> int:
    return  a / b

# 使用 StructuredTool.from_function 方法将普通函数转换为工具
div_tool = StructuredTool.from_function(
    func=divide,
    args_schema=DivideInput,
    description="两数相除",
    name='divide',
)
# 将工具添加到工具列表
tools = [add, div_tool]
tool_with_model = model.bind_tools(tools=tools)


message = [HumanMessage("5加8等于多少？10除以2等于多少？")]

# 调用工具函数获取工具选择结果
ai_msg = tool_with_model.invoke(message)
message.append(ai_msg)

#  根据工具选择结果，调用对应的工具函数，并将结果添加到消息列表中
tool_map = {"add": add, "divide": div_tool}
for tool_call in ai_msg.tool_calls:
    select_tool = tool_map[tool_call["name"].lower()]
    tool_result = select_tool.invoke(tool_call)
    message.append(tool_result)


result = model.invoke(message)
print(result.content)



