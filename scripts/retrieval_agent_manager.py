from typing import Dict, Optional, TypedDict, List
from loguru import logger

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langgraph.graph import START, StateGraph
from persona.customer_service import persona_customer_service
from scripts.credential import GEMINI_API_KEY

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


class RetrievalAgentManager:
    def __init__(
        self,
        vectordb: Chroma,
        llm=None,
        llm_config: Optional[Dict] = None,
        custom_prompt: Optional[str] = None,
    ):
        self.vectordb = vectordb
        self.llm_config = llm_config or {
            "temperature": 0.5,
            "max_tokens": 2048,
            "top_p": 0.95,
            "top_k": 40,
        }

        self.llm = llm or ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=self.llm_config.get("temperature"),
            max_tokens=self.llm_config.get("max_tokens"),
            top_p=self.llm_config.get("top_p"),
            top_k=self.llm_config.get("top_k"),
            google_api_key = GEMINI_API_KEY
        )
        self.persona = custom_prompt or persona_customer_service
        self.prompt = PromptTemplate(
            input_variables=["question", "context"],
            template = (f"{self.persona}"
            "Question: {question}"
            "Context: (context)"
            "Answer:")
        ) 

    def retrieve(self, state: State):
        """Retrieve information related to a query."""
        retrieved_docs = self.vectordb.similarity_search(state["question"], k=11)

        return {"context": retrieved_docs}

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.prompt.format(
            question=state["question"], context=docs_content
        )
        response = self.llm.invoke(messages)
        return {"answer": response.content}

    def control_flow(self):
        graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        graph_builder.add_edge(START, "retrieve")
        graph = graph_builder.compile()
        return graph

    def generate_message(self, query):
        graph = self.control_flow()
        logger.info("Generate message")
        response = graph.invoke({"question": query})
        logger.success(response)
        
        return response["answer"]
