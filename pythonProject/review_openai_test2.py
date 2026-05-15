from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

base_url = "https://api.laozhang.ai/v1"

# model = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0.9,
#     max_tokens=100,
#     base_url=base_url,
#     max_retries=None,
#     timeout=None,
#     # api_key="..."
# )

# result = model.invoke(
#     input=[
#         {"role": "system", "content": "你是一个友好、耐心的AI助手，回答要简洁易懂，用口语化的英文"},
#         {"role": "user", "content": "你在干嘛呢？"}
#     ]
# )

# print(result.content)

# --------------------------------------------------------------------------------------------------------------------------

# model = init_chat_model(
#     base_url=base_url,
#     temperature=0.7,
# )
#
# result = model.invoke( input=[
#         {"role": "system", "content": "你是一个友好、耐心的AI助手，回答要简洁易懂，用口语化的英文"},
#         {"role": "user", "content": "你在干嘛呢？"}
#     ], config={"configurable": {"model": "gpt-4o-mini"}}
# )
#
# print(result.content)

#---------------------------------------------------------------------------------------------------------------------------

model = init_chat_model(
    base_url=base_url,
    temperature=0.7,
    model="gpt-4o-mini",
    model_provider="openai",
    configurable_fields=["model", "base_url", "model_provider"],
    config_prefix="test",
    api_key=""
)

result = model.invoke(
    input=[{"role": "system", "content": "你是一个友好、耐心的AI助手，回答要简洁易懂，用口语化的日语"},
        {"role": "user", "content": "我想你了，你在做什么"}
    ],
    config={"configurable": {"test_model": "deepseek-chat", "test_model_provider": "deepseek"}},
)

print(result)

