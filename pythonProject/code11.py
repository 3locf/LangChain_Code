from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

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
    HumanMessage(content="今天贵阳的天气怎么样？")
]

ai_msg = tool_with_model.invoke(message)
message.append(ai_msg)

tool_map = {"tavily_search": tool}
for tool_call in ai_msg.tool_calls:
    select_tool = tool_map[tool_call["name"]]
    tool_result = select_tool.invoke(tool_call)
    message.append(tool_result)


class SearchResult(BaseModel):
    query: str = Field(..., description="搜索查询")
    results: str = Field(..., description="搜索结果")
    resource: str = Field(..., description="搜索来源链接")


tools = tool_with_model.with_structured_output(SearchResult)
print(tools.invoke(message))



