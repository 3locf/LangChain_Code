from typing import TypedDict, Annotated

from langchain.chat_models import init_chat_model
api_key = "sk-3b9d76669a784dfb9f513a93ff6062c5"

model = init_chat_model(model="deepseek-chat", model_provider="deepseek", api_key=api_key)


#  方法二   使用TypedDict定义结构化输出
class User(TypedDict):
    """用户信息"""
    name: Annotated[str, ..., "用户名称"]
    age: Annotated[int, ..., "用户年龄"]
    sex: Annotated[str, ..., "用户性别"]
    hobbies: Annotated[list[str], ..., "用户爱好列表"]


#  include_raw=True  让模型在返回结构化输出的同时，也返回原始的文本输出，方便我们进行对比和调试。
model_with_output = model.with_structured_output(User, include_raw=True)
print(model_with_output.invoke("请你介绍一下雷军"))

