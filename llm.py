from openai import OpenAI

from config import OPENAI_API_KEY
from prompts import LOG_ANALYSIS_INSTRUCTIONS


client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(log_text: str) -> str:
    """Send infrastructure logs to the model for analysis."""

    response = client.responses.create(
        model="gpt-5.6",
        instructions=LOG_ANALYSIS_INSTRUCTIONS,
        input=log_text,
    )

    return response.output_text