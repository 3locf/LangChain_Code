from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter

file_path = "./doc/在线图书借阅系统.md"

loader = UnstructuredMarkdownLoader(file_path)

docs = loader.load()

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",  # cl100k_base 是 OpenAI 的一个编码器，适用于处理文本数据。它能够将文本转换为一系列的标记（tokens），这些标记可以是单词、子词或字符，具体取决于编码器的设计。
    chunk_size=500,
    chunk_overlap=20,
)

docs_split = text_splitter.split_documents(docs)

for ducment in docs_split[:10]:
    print("*" * 30)
    print(ducment.page_content[:200])
    print(ducment.metadata)
