from langchain_openai import ChatOpenAI
base_url = "https://api.laozhang.ai/v1"

# 定义⼤模型
model = ChatOpenAI(model="gpt-4o-mini", base_url=base_url)
json_schema = {
    "title": "joke",
    "description": "给⽤⼾讲⼀个笑话。",
    "type": "object",
    "properties": {
        "setup": {
            "type": "string",
            "description": "这个笑话的开头",
        },
        "punchline": {
            "type": "string",
            "description": "这个笑话的妙语",
        },
        "rating": {
            "type": "integer",
            "description": "从1到10分，给这个笑话评分",
            "default": None,
        },
    },
    "required": ["setup", "punchline"],
}
structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke("给我讲⼀个关于唱歌的笑话")
print(result)
