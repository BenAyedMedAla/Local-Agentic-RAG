from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(text: str):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=50)
    chunks = text_splitter.split_documents([{"content": text}])
    return chunks