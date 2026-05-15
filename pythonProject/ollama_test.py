
# 本地部署
from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:1.5b", base_url="http://127.0.0.1:11434")

print(llm.invoke("请问1+1等于几").content)