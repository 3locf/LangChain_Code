""""输出解析器"""
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# 1. 创建模型
model = ChatOpenAI(model="gpt-4o-mini",base_url="https://api.laozhang.ai/v1")

# 2. 创建输出解析器
output_parser = StrOutputParser()

# 3. 定义链
chain = model | output_parser

# 4. 执行链
result = chain.invoke("你觉得或者的意义是什么？请以JSON格式输出")
print(result)
