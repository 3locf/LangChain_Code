from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter

loader = UnstructuredMarkdownLoader("./doc/test.md", mode="single")

docs = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n\n",  # 选择分割符
    chunk_size=50,  # 设定目标： 目标块大小
    chunk_overlap=2,  # 设定目标：块之间的重叠大小
    length_function=len,  # 使用测量长度函数
    is_separator_regex=False,  # 分隔符是否是正则表达式
)

documents = text_splitter.split_documents(docs)

for document in documents:
    print("*" * 30)
    print(f"{document}\n")
