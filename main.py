from dotenv import load_dotenv
load_dotenv()
from agno.models.groq import Groq
import asyncio
from agno.tools.mcp import MCPTools
from agno.utils.pprint import apprint_run_response
from agno.agent import Agent
async def run_agent(message: str) -> None:
    async with MCPTools(
        "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"
    ) as mcp_tools:
        agent = Agent(
            model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
            tools=[mcp_tools],
            markdown=True,
        )

        response_stream = await agent.arun(message, stream=True)
        await apprint_run_response(response_stream, markdown=True)
if __name__ == "__main__":
    asyncio.run(
        run_agent(
            "What listings are available in Hyderabad for 2 people for 2 nights from 1 to 4 June 2025?.Also give me the hotel name and the price and the location of the hotel and rating of the hotel in tabular format.Also give the contact number of the hotel and the exact address of the hotel."
        )
    )