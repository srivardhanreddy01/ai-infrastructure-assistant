from textwrap import dedent

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


def build_log_analysis_request(
    log_text: str,
    retrieved_docs: list[str],
) -> LLMRequest:
    knowledge = "\n\n---\n\n".join(
        f"""
    Source: {chunk.source}
    Similarity: {chunk.similarity_score:.3f}

    {chunk.text}
    """.strip()
        for chunk in retrieved_docs
    )

    user_input = dedent(
        f"""
        Use the retrieved documentation when it is relevant.
        Do not assume the documentation is always correct for the current incident.

        RETRIEVED KNOWLEDGE:
        {knowledge or "No relevant documentation was found."}

        LOGS:
        {log_text}
        """
    ).strip()

    return LLMRequest(
        instructions=SYSTEM_PROMPT.strip(),
        input=user_input,
    )