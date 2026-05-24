from langchain_community.document_loaders import PyPDFLoader

file_path = "./doc/.pdf"

# 创建一个 PyPDFLoader 对象，传入 PDF 文件的路径。
loader = PyPDFLoader(file_path)


# 将 PDF ⽂件的每⼀⻚转换为⼀个独⽴的 Document 对象，并存储在列表 docs 中。
docs = loader.load()

# print(f"PDF的总页数:\n {len(docs)}\n")
# print(f"问：第⼀⻚⽂本内容的前200个字符是：\n{docs[0].page_content[:200]}\n")
# print(f"问：第⼀⻚元数据：\n{docs[0].metadata}")

print(docs[5])
