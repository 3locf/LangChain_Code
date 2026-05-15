from typing import Iterator, List

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

base_url = "https://api.laozhang.ai/v1"
message = [SystemMessage(content="用户叫你创作内容时，每句话使用中文句号分隔开")]
human_input: HumanMessage = input("请输入内容：")  #写一段关于爱情的歌词，需要5句话。
message.append(human_input)

# 组件1：定义OpenAI⼤模型
model = ChatOpenAI(model="gpt-4o-mini", base_url=base_url)

# 组件2：定义输出解析器
parser = StrOutputParser()

# 自定义生成器
def split_into_list(input: Iterator[str]) -> Iterator[List[str]]:
    buffer = ""
    for chunk in input:
        buffer += chunk
        # 遇到句号，需要将buffer中的内容分割成列表并yield出来
        while "。" in buffer:
            index = buffer.index("。")
            yield [buffer[:index].strip() + "。"]  # yield一个列表，列表中只有一个元素，
            buffer = buffer[index + 1:]  # 更新buffer，去掉已经yield的内容
    yield [buffer.strip()]  # 最后yield一个列表，列表中只有一个元素，就是buffer中的内容

# 将模型和解析器组合起来
chain = model | parser | split_into_list

for chunk in chain.stream(message):
    # 使用parser 结果就是str
    print(chunk, end="/", flush=True)