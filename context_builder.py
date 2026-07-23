from models import LLMRequest


SYSTEM_PROMPT = """
You are a Senior Site Reliability Engineer.

Analyze the provided infrastructure logs.

Use the count_errors tool when an exact error-line count is relevant.
Do not estimate counts manually when the tool is available.

Return a structured analysis containing:
- root cause
- severity
- confidence
- recommendation
- summary
"""

def build_log_analysis_prompt(log_text: str) -> LLMRequest:
    return LLMRequest(
        instructions=SYSTEM_PROMPT,
        input=log_text,
    )