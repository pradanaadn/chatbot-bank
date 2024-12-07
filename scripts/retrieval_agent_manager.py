from typing import Dict, List, Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackManager
from langchain.prompts import PromptTemplate, ChatPromptTemplate

from persona.customer_service import persona_customer_service

class RetrievalAgentManager:
    def __init__(
        self,
        vector_db,
        llm=None,
        llm_config: Optional[Dict] = None,
        custom_prompt: Optional[str] = None,
    ):
        self.vectordb = vector_db
        self.llm_config = llm_config or {
            "temperature": 0.7,
            "max_tokens": 1024,
            "top_p": 0.95,
            "top_k": 40,
        }

        self.llm = llm or ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=self.llm_config.get("temperature"),
            max_tokens=self.llm_config.get("max_tokens"),
            top_p=self.llm_config.get("top_p"),
            top_k=self.llm_config.get("top_k"),
            
        )
        self.persona = custom_prompt or persona_customer_service

    def query(self, query_text:str):
        results = self.vectordb.similarity_search_with_relevance_scores(query_text, k=4)
        context_text = "\n\n - -\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(self.persona)
        prompt = prompt_template.format(context=context_text, question=query_text)  
        for chunk in self.llm.stream(prompt):
            print(chunk.content)