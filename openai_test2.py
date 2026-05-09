# 聊天模型组件


from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

base_url = "https://api.laozhang.ai/v1"
system_message = ("请补全一段故事,20个字以内")

# 1.定义OpenAI⼤模型
model = ChatOpenAI(
    model="gpt-4o-mini",
    base_url=base_url,
    # temperature=0, # 温度 温度越高，AI回复的内容就越天马行空，温度越低，答案越保守
    max_tokens=None, # 输出的最大 token 数
    timeout=None, # 请求超时时间
    max_retries=2, # 最大的请求次数
    # api_key="...",
    # base_url="...",
    # organization="...",
    # other params...
)

# 2.定义消息列表
messages = [
    SystemMessage(content=system_message),
    HumanMessage(content="一只猫正在__?")
]

# 3.定义输出解析器组件
parser = StrOutputParser()

# 4.定义链
# 执行链
chain = model | parser
print(chain.invoke(messages))
