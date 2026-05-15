from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# 提示词模版


model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")

#  定义文本提示词模版 方式一
# prompt_template = PromptTemplate(
#     template="介绍{city}的历史",
#     input_variables=["city"]
# )

#  定义模版 方式二
# prompt_template = PromptTemplate.from_template("将文本从{language_from}翻译为{language_to}")
#
# # 使用模版
# print(prompt_template.invoke({
#     "language_from": "中文",
#     "language_to": "英语"
# }))



# 处理聊天消息的模版
# chat_prompt_template = ChatPromptTemplate(
#     [
#         ("system", "将文本从{language_from}翻译为{language_to}"),
#         ("user", "{text}"),
#         # ("ai", "")
#     ]
# )

# messages = chat_prompt_template.invoke({
#     "language_from": "中文",
#     "language_to": "英语",
#     "text": "你好,我叫小明"
# })

# print(chat_prompt_template.invoke({
#     "language_from": "中文",
#     "language_to": "英语",
#     "text": "你好,我叫小明"
# }))
#  实例化后会生成一个新的模版，模版里已经将system和user的消息内容按照我们传入的参数进行了替换
# messages=[SystemMessage(content='将文本从中文翻译为英语', additional_kwargs={}, response_metadata={}),
#           HumanMessage(content='你好,我叫小明', additional_kwargs={}, response_metadata={})]


chat_prompt_template = ChatPromptTemplate(
    [
        ("system", "将文本从{language_from}翻译为{language_to}"),
        MessagesPlaceholder("msgs"),  # MessagesPlaceholder 可以让我们在调用模版时传入一个消息列表，模版会将这个消息列表插入到指定的位置，这样我们就可以灵活地构建多轮对话的消息列表，而不需要在模版里固定每一轮对话的内容
        ("user", "{text}"),

        # ("ai", "")
    ]
)


messages_placeholder = [
    HumanMessage(content="你知道的我一直爱你！！！"),
    AIMessage(content="I have always loved you!!!")
]

# print(chat_prompt_template.invoke({
#     "language_from": "中文",
#     "language_to": "英语",
#     "text": "许多年后，我终于鼓起勇气告诉你我的心意，我爱你！",
#     "msgs": messages_placeholder
# }))


chain = chat_prompt_template | model
print(chain.invoke({
    "language_from": "中文",
    "language_to": "英语",
    "text": "许多年后，我终于鼓起勇气告诉你我的心意，我爱你！",
    "msgs": messages_placeholder
}).content)




