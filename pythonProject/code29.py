"""通过 ngram 重叠选择⽰例（Ngram）"""
from langchain_community.example_selectors import NGramOverlapExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

# 翻译⽰例
examples = [
    {"input": "See Spot run.", "output": "看⻅Spot跑。"},
    {"input": "My dog barks.", "output": "我的狗叫。"},
    {"input": "Spot can run.", "output": "Spot可以跑。"},
    {"input": "My dog can run.", "output": "我的狗也可以跑。"},
    {"input": "i love you", "output": "我爱你"},
]


# 字符串模板
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)


selector = NGramOverlapExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    threshold=0.0,  # 这里的阈值设置的情况有很多，可以根据实际需求进行调整。较高的阈值可能会导致选择更少的示例，而较低的阈值可能会选择更多的示例。
    # threshold=0.0 （表⽰排除不相关的⽰例）
    # threshold=1.0（排除所有⽰例）
)


# ⽤于实例化⽰例的模板
dynamic_prompt = FewShotPromptTemplate(
    example_selector=selector,
    example_prompt=example_prompt,
    prefix="给出每个输⼊的中文翻译",
    suffix="Input: {sentence}\nOutput:",
    input_variables=["sentence"],
)

print(dynamic_prompt.invoke({"sentence": "My dog can run."}).to_messages()[0].content)