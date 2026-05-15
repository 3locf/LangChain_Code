from typing import Annotated

from langchain_core.tools import tool
from pydantic import BaseModel, Field


# 方式一
# @tool
# def sub(a: int, b: int) -> int:
#     """两数相减
#
#     Args
#     a: 被减数
#     b: 减数
#     """
#     return a - b
#
#
# print(sub.invoke({"a": 3, "b": 2}))
# print(sub.name)
# print(sub.description)
# print(sub.args)


# 方式二
# class SubInput(BaseModel):
#     """两数相减"""
#     a: int = Field(..., description="被减数")
#     b: int = Field(..., description="减数")
#
#
# @tool(args_schema=SubInput)
# def sub(a: int, b: int) -> int:
#     return a - b
#
#
# print(sub.invoke({"a": 3, "b": 2}))
# print(sub.name)
# print(sub.description)
# print(sub.args)




# 方式三

@tool
def sub(
        a: Annotated[int, ..., "被减数"],
        b: Annotated[int, ..., "减数"]
) -> int:
    """两数相减

    Args:
        a: 被减数,整数
        b: 减数,整数
    Returns:
        两数相减的结果
    """
    return a - b


print(sub.invoke({"a": 3, "b": 2}))
print(sub.name)
print(sub.description)
print(sub.args)