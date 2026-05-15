from typing import Tuple, List

from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


# def sub(a: int, b: int) -> int:
#     """两数相减"""
#     return a - b
#
#
# sub_tool = StructuredTool.from_function(func=sub)  # 把普通函数 → 变成 AI 工具
#
#
# print(sub_tool.invoke({"a": 5, "b": 3}))  #调用工具
# print(sub_tool.name)
# print(sub_tool.description)
# print(sub_tool.args)




#  方式二
# class SubInput(BaseModel):
#       a: int = Field(..., description="第一个被减数")
#       b: int = Field(..., description="第二个减数")
#
#
# def sub(a: int, b: int) -> int:
#     return a - b
#
# sub_tool = StructuredTool.from_function(
#     func=sub,
#     description="两数相减",
#     name="SUB",
#     args_schema=SubInput
# )





#  方式三
class SubInput(BaseModel):
    a: int = Field(..., description="第一个被减数")
    b: int = Field(..., description="第二个减数")


def sub(a: int, b: int) -> Tuple[str, List[int]]:
    nums = [a, b]
    content = f"{nums}两数相减的结果是{a - b}"
    return content, nums


sub_tool = StructuredTool.from_function(
    func=sub,
    description="两数相减",
    name="SUB",
    args_schema=SubInput,
    response_format="content_and_artifact"
)

# print(sub_tool.invoke({"a": 9, "b": 6}))
# print(sub_tool.name)
# print(sub_tool.args)


# 模拟大模型调用姿势
print(sub_tool.invoke(
    {
        "name": "SUB",
        "args": {"a": 19, "b": 3},
        "type": "tool_call",  # 必填
        "id": "12345",  # 必填，用来将工具调用的请求和结果关联起来
    }
))