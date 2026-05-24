# 基于字符⻓度拆分
from langchain_community.document_loaders import UnstructuredMarkdownLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

file_path = "./doc/在线图书借阅系统.md"

loader = UnstructuredMarkdownLoader(file_path, mode="single")
docs = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n\n",  # 选择分割符
    chunk_size=500,  # 设定目标： 目标块大小
    chunk_overlap=20,  # 设定目标：块之间的重叠大小
    length_function=len,  # 使用测量长度函数
    is_separator_regex=False,  # 分隔符是否是正则表达式
)

texts = text_splitter.split_documents(docs)

# 打印前10个被分割出来的⽂档
for document in texts[:10]:
    print("*" * 30)
    print(f"{document}\n")