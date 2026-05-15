from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

# 案例
examples = [
    {"text": "hi, what is your name?", "output": "你好，你叫什么名字？"},
    {"text": "hi, what is your age?", "output": "你好，你多大了？"},
]


# 与案例关联的提示词模版
example_prompt = ChatPromptTemplate(
    [
        ("user", "{text}"),
        ("ai", "{output}"),
    ]
)

# 将案例转换为 消息列表，插入到提示词模版中去
# 少量样本提示词模版
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,     # 案例
    example_prompt=example_prompt,    # ChatPromptTemplate 模版
)

# print(few_shot_prompt.invoke({}).to_messages())
# [HumanMessage(content='hi, what is your name?', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='你好，你叫什么名字？', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#  HumanMessage(content='hi, what is your age?', additional_kwargs={}, response_metadata={}),
#  AIMessage(content='你好，你多大了？', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]


chat_prompt_template = ChatPromptTemplate(
    [
        ("system", "将文本从{language_from}翻译为{language_to}"),
        # 示例
        few_shot_prompt,
        ("user", "{text}"),
    ]
)

# print(chat_prompt_template.invoke({"language_from": "英语", "language_to": "中文", "text": "what are you doing?"}))
# messages=[SystemMessage(content='将文本从英语翻译为中文', additional_kwargs={}, response_metadata={}),
#           HumanMessage(content='hi, what is your name?', additional_kwargs={}, response_metadata={}),
#           AIMessage(content='你好，你叫什么名字？', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#           HumanMessage(content='hi, what is your age?', additional_kwargs={}, response_metadata={}),
#           AIMessage(content='你好，你多大了？', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
#           HumanMessage(content='what are you doing?', additional_kwargs={}, response_metadata={})]


chain = chat_prompt_template | model

chain.invoke({"language_from": "英语", "language_to": "中文", "text": "what are you doing?"}).pretty_print()
