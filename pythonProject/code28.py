""" 按最⼤边际相关性选择⽰例（MMR） """
from langchain_chroma import Chroma
from langchain_core.example_selectors import MaxMarginalRelevanceExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# 反义词示例集合
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

prompt = PromptTemplate(
    input_ariables=["input", "output"],
    template="输入: {input}\n输出: {output}",
)

custom_embeddings = OpenAIEmbeddings(
    base_url="https://api.laozhang.ai/v1",
    model="text-embedding-3-large"
)

selector = MaxMarginalRelevanceExampleSelector.from_examples(
    examples,
    custom_embeddings,
    Chroma,
    k=2,
)


mmr_prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=prompt,
    prefix="给出每个输入的反义词",
    suffix="Input: {adjective}\nOutput:",
    input_variables=["adjective"],
)

print(mmr_prompt.invoke({"adjective": "funny"}).to_messages()[0].content)
