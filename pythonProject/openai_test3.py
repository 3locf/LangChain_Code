# 聊天模型 init_chat_model()

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

base_url = "https://api.laozhang.ai/v1"

# gpt_model = init_chat_model(base_url=base_url, model="gpt-4o-mini", model_provider="openai")
# deep_model = init_chat_model(model="deepseek-chat", model_provider="deepseek", api_key="sk-3b9d76669a784dfb9f513a93ff6062c5")


# print(gpt_model.invoke("你是谁？").content)
# print(deep_model.invoke("你是谁？是由哪家公司开发的？").content)

# system_message = ("你是一个全能的智能助手，拥有广博的知识，"
#                   "能够解答编程、科技、生活等各个领域的问题。请务必始终使用流畅、"
#                   "专业、易懂的中文进行回答。保持友善、耐心和客观的态度。")

# messages = [
#     SystemMessage(content=system_message),
#     HumanMessage(content="我爱你，你要记得我")
# ]

# 2.定义可配置的模型（模型模拟器）
# .invoke() 的config参数才真正意义上定义了模型
# config_model = init_chat_model(temperature=0.3, api_key="sk-3b9d76669a784dfb9f513a93ff6062c5")
# print(config_model.invoke(input=messages,
#                           config={"configurable": {"model": "deepseek-chat"}})
#       )




# 3.具有默认值的可配置模型

messages = [
    SystemMessage(content="请补全一段故事,100个字以内,使用中文回答"),
    HumanMessage(content="一只猫正在__?")
]


# gpt_model = init_chat_model(
#     base_url=base_url,
#     model="gpt-4o-mini",
#     model_provider="openai",
#     max_tokens=1024,
#     configurable_fields=("max_tokens",), 可变参数key，是一个列表
#     config_prefix="first",
# )
#
# result = gpt_model.invoke(
#     input=messages,
#     config={"configurable": {"first_max_tokens": 10}}
# )
# print(result.content)

model = init_chat_model(
    base_url=base_url,
    model="gpt-4o-mini",
    model_provider="openai",
    temperature=0.3,
    configurable_fields=("model", "model_provider"),
    config_prefix="hello",
    api_key=""
)

result = model.invoke(
    messages,
    config={"configurable": {"hello_model": "deepseek-chat", "hello_model_provider": "deepseek"}}
)

print(result)


