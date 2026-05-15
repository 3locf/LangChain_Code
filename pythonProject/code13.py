from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage
# 多轮对话 --- 将多轮对话的消息列表直接传入模型，模型会根据上下文进行理解和回复
model = init_chat_model(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1",model_provider="openai")

# print(model.invoke("你好,i miss you!").text())
# model.invoke("hello,my name is xiaoming!").pretty_print()
# model.invoke("Do you know my name?").pretty_print()

messages =[
    HumanMessage(content="hello,我叫小明"),
    AIMessage(content="Hello, 小明! How can I assist you today?"),
    HumanMessage(content="What's my name?"),
]

model.invoke(messages).pretty_print()
