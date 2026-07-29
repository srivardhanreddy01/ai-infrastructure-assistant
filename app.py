from llm import ask_llm
from context_builder import build_log_analysis_request
from retriever import retrieve

def main() -> None:
    try:
        with open(
            "logs/mongodb_connection.log",
            "r",
            encoding="utf-8",
        ) as file:
            file_content = file.read()
    except OSError as exc:
        print(f"Unable to open the log file: {exc}")
        return

    relevant_docs = retrieve(file_content)
    request = build_log_analysis_request(
    log_text=file_content,
    retrieved_docs=relevant_docs,
    )
    response = ask_llm(request)

    print(f"Root cause: {response.root_cause}")
    print(f"Severity: {response.severity.value}")
    print(f"Confidence: {response.confidence:.0%}")
    print(f"Recommendation: {response.recommendation}")
    print(f"Summary: {response.summary}")


if __name__ == "__main__":
    main()