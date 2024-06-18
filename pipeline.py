from langchain_core.output_parsers import StrOutputParser
from utils.openai_api import client_openai as model
from langchain.prompts import ChatPromptTemplate

parser = StrOutputParser()

def create_qa_prompt():
    template = """
    Answer the question based on the context below. If you can't
    answer the question, reply "I don't know".

    Context: {context}

    Question: {question}
    """
    return ChatPromptTemplate.from_template(template)


def create_qa_chain():
    prompt = create_qa_prompt()
    return prompt | model | parser


