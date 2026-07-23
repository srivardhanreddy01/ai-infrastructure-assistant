import re


COUNT_ERRORS_TOOL = {
    "type": "function",
    "name": "count_errors",
    "description": (
        "Count the number of log lines containing the standalone "
        "word 'error', case-insensitively."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "log_text": {
                "type": "string",
                "description": "The infrastructure log text to inspect.",
            }
        },
        "required": ["log_text"],
        "additionalProperties": False,
    },
    "strict": True,
}


def count_errors(log_text: str) -> int:
    """Count lines containing the standalone word 'error'."""

    return sum(
        1
        for line in log_text.splitlines()
        if re.search(r"\berror\b", line, re.IGNORECASE)
    )