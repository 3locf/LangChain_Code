# Create a LangSmith API in Settings > API Keys
# Make sure API key env var is set:
# import os; os.environ["LANGSMITH_API_KEY"] = "<your-api-key>"
from langchain_openai import ChatOpenAI
from langsmith import Client

client = Client()
prompt = client.pull_prompt("hardkothari/prompt-maker")

model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

chain = prompt | model

task = input("\n请输入你的任务：")
lazy_prompt = input("\n请输入你的提示词：")

chain.invoke({"task": task, "lazy_prompt": lazy_prompt}).pretty_print()