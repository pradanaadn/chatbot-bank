from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from scripts.credential import GEMINI_API_KEY
from loguru import logger
from os import path
from shutil import rmtree


class EmbeddingManager:
    def __init__(
        self, chunks: list[Document] = None, persist_directory="chroma_langchain_db", embedding=None
    ):
        self.chunks = chunks
        self.persist_directory = persist_directory
        self.vectordb = None
        self.embedding = embedding or GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004", google_api_key=GEMINI_API_KEY
        )

    def get_vectordb(self, **kwargs):
        logger.info("Trying load the vectordb")
        self.vectordb = Chroma(
            persist_directory=self.persist_directory, embedding_function=self.embedding
        )
        logger.success("Success load vectordb")
        return self.vectordb

    # Method to create and persist embeddings
    def create_and_persist_embeddings(self):
        try:
            if path.exists(self.persist_directory):
                logger.info("Remove existent persist chroma db directory")
                rmtree(self.persist_directory)
                logger.success("Success remove existent persist chroma db directory")

            logger.info(
                "Creating an instance of Chroma with the sections and the embeddings"
            )
            self.vectordb = Chroma(
                collection_name="chatbot_bank_service",
                embedding_function=self.embedding,
                persist_directory=self.persist_directory,  # Where to save data locally, remove if not necessary
            )
            logger.success(
                "Success creating an instance of Chroma with the sections and the embeddings"
            )
            logger.info("Adding document to vectordb")
            logger.info(self.chunks[0])
            self.vectordb.add_documents(self.chunks)
            logger.success("Success adding document to vectordb")

        except Exception as e:
            logger.exception(e)
