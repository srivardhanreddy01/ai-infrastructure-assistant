from openai import OpenAI
import json

from config import OPENAI_API_KEY
from models import LLMRequest, LogAnalysis
from tools import count_errors, COUNT_ERRORS_TOOL


client = OpenAI(api_key=OPENAI_API_KEY)

def execute_tool(name: str, arguments: dict) -> str:
    """Route an approved tool call to its Python implementation."""

    if name=="count_errors":
        return str(count_errors(**arguments))
    
    raise ValueError(f"Unknown tool requested: {name}")

def ask_llm(request: LLMRequest) -> LogAnalysis:
    """Analyze infrastructure logs and return a validated result."""

    input_items = [
        {
            "role": "user",
            "content": request.input,
        }
    ]

    first_response = client.responses.parse(
        model="gpt-5.6",
        instructions=request.instructions,
        input=input_items,
        tools=[COUNT_ERRORS_TOOL],
        tool_choice="auto",
    )

    input_items.extend(first_response.output)

    for item in first_response.output:
        if item.type != "function_call":
            continue

        arguments = json.loads(item.arguments)
        tool_result = execute_tool(item.name, arguments)
        input_items.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": tool_result,
            }
        )

    final_response = client.responses.parse(
        model="gpt-5.6",
        instructions=request.instructions,
        input=input_items,
        tools=[COUNT_ERRORS_TOOL],
        text_format=LogAnalysis,
    )

    result = final_response.output_parsed

    if result is None:
        raise RuntimeError(
            "The model did not return a structured log analysis."
        )

    return result