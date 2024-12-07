from pathlib import Path
from scripts.document_manager import DocumentManager
from scripts.embedding_manager import EmbeddingManager
from src.data_preprocessing import PROCESSED_DATA_FOLDER




if __name__ == "__main__":
    document_manager = DocumentManager(directory_path=PROCESSED_DATA_FOLDER)
    document_manager.load_documents()
    document_manager.split_documents()
    
    embedding_manager = EmbeddingManager(chunks= document_manager.all_sections)
    embedding_manager.create_and_persist_embeddings()
