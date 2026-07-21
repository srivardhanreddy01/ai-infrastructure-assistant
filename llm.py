from openai import OpenAI
from config import OPENAI_API_KEY
from models import LLMRequest

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(request: LLMRequest) -> str:
    """Send infrastructure logs to the model for analysis."""

    response = client.responses.create(
        model="gpt-5.6",
        instructions=request.instructions,
        input=request.input,
    )

    return response.output_text