from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage,merge_message_runs
# 定义⼤模型  合并消息列表 - 合并  merge_message_runs 将连续的同类型消息合并成一个消息，减少模型处理的消息数量，提高效率
model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")
# 历史消息记录
messages = [
    SystemMessage("你是⼀个聊天助⼿。"),
    SystemMessage("你总是以笑话回应。"),
    HumanMessage("为什么要使⽤ LangChain?"),
    HumanMessage("为什么要使⽤ LangGraph?"),
    AIMessage("因为当你试图让你的代码更有条理时，LangGraph 会让你感到“节点”是个好主意！"),
    AIMessage("不过别担⼼，它不会“分散”你的注意⼒！"),
    HumanMessage("选择LangChain还是LangGraph?"),
]

# print(merge_message_runs(messages))
# merge_message =  merge_message_runs(messages)
# model.invoke(merge_message).pretty_print()

merger = merge_message_runs()
chain = merger | model
chain.invoke(messages).pretty_print()