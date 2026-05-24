from langchain_core.documents import Document

documents = [
    Document(
        # 内容字符串
        page_content="狗是人类最好的朋友，它们忠诚、友善，能够陪伴我们度过快乐和困难的时光。",
        # 元信息
        # 元信息是一个字典，可以包含文档的标题、作者、日期、来源等信息。
        metadata={"source": "mammal-pets-doc"}
    ),
    Document(
        page_content="猫是独立、优雅的动物，它们喜欢独处，但也能与人类建立深厚的感情。",
        metadata={"source": "mammal-pets-doc"}
    )
]

print(documents[0].page_content)
print(documents[0].metadata)