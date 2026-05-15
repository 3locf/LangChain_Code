from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

base_url = "https://api.laozhang.ai/v1"
system_message = ("你是一个全能的智能助手，拥有广博的知识，"
                  "能够解答编程、科技、生活等各个领域的问题。请务必始终使用流畅、"
                  "专业、易懂的中文进行回答。保持友善、耐心和客观的态度。")

message = [
    SystemMessage(content=system_message),
    HumanMessage(content="我爱你你要记得我。"),
]

#  1. 定义聊天模型
model = ChatOpenAI(model="gpt-4o-mini", base_url=base_url)

# 2. 定义输出解析器
parser = StrOutputParser()

# 3.定义链
chain = model | parser
# chain = model.pipe(parser)

# 4.执行链
print(chain.invoke(message))

