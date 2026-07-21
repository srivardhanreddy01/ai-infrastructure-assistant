from models import LLMRequest


SYSTEM_PROMPT = """
You are a Senior Site Reliability Engineer.

Analyze the provided infrastructure logs.

Return:
- Root Cause
- Severity
- Recommendation

Clearly distinguish confirmed observations from assumptions.
"""


def build_log_analysis_prompt(log_text: str) -> LLMRequest:
    return LLMRequest(
        instructions=SYSTEM_PROMPT,
        input=log_text,
    )