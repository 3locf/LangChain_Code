from typing import Optional, Union

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

base_url = "https://api.laozhang.ai/v1"
# 定义模型
model = ChatOpenAI(model="gpt-4o-mini", base_url=base_url)


# 方式一：使用pydantic定义结构化输出
class Author(BaseModel):
    """作者信息"""
    name: str = Field(..., description="作者名称")
    age: int = Field(..., description="作者年龄")
    books: list[str] = Field(..., description="作者的书籍列表")
    hobbies: Optional[list[str]] = Field(default=None, description="作者的爱好列表")
    quotes: str = Field(..., description="作者的经典语录")
    impact: int = Field(..., description="作者的影响力")


class CommonResponse(BaseModel):
        """平常的普通对话"""
        response: str = Field(..., description="模型的普通对话回复")


class FinalResponse(BaseModel):
    """最终的结构化输出"""
    final_response: Union[CommonResponse, Author]


model_with_output = model.with_structured_output(FinalResponse)
print(model_with_output.invoke("请你给我介绍一位作者"))
print(model_with_output.invoke("你是谁？"))
