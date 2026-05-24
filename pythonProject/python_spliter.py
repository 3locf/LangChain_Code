from langchain_text_splitters import PythonCodeTextSplitter

# 字符串⽂档
PYTHON_CODE = """
    def hello_world():
    print("Hello, World!")
    
    def hello_python():
    print("Hello, Python!")
    
    class MyClass:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, {self.name}!")
    """

splitter = PythonCodeTextSplitter(chunk_size=100, chunk_overlap=20)

docs = splitter.create_documents([PYTHON_CODE])

for doc in docs:
    print("*" * 30)
    print(doc.page_content)
    print(doc.metadata)