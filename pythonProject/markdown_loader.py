from langchain_community.document_loaders import UnstructuredMarkdownLoader

file_path = "./doc/企业员工管理系统文档.md"

# "single": 默认模式。将整个 Markdown 文件作为一个单一的文档对象（Document）处理。
# "elements": 将 Markdown 文件解析为独立的元素（如标题、段落、列表项等），每一个元素作为一个单独的 Document 对象返回。这种模式非常适合需要对文档结构进行更细粒度控制的场景。
# "pdx" (在某些版本中): 以分区数据交换格式（Partitioned Data Exchange）处理。
# loader = UnstructuredMarkdownLoader(file_path, mode="single")
loader = UnstructuredMarkdownLoader(file_path, mode="elements")


docs = loader.load()

# print(f"总共有{len(docs)}个文档")
# print(docs[0].page_content[:200])
# print(docs[0].metadata)
# print(docs[1].page_content[:200])
# print(docs[1].metadata)
print(set(document.metadata["category"] for document in docs))