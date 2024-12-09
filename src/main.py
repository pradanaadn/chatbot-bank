from scripts.retrieval_agent_manager import RetrievalAgentManager
from scripts.embedding_manager import EmbeddingManager
from scripts.credential import load_llm_env_key
async def main():
    load_llm_env_key()
    # Initialize vector database (replace with your implementation)
    vector_db = EmbeddingManager().get_vectordb()  # Replace with actual vector database
    
    # Configure the retrieval agent
    
    
    # Create the agent
    agent = RetrievalAgentManager(
        vectordb=vector_db,
    )
    
    # Example conversation
    question = "Apa itu BNI Life?"
    agent.generate_message(question)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())