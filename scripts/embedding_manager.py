from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from os import path
from shutil import rmtree



class EmbeddingManager:
    def __init__(self, chunks: Document, persist_directory = "db"):
        self.chunks = chunks
        self.persist_directory = persist_directory
        self.vectordb = None
    # Method to create and persist embeddings
    def create_and_persist_embeddings(self):
        if path.exists(self.persist_directory):
            rmtree(self.persist_directory)
        # Creating an instance of OpenAIEmbeddings
        embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        # Creating an instance of Chroma with the sections and the embeddings
        self.vectordb = Chroma.from_documents(
            documents=self.chunks, embedding=embedding, persist_directory=self.persist_directory
        )
