from dapr_agents import AgentActor, OpenAIChatClient, OpenAPIReActAgent
from dapr_agents.tool.utils import OpenAPISpecParser
from dapr_agents.document.embedder import SentenceTransformerEmbedder
from dapr_agents.storage import ChromaVectorStore
from dotenv import load_dotenv
import asyncio
import logging
import os


async def main():
    try:
        #llm = OpenAIChatClient(
        #    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        #    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        #    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        #    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        #)

        spec_parser = OpenAPISpecParser.from_url("http://127.0.0.1:8000/openapi.json")
        embedding_function = SentenceTransformerEmbedder(model="all-MiniLM-L6-v2", cache_dir=".model")
        api_vector_store = ChromaVectorStore(
            name="api_toolbox",
            embedding_function=embedding_function,
            persistent=False
        )

        # Define Agent
        calculator_agent = OpenAPIReActAgent(
            #llm=llm,
            role="Calculator API Assistant",
            instructions=[
                "You are a helpful assistant that can perform calculations by calling REST API endpoints.",
            ],
            name="CalculatorOpenAPIReActAgent",
            spec_parser=spec_parser,
            api_vector_store=api_vector_store,
        )

        # Expose Agent as an Actor over a Service
        calculator_actor = AgentActor(
            agent=calculator_agent,
            message_bus_name="pubsub",
            agents_registry_store_name="agentstatestore",
            agents_registry_key="agents_registry",
            service_port=8003,
        )

        await calculator_actor.start()
    except Exception as e:
        print(f"Error starting actor: {e}")


if __name__ == "__main__":
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
