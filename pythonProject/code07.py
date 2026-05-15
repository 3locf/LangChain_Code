from typing import Optional

from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field

""" 结构化输出   """

# 定义模型
model = init_chat_model(model="deepseek-chat", model_provider="deepseek", api_key="513a93ff6062c5")


# 方式一：使用pydantic定义结构化输出
class Author(BaseModel):
    """作者信息"""
    name: str = Field(..., description="作者名称")
    age: int = Field(..., description="作者年龄")
    books: list[str] = Field(..., description="作者的书籍列表")
    hobbies: Optional[list[str]] = Field(default=None, description="作者的爱好列表")
    quotes: str = Field(..., description="作者的经典语录")
    impact: int = Field(..., description="作者的影响力")



class ListAuthor(BaseModel):
    """作者列表信息"""
    authors: list[Author] = Field(..., description="作者列表信息")


# 大模型绑定结构化输出
model_with_output = model.with_structured_output(ListAuthor)
print(model_with_output.invoke("请你给我介绍两位知名作家"))   #  模型会根据Author的定义，返回一个结构化的输出，包含name、age、books、hobbies和quotes等字段的信息。



