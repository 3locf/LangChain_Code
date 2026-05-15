from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, trim_messages
from langchain_openai import ChatOpenAI

# 消息管理列表 - 裁剪
model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

messages = [
    SystemMessage(content="you're a good assistant"),
    HumanMessage(content="hi! I'm bob"),
    AIMessage(content="hi!"),
    HumanMessage(content="I like vanilla ice cream"),
    AIMessage(content="nice"),
    HumanMessage(content="whats 2 + 2"),
    AIMessage(content="4"),
    HumanMessage(content="thanks"),
    AIMessage(content="no problem!"),
    HumanMessage(content="having fun?"),
    AIMessage(content="yes!"),
    HumanMessage(content="What's my name?"),
]

# token数
# trimmer = trim_messages(
#     max_tokens=65,      # 修剪消息的最⼤令牌数，根据你想要的谈话⻓度来调整
#     strategy="last",    # 修剪策略：
#                         # “last”（默认）：保留最后的消息。
#                         # “first”：保留最早的消息。
#     token_counter=model,  # 传⼊⼀个函数或⼀个语⾔模型（因为语⾔模型有消息令牌计数⽅法）
#     include_system=True,  # 如果想始终保留初始系统消息，可以指定include_system=True
#     allow_partial=False,  #是否允许拆分消息的内容
#     start_on="human",    # 如果需要确保我们的第⼀条消息（不包括系统消息）始终是特定类型，可以指定 start_on
# )


# 消息数
trimmer = trim_messages(
    max_tokens=11,      # 修剪消息的最⼤令牌数，根据你想要的谈话⻓度来调整
    strategy="last",    # 修剪策略：
                        # “last”（默认）：保留最后的消息。
                        # “first”：保留最早的消息。
    token_counter=len,  # 传⼊⼀个函数或⼀个语⾔模型（因为语⾔模型有消息令牌计数⽅法）
    include_system=True,  # 如果想始终保留初始系统消息，可以指定include_system=True
    allow_partial=False,  #是否允许拆分消息的内容
    start_on="human",    # 如果需要确保我们的第⼀条消息（不包括系统消息）始终是特定类型，可以指定 start_on
)

# print(trimmer.invoke(messages))
# [SystemMessage(content="you're a good assistant", additional_kwargs={}, response_metadata={}),
#  HumanMessage(content='I like vanilla ice cream', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='nice', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='whats 2 + 2', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='4', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='thanks', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='no problem!', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='having fun?', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='yes!', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content="What's my name?", additional_kwargs={}, response_metadata={})]


#  先对消息列表进行裁剪，确保它们的总令牌数不超过65，然后将裁剪后的消息列表传递给模型进行处理
chain = trimmer | model

print(chain.invoke(messages))
