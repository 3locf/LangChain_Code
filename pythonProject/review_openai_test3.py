from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

base_url = "https://api.laozhang.ai/v1"
message = [
    SystemMessage(content="你是一个全能的智能助手，拥有广博的知识，"
                  "能够解答编程、科技、生活等各个领域的问题。请务必始终使用流畅、"
                  "专业、易懂的中文进行回答。保持友善、耐心和客观的态度。"),
    HumanMessage(content="你好呀，我想认识你"),
]

# 1.定义聊天模型
gpt_model = init_chat_model(model="gpt-4o-mini", model_provider="openai", base_url=base_url)
deep_model = init_chat_model(model="deepseek-chat", model_provider="deepseek", api_key="c5")

# 2.调用大模型
print(f"chat-gpt : {gpt_model.invoke(input=message).content}")
print(f"deepseek : {deep_model.invoke(input=message).content}")

