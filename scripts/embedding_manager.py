from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from os import path
from shutil import rmtree


class EmbeddingManager:
    def __init__(self, chunks: Document = None, persist_directory="db", embedding=None):
        self.chunks = chunks
        self.persist_directory = persist_directory
        self.vectordb = None
        self.embedding = (
            GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
            if embedding
            else embedding
        )

    def get_retriever(self):
        self.vectordb = Chroma(
            persist_directory=self.persist_directory, embedding_function=self.embedding
        )
        retriever = self.vectordb.as_retriever(
            search_type="mmr", search_kwargs={"k": 6, "lambda_mult": 0.25}
        )
        return retriever

    # Method to create and persist embeddings
    def create_and_persist_embeddings(self):
        if path.exists(self.persist_directory):
            rmtree(self.persist_directory)
        # Creating an instance of OpenAIEmbeddings
        # Creating an instance of Chroma with the sections and the embeddings
        self.vectordb = Chroma.from_documents(
            documents=self.chunks,
            embedding=self.embedding,
            persist_directory=self.persist_directory,
        )
