from typing import Optional

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


""""解析结构化对象输出"""
model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

class Dog(BaseModel):
    """提取狗的信息"""
    name: str = Field(..., description="狗的名字")
    age: Optional[int] = Field(None, description="狗的年龄")
    color: Optional[str] = Field(None, description="狗的颜色")
    breed: Optional[str] = Field(None, description="狗的品种")


parser = PydanticOutputParser(pydantic_object=Dog)

# 要想让 PydanticOutputParser 工作，你必须把“请输出什么样的 JSON”这个指令（Format Instructions）拼接到提示词（Prompt）里告诉大模型。
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],  # 输入变量
    partial_variables={"format_instructions": parser.get_format_instructions()}, # 部分变量
)

chain = prompt | model | parser

result = chain.invoke({"query": "上周六去朋友家做客，她家养了只特别可爱的小狗，叫什么来着？哦对，叫布丁。毛是那种浅棕色的，软乎乎的，摸起来像棉花糖。好像是泰迪和比熊的串串吧，具体多大我也没问，看着也就一岁多两岁的样子，特别活泼，一直围着我转要吃的。"})
print(result)