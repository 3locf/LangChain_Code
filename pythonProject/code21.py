from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

# chat_prompt_template = ChatPromptTemplate(
#     [
#         ("system", "将文本从{language_from}翻译为{language_to}"),
#         ("user", "{text}"),
#     ]
# )

# print(chat_prompt_template.invoke(
#     {
#         "language_from": "英语", "language_to": "中文",
#         "text": "Alice is a good girl,I really like her,but she like Bob"
#     }))

# chain = chat_prompt_template | model
#
#
# print("======这是一个简易翻译,如果你想退出，请输入'exit'!========")
# while True:
#     print("\n请你输入原本的语言:")
#     language_from = input()
#     if language_from == "exit":
#         break
#     print("\n请你输入要翻译的语言:")
#     language_to = input()
#     if language_to == "exit":
#         break
#     print("\n请你输入要翻译的文本:")
#     text = input()
#     if text == "exit":
#         break
#     chain.invoke({"language_from": language_from, "language_to": language_to, "text": text}).pretty_print()



# 1. 定义一个提示词模版
# chat_prompt_template = ChatPromptTemplate.from_template("请你介绍{city}的特色美食和历史文化")
# prompt_template = PromptTemplate.from_template("请你介绍{city}的特色美食和历史文化")
#
# chain1 = prompt_template | model
#
# chain1.invoke({"city": "贵阳"}).pretty_print()


messages = [
    HumanMessage(content='我爱你'),
    AIMessage(content='i love you ,too'),
]

chat_prompt_template = ChatPromptTemplate(
    [
        ("system", "you are a powerful assistant"),
        MessagesPlaceholder("msgs"),
    ]
)

print(chat_prompt_template.invoke({"msgs": messages}))
# messages=[
#     SystemMessage(content='you are a powerful assistant', additional_kwargs={}, response_metadata={}),
#     HumanMessage(content='我爱你', additional_kwargs={}, response_metadata={}),
#     AIMessage(content='i love you ,too', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]



