
from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

"""示例选择器   基于长度的示例选择器（LengthBasedExampleSelector）是⼀种示例选择器，它根据示例的长度来选择适合当前输入的示例。"""


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


#   定义 长度基准 示例选择器
selector = LengthBasedExampleSelector(
    examples=examples,   # 示例
    example_prompt=example_prompt,  # 模版
    # 格式化⽰例的最⼤⻓度。
    # ⻓度由下⾯的get_text_length函数测量。
    max_length=5,
    # ⽤于获取字符串⻓度的函数，⽤于确定包含哪些⽰例。
    # 如果没有指定，它是作为默认值提供的。
    # 该函数返回⼀个整数，表⽰字符串中由换⾏符或空格分隔的“单词”数量
    # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ",x))
)


# ⽤于实例化⽰例的模板
dynamic_prompt = FewShotPromptTemplate(
    #  提供一个ExampleSelector而不是examples
    example_selector=selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="Input: {adjective}\nOutput:",
    input_variables=["adjective"],
)


print(
    dynamic_prompt.invoke({"adjective": "big"}).to_messages()[0].content
)

