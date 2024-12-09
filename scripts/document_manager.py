from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentManager:
    def __init__(self, directory_path, glob_pattern="./*.md"):
        self.directory_path = directory_path
        self.glob_pattern = glob_pattern
        self.documents = None
        
       
    
    def load_documents(self):
        loader = DirectoryLoader(self.directory_path, glob=self.glob_pattern, show_progress=True, loader_cls=UnstructuredMarkdownLoader)
        self.documents = loader.load()
        

    def split_documents(self, chunk_size=1000,chunk_overlap=500):
        self.load_documents()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = text_splitter.split_documents(self.documents)
        return chunks