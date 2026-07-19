from llm import ask_llm


def main() -> None:
    sample_logs = """
    Warning  BackOff  kubelet
    Back-off restarting failed container api-server.

    Container exited with code 1.
    Error: connection refused while connecting to MongoDB on port 27017.
    """

    response = ask_llm(sample_logs)
    print(response)


if __name__ == "__main__":
    main()