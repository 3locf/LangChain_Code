from typing import Optional

from langchain_core.output_parsers import JsonOutputParser
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

class Data(BaseModel):
    """提取数据"""
    dogs: list[Dog] = Field(..., description="狗的信息列表")


parser = JsonOutputParser(pydantic_object=Data)

prompt = PromptTemplate(
    template="请提取用户输入中关于狗的信息，并以JSON格式输出.\n{format_instructions}\n{query}",
    input_variables=["query"],  # 输入变量
    partial_variables={"format_instructions": parser.get_format_instructions()},  # 部分变量
)

# print(prompt.invoke({
#     "query": "昨天在公园看到两个人遛狗，一只白色的萨摩耶，叫雪球，主人说它刚满两岁，毛特别厚，跑起来像个小棉花球。还有一只黑色的小狗，个子小小的，叫煤球，没看清是什么品种，好像是中华田园犬吧，年龄也不知道，看着挺小的，可能才几个月大，一直跟在雪球后面跑。"}))

chain = prompt | model | parser
result = chain.invoke({"query": "昨天在公园看到两个人遛狗，一只白色的萨摩耶，叫雪球，主人说它刚满两岁，毛特别厚，跑起来像个小棉花球。还有一只黑色的小狗，个子小小的，叫煤球，没看清是什么品种，好像是中华田园犬吧，年龄也不知道，看着挺小的，可能才几个月大，一直跟在雪球后面跑。"})
print(result)
# {'dogs': [{'name': '雪球', 'age': 2, 'color': '白色', 'breed': '萨摩耶'},
#           {'name': '煤球', 'age': None, 'color': '黑色', 'breed': '中华田园犬'}]}



