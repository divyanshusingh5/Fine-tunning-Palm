from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

api_key="AIzaSyDGf9gyCmw3dKLzg49DIpIu-mMJN9AyGYQ"

llm=GooglePalm(google_api_key=api_key,temperature=0.5)



loader = CSVLoader(file_path='UropData.csv', encoding='utf-8', source_column='dialogue')
data = loader.load()

instructor_embeddings=HuggingFaceInstructEmbeddings()
vectordb_file_path=r"D:\\Desktop\\Finetune_Palm_Summary\\faiss_index"


def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate a summmary of the text n based on this context only.
    In the answer try to provide as much text as possible from "Summary" section in the source document with some changes .
    If the answer is not found try to give Simple Summary of text .

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain

if __name__ == "__main__":
    chain=get_qa_chain()

    print(chain('''I am having Head ace what i should do ?'''))





