from pathlib import Path
from scripts.document_manager import DocumentManager
from scripts.embedding_manager import EmbeddingManager
from scripts.credential import load_llm_env_key
from src.data_preprocessing import PROCESSED_DATA_FOLDER




if __name__ == "__main__":
    load_llm_env_key()
    document_manager = DocumentManager(directory_path=PROCESSED_DATA_FOLDER)
    document_chunk = document_manager.split_documents()
    
    embedding_manager = EmbeddingManager(chunks= document_chunk)
    embedding_manager.create_and_persist_embeddings()
    embedding_manager.get_vectordb().get()