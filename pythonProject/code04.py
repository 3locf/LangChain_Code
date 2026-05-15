from typing import Annotated

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool, StructuredTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

base_url = "https://api.laozhang.ai/v1"


# 定义工具---》绑定工具---》调用工具（1.工具选择   2.调用工具）

@tool
def add(
        a: Annotated[int, ..., "第一个加数"],
        b: Annotated[int, ..., "第二个加数"],
) -> int:
    """两数相加"""
    return a + b



def multiple(a: int, b: int) -> int:
    return a * b


class MultipleInput(BaseModel):
    a: int = Field(..., description="第一个乘数")
    b: int = Field(..., description="第二个乘数")


mul_tool = StructuredTool.from_function(
    func=multiple,
    args_schema=MultipleInput,   #  工具参数
    description="两数相乘",  # 工具描述
    name="mul",
)

model = ChatOpenAI(model='gpt-4o-mini', base_url=base_url)
deep_model = init_chat_model(model="deepseek-chat", model_provider="deepseek", api_key="")

#  绑定工具
tools = [mul_tool, add]
# model_with_tools = deep_model.bind_tools(tools=tools)

#  强制选择工具 tool_choice
model_with_tools = deep_model.bind_tools(tools=tools)

# 调用工具
# print(model_with_tools.invoke("2乘3等于多少?"))   根据输入相关性，选择是否调用工具
# print(model_with_tools.invoke("你是谁?"))

# ai_msg = model_with_tools.invoke("2乘3等于多少？")
# print(ai_msg)

# 定义消息列表，添加要传递给消息模型的消息
#  HumanMessage -->  [HumanMessage(content='2乘3等于多少？5加8等于多少', additional_kwargs={}, response_metadata={}),
message = [
    HumanMessage("2乘3等于多少？5加8等于多少")
]
ai_msg = model_with_tools.invoke(message)

# print(ai_msg)
# tool_calls=[
#     {'name': 'MUL', 'args': {'a': 2, 'b': 3}, 'id': 'call_00_xrm7zue4fO95xZPyi8JoPq6D', 'type': 'tool_call'},
#     {'name': 'add', 'args': {'a': 5, 'b': 8}, 'id': 'call_01_Q0tn0vlODwjznBhIjqxkJdSx', 'type': 'tool_call'}
# ]

message.append(ai_msg)
#  AIMessage(content='', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 96, 'prompt_tokens': 385, 'total_tokens': 481, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 385}, 'model_provider': 'deepseek', 'model_name': 'deepseek-v4-flash', 'system_fingerprint': 'fp_058df29938_prod0820_fp8_kvcache_20260402', 'id': 'e8378206-348c-4987-b763-77ef6aeec322', 'finish_reason': 'tool_calls', 'logprobs': None}, id='lc_run--019de3b7-a91b-77a1-a13a-f07fc160cf46-0',
#  tool_calls=[
#  {'name': 'mul', 'args': {'a': 2, 'b': 3}, 'id': 'call_00_vhZFMu2RUKrqkcTkzDsXfPQQ', 'type': 'tool_call'},
#  {'name': 'add', 'args': {'a': 5, 'b': 8}, 'id': 'call_01_l55SJVrrcIEORbJw352Vxykv', 'type': 'tool_call'}
#  ],
#  invalid_tool_calls=[], usage_metadata={'input_tokens': 385, 'output_tokens': 96, 'total_tokens': 481, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}}),


# 构造 ToolMessage，并添加到消息列表中去
tool_map = {
    "add": add,
    "mul": mul_tool
}
for tool_call in ai_msg.tool_calls:
    selected_tool = tool_map[tool_call["name"].lower()]
    tool_msg = selected_tool.invoke(tool_call)
    # ToolMessage(content='6', name='mul', tool_call_id='call_00_vhZFMu2RUKrqkcTkzDsXfPQQ'),
    # ToolMessage(content='13', name='add', tool_call_id='call_01_l55SJVrrcIEORbJw352Vxykv')]
    message.append(tool_msg)

print(message)
# 组合 HumanMessage、AIMessage、ToolMessage 然后喂给大模型
print(model.invoke(message).content)

