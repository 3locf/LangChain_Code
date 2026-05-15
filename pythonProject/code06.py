from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

base_url = "https://api.laozhang.ai/v1"


# 定义模型
model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url=base_url)

# 定义工具
tool = TavilySearch(max_results=3)
# 绑定模型和工具
tool_with_model = model.bind_tools([tool])

message = [
    HumanMessage(content="NBA球星德安吉洛.拉塞尔的实力怎么样？")
]

ai_msg = tool_with_model.invoke(message)

# tool_calls=[{'name': 'tavily_search',
# 'args': {'query': '贵阳天气', 'topic': 'general'},
# 'id': 'call_s6wot2Rrf0G1LYyXKIbaMFjz',
# 'type': 'tool_call'}]
message.append(ai_msg)

tool_map = {"tavily_search": tool}
for tool_call in ai_msg.tool_calls:
    select_tool = tool_map[tool_call["name"]]
    tool_result = select_tool.invoke(tool_call)
    message.append(tool_result)

result = model.invoke(message)
print(result.content)