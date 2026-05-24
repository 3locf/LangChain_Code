from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = "./doc/在线图书借阅系统.md"

loader = UnstructuredMarkdownLoader(file_path)

docs = loader.load()

# 强制按照约定的 chunk_size 和 chunk_overlap 来拆分文本，直到满足条件为止。它会递归地尝试不同的分割策略，直到找到合适的分割点。
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base",
    separators=["\n\n", "\n", " ", "。", ",", "",],
    chunk_size=50,
    chunk_overlap=0,
    is_separator_regex=True,
)

docs_split = text_splitter.split_documents(docs)

for ducment in docs_split[:10]:
    print("*" * 30)
    print(ducment.page_content)
    print(ducment.metadata)

