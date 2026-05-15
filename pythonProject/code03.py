from typing import Annotated

from langchain_core.tools import StructuredTool, tool
from pydantic import Field, BaseModel


# 方法一
# def add(a: int, b: int) -> int:
#     """两数相加"""
#     return a + b
# add_tool = StructuredTool.from_function(func=add)
# print(add_tool.invoke({"a": 1, "b": 2}))

# # 方法二
# class AddInput(BaseModel):
#     a: int = Field(description="第一个参数")
#     b: int = Field(description="第二个参数")
#
#
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# add_tool = StructuredTool.from_function(
#     func=add,
#     name="ADD",    # 工具名
#     description="两数相加", #工具描述
#     args_schema=AddInput, # 工具参数
# )
#
# print(add_tool.invoke({"a": 1, "b": 2}))
# print(add_tool.name)
# print(add_tool.description)
# print(add_tool.args)



# @tool
# def add(
#         a: Annotated[int, ..., "第一个加数"],
#         b: Annotated[int, ..., "第二个加数"],
# ) -> int:
#     """两数相加"""
#     return a + b
#
#
# print(add.invoke({"a": 1, "b": 2}))




def multiple(a: int, b: int) -> int:
    return a * b


class MultipleInput(BaseModel):
    a: int = Field(..., description="第一个乘数")
    b: int = Field(..., description="第二个乘数")


mul_tool = StructuredTool.from_function(
    func=multiple,
    args_schema=MultipleInput,   #  工具参数
    description="两数相乘",  # 工具描述
    name="MUL",
)


print(mul_tool.invoke({"a": 1, "b": 2}))
print(mul_tool.name)
