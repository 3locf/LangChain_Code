"""按语义相似性选择⽰例（Similarity）"""
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAIEmbeddings

# 反义词⽰例集合
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]


# 定义提示词模版
example_prompt = PromptTemplate(
    input_ariables=["input", "output"],
    template="输入：{input}\n输出：{output}"
)

custom_embeddings = OpenAIEmbeddings(
    base_url="https://api.laozhang.ai/v1",
    model="text-embedding-3-large"
)

#  语义相似性示例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    #  嵌⼊类⽤于⽣成⽤于度量语义相似度的嵌⼊。 嵌入模型
    custom_embeddings,
    # VectorStore类，⽤于存储嵌⼊并对其进⾏相似性搜索。 向量数据库
    Chroma,
    # ⽣成⽰例的数量。
    k=1,
)



 #  ⽤于实例化⽰例的模板
similarity_prompt = FewShotPromptTemplate(
     example_selector=example_selector,
     example_prompt=example_prompt,
     prefix="给出每个输入的反义词",
     suffix="Input: {adjective}\nOutput:",
     input_variables=["adjective"],
 )

result = similarity_prompt.invoke({"adjective": "funny"}).to_messages()[0].content

print(result)