from tools import count_errors

def test_count_errors() -> None:
    logs = """
    ERROR Failed to connect
    INFO Application started
    error Request timed out
    WARNING Retrying
    """

    assert count_errors(logs) == 2

def test_count_errors_ignores_substrings() -> None:
    logs = """
    terror
    errors
    INFO Application started
    """

    assert count_errors(logs) == 0

def test_count_errors_empty_input() -> None:
    assert count_errors("") == 0