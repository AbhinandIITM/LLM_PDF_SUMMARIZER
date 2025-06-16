import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama

# 1. Load PDFs
def load_pdfs_from_folder(folder_path: str):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            print(f"Loading {filename}...")
            loader = PyPDFLoader(full_path)
            documents.extend(loader.load())
    return documents

# 2. Chunk
def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

# 3. Embed & store
def create_vector_store(chunks, persist_dir="chroma_db"):
    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=persist_dir)
    return db

# 4. Chain
def create_qa_chain(db, llm):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return ConversationalRetrievalChain.from_llm(llm=llm, retriever=db.as_retriever(), memory=memory)

# 🧠 Main
if __name__ == "__main__":
    docs = load_pdfs_from_folder("documents")
    chunks = split_documents(docs)
    db = create_vector_store(chunks)

    # 🧠 Use local Ollama model (e.g., llama3)
    llm = Ollama(model="llama3.1:8b")
    qa_chain = create_qa_chain(db, llm)

    print("💬 Ask me anything about your documents. Type 'exit' to stop.")

    while True:
        query = input("\nYou: ")
        if query.lower() in ("exit", "quit"):
            break
        result = qa_chain.invoke({"question": query})
        print("Assistant:", result["answer"])
