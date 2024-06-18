import sys
from pipeline import create_qa_chain
from transcription import transcribe_video, split_transcription
from store import get_retriever, create_pinecone_store
from utils.openai_api import connect_openai

def main(youtube_url):

    transcription, transcription_file = transcribe_video(youtube_url)
    transcription_chunks = split_transcription(transcription_file)
    pinecone_store = create_pinecone_store(transcription_chunks)

    print("Talk with...",transcription_file)
    print("(type 'quit' to exit)")

    while True:
        query = input("Question: ")
        if query.lower() == 'quit':
                    break

        retriever = get_retriever(pinecone_store)
        relevant_chunks = retriever.invoke(query)
        context = relevant_chunks

        qa_chain = create_qa_chain()
        qa_answer = qa_chain.invoke({
            "context": context,
            "question": query
        })
        print("Answer:", qa_answer)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <YouTube_URL>")
        sys.exit(1)

    main(sys.argv[1])