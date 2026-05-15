from typing import Annotated

from langchain_core.tools import tool
from pydantic import BaseModel, Field


# @tool  方式一
# def add(a: int, b: int) -> int:
#     """ 两数相加
#     Args:
#         a: 第一个整数
#         b: 第二个整数
#     """
#     return a + b



#  方式二
# class AddInput(BaseModel):
#     """两数相加"""
#
#     a: int = Field(..., description="第一个整数")
#     b: int = Field(..., description="第二个参数")
#
#
# @tool(args_schema=AddInput)
# def add(a: int, b: int) -> int:
#     return a + b



@tool
def add(
        a : Annotated[int, ..., "第一个参数"],
        b : Annotated[int, ..., "第二个参数"]
) -> int:
    """ 两数相加
    Args:
        a: 第一个整数
        b: 第二个整数
    """
    return a + b


print(add.invoke({"a": 2, "b": 3}))
print(add.name)
print(add.description)
print(add.args)

