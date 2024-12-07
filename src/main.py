from scripts.retrieval_agent_manager import RetrievalAgentManager
from scripts.embedding_manager import EmbeddingManager

async def main():
    # Initialize vector database (replace with your implementation)
    vector_db = EmbeddingManager().get_retriever()  # Replace with actual vector database
    
    # Configure the retrieval agent
    agent_config = {
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 0.95,
        "top_k": 40,
    }
    
    # Create the agent
    agent = RetrievalAgentManager(
        vector_db=vector_db,
        llm_config=agent_config
    )
    
    # Example conversation
    question = "Apa itu BNI Life?"
    agent.query(question)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())