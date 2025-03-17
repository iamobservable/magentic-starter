import asyncio

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import MagenticOneGroupChat
from autogen_agentchat.ui import Console

from src.anthropic import model_client


async def main() -> None:
    assistant = AssistantAgent(
        "Assistant",
        model_client=model_client,
    )
    team = MagenticOneGroupChat([assistant], model_client=model_client)
    await Console(
        team.run_stream(task="Provide an alternative option to the meaning of life")
    )


if __name__ == "__main__":
    asyncio.run(main())
