"""
示例演示：使用 LangChain 的 ChatPromptTemplate 与 FewShotChatMessagePromptTemplate
构造一个少样本（few-shot）提示，并将其与聊天模型组合后进行一次演示调用。
"""

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

# 初始化聊天模型（这里只是构造模型对象，真正的网络请求通常发生在调用模型时）
# 参数说明：第一个参数是模型名称，base_url 指向模型服务的 HTTP API 端点
model = init_chat_model("gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

# 1.  这是少样本示例（examples）——每个示例包含输入和期望输出，作为提示的一部分
examples = [
    {"input": "2 🐻 3", "output": "11"},
    {"input": "2 🐻 4", "output": "13"},
    {"input": "2 🐻 7", "output": "19"},
]

# 定义单个示例的提示模版：先是 human 的内容（输入），再是 ai 的内容（对应的输出）
# 这里使用 ChatPromptTemplate 表示一个人类消息/AI消息对的模版。
chat_prompt_template = ChatPromptTemplate(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

# 使用 FewShotChatMessagePromptTemplate 将多个示例组合在一起，形成少样本提示
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,    # 少样本案例列表
    example_prompt=chat_prompt_template,   # 每个案例遵循的模板
)

# 打印 few_shot_prompt.invoke({}).to_messages() 的结果可以看到构造出来的消息序列，
# print(few_shot_prompt.invoke({}).to_messages())
# [HumanMessage(content='2 ?? 3', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='11', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='2 ?? 4', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='13', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='2 🐻 7', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='19', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]


# 构造最终的 ChatPromptTemplate：包含 system 提示、few-shot 示例，以及后续的人类输入占位符
final_prompt = ChatPromptTemplate(
    [
        ("system", "你是一个神奇的数学奇才!"),  # 系统消息：设定模型的身份和行为
        few_shot_prompt,                              # 少样本示例（会插入上面的 examples）
        ("human", "{input}"),                     # 最终用户输入的占位符
    ]
)

# 将提示模板与模型通过管道符（|）组合成一个链，便于后续调用：
# chain.invoke({"input": ...}) 将会把填充好的消息发送到模型并获得响应。
chain = final_prompt | model


# 运行一次演示调用（注意：这将触发与模型服务的网络交互）
result = chain.invoke({"input": "2 🐻 8"})
# pretty_print 将以可读形式输出模型返回的消息/内容
result.pretty_print()
