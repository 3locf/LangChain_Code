from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, filter_messages
from langchain_openai import ChatOpenAI

#  管理消息列表 - 过滤
model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

# 历史消息记录
messages = [
    SystemMessage("你是⼀个聊天助⼿", id="1"),
    HumanMessage("⽰例输⼊", id="2"),
    AIMessage("⽰例输出", id="3"),
    HumanMessage("真实输⼊", id="4"),
    AIMessage("真实输出", id="5"),
]

# 按照类型过滤消息
# print(filter_messages(include_types="human").invoke(messages))
# print(filter_messages(messages, include_types="human"))

# 按照id过滤消息
# print(filter_messages(messages, exclude_ids=["1"]))
print(filter_messages(messages, exclude_ids=["2"], include_types=[HumanMessage, AIMessage]))
