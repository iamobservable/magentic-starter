import os

from autogen_ext.models.anthropic import AnthropicChatCompletionClient

model_client = AnthropicChatCompletionClient(
    model=os.getenv("ANTHROPIC_MODEL"),
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)
