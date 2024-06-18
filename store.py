from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


def get_retriever(pinecone_store):
    return pinecone_store.as_retriever()

def create_pinecone_store(documents):
    print("Creating Pinecone store...")
    embeddings = OpenAIEmbeddings()
    index_name = "ytrag"
    pinecone_store = PineconeVectorStore.from_documents(
        documents, embedding=embeddings, index_name=index_name)

    print("Pinecone store created.")

    return pinecone_store