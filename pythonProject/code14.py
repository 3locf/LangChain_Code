from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# 内存消息历史
model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")


store = {}

# 根据会话Id 查询会话里的消息列表
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        # InMemoryChatMessageHistory() 帮助我们将AI和Human的消息列表保存在内存中，后续我们可以根据session_id 获取对应的消息列表
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 包装了model ,让model具有了消息历史的功能，调用model时会自动根据session_id获取对应的消息历史，并将新的消息添加到历史中
with_history_model = RunnableWithMessageHistory(model, get_session_history)


# invoke: config: 配置 Runnable 实例
config = {
    "configurable": {"session_id": "123456"}
}

with_history_model.invoke(
    [HumanMessage(content="你好,我叫小明")],
    config=config
).pretty_print()

with_history_model.invoke(
    [HumanMessage(content="你好,你知道我是谁吗？")],
    config=config
).pretty_print()