from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

base_url = "https://api.laozhang.ai/v1"
system_message = ("你是一个全能的智能助手，拥有广博的知识，"
                  "能够解答编程、科技、生活等各个领域的问题。请务必始终使用流畅、"
                  "专业、易懂的中文进行回答。保持友善、耐心和客观的态度。")

model = ChatOpenAI(
    base_url=base_url,
    model='gpt-4o-mini'
)

messages = [
    HumanMessage(content=system_message),
    SystemMessage(content='请你给我说说中国作家张嘉佳的一些经典语句'),
]

result = model.invoke(messages)

print(result.content)