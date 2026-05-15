from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

base_url = "https://api.laozhang.ai/v1"
system_message = ("你是一个全能的智能助手，拥有广博的知识，"
                  "能够解答编程、科技、生活等各个领域的问题。请务必始终使用流畅、"
                  "专业、易懂的中文进行回答。保持友善、耐心和客观的态度。")

# 1.定义OpenAI⼤模型
# 默认从系统环境变量中读取 OPENAI_API_KEY
model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url=base_url
)

# 2.定义消息列表
# 用户消息 -》  HumanMessage
# 系统提示消息 -》 SystemMessage  通常作为第一条消息进行传入
# AI 消息 AIMessage
messages = [
    SystemMessage(content=system_message),
    HumanMessage(content="我爱你，你要记得我")
]


# 3.调用大模型
# result = model.invoke(messages)
# print(result)

# 4.定义输出解析器组件
parser = StrOutputParser()
# print(parser.invoke(result))

# 5.定义链
# 执行链
# chain = model | parser
# chain = RunnableSequence(first=model, last=parser)
chain = model.pipe(parser)
print(chain.invoke(messages))

