from openai import OpenAI

from config import OPENAI_API_KEY
from models import LLMRequest, LogAnalysis


client = OpenAI(api_key=OPENAI_API_KEY)


def ask_llm(request: LLMRequest) -> LogAnalysis:
    """Analyze infrastructure logs and return a validated result."""

    response = client.responses.parse(
        model="gpt-5.6",
        instructions=request.instructions,
        input=request.input,
        text_format=LogAnalysis,
    )

    result = response.output_parsed

    if result is None:
        raise RuntimeError("The model did not return a structured log analysis.")

    return result