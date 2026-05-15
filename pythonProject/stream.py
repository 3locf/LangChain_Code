import asyncio

from langchain_openai import ChatOpenAI

base_url = "https://api.laozhang.ai/v1"

model = ChatOpenAI(model="gpt-4o-mini", base_url=base_url)

# print(model.invoke("请给我写一份关于春天的诗歌，要求押韵，200字以内").content)

#  返回的是一个迭代器，产生的内容是一个个的文本块，文本块之间是连续的
# chunks = []
# result = model.stream("请给我写一份关于春天的诗歌，要求押韵，200字以内")
# #  chunk 的类型是AIMessageChunk
# for chunk in result:
#     chunks.append(chunk)
#     # print(chunk.content, end="/", flush=True)
#
# print(chunks[0].content+chunks[1].content+chunks[2].content+chunks[3].content+chunks[4].content)


async def async_stream():
  print("===异步流式处理===")
  async for chunk in model.astream("请给我写一份关于春天的作文，要求押韵，2000字以内"):
    print(chunk.content, end="/", flush=True)

asyncio.run(async_stream())