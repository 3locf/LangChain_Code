from typing import Optional

from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.utils.function_calling import tool_example_to_messages
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


#  1. 定义结构化输出
class Person(BaseModel):
    """描述一个人的信息"""

    name: Optional[str] = Field(default=None, description="这个人的姓名")
    hair_color: Optional[str] = Field(default=None, description="如果知道这个人的头发颜色")
    skin_color: Optional[str] = Field(default=None, description="如果知道这个人的皮肤颜色")
    height_in_meters: Optional[str] = Field(default=None, description="以米为单位的身高")


class Data(BaseModel):
    """提取关于人的数据"""
    people: list[Person]


# 2. 定义两个示例
examples = [
    (
        "海洋是⼴阔⽽蓝⾊的。它有两万多英尺深。",
        Data(people=[]),  # 没有⼈物信息的情况
    ),
    (
        "⼩强从中国远⾏到美国。",
        Data(people=[Person(name="⼩强", height_in_meters=None, skin_color=None, hair_color=None),]),  # 部分信息缺失的情况
    ),
]


# 3. 定义提示词模版
chat_prompt_template = ChatPromptTemplate([
    ("system", "你是⼀个提取信息的专家，只从⽂本中提取相关信息。如果您不知道要提取的属性的值，属性值返回null"),
    MessagesPlaceholder("example_messages"),
    ("user", "{new_message}"),
])

# 4. 获取样例消息列表
example_messages = []
# 遍历示例对，将每个示例构造成聊天消息
for text, tool_call in examples:
    # 根据提取结果生成AI响应文本
    if tool_call.people:
        ai_response = "检测到人"
    else:
        ai_response = "没有检测到人"

    # 将示例转换为模型可理解的消息格式
    example_messages.extend(
        tool_example_to_messages(text, [tool_call],ai_response=ai_response)
    )   # ⽅法返回 list[BaseMessage]

# print(example_messages)
# [
# HumanMessage(content='海洋是⼴阔⽽蓝⾊的。它有两万多英尺深。', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': '826129d7-7397-4b30-be08-648c97932f12', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': []}, 'id': '826129d7-7397-4b30-be08-648c97932f12', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='826129d7-7397-4b30-be08-648c97932f12'),
# AIMessage(content='没有检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[]),
# HumanMessage(content='⼩强从中国远⾏到美国。', additional_kwargs={}, response_metadata={}),
# AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'b9e56ffc-5be2-4c5c-96f9-464a0c6b97ae', 'type': 'function', 'function': {'name': 'Data', 'arguments': '{"people":[{"name":"⼩强","hair_color":null,"skin_color":null,"height_in_meters":null}]}'}}]}, response_metadata={}, tool_calls=[{'name': 'Data', 'args': {'people': [{'name': '⼩强', 'hair_color': None, 'skin_color': None, 'height_in_meters': None}]}, 'id': 'b9e56ffc-5be2-4c5c-96f9-464a0c6b97ae', 'type': 'tool_call'}], invalid_tool_calls=[]),
# ToolMessage(content='You have correctly called this tool.', tool_call_id='b9e56ffc-5be2-4c5c-96f9-464a0c6b97ae'),
# AIMessage(content='检测到人', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])
# ]

# 5. 调⽤
# 定义结构化输出模型，⾃动解析为 Pydantic 对象
model = ChatOpenAI(model="gpt-4o-mini", base_url="https://api.laozhang.ai/v1")
model_with_structured = model.with_structured_output(schema=Data)

# 6. 定义连
chain = chat_prompt_template | model_with_structured

result = chain.invoke(
    {
        "example_messages": example_messages,
        "new_message": "天空是蔚蓝色，窗外有千纸鹤。"
    })

print("\n")
print(result)





