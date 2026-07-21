from llm import ask_llm
from prompts import build_log_analysis_prompt

def main() -> None:
    file_content=""
    try:
        with open("logs/mongodb_connection.log", "r") as file:
            file_content = file.read()
    except:
        print("An error occurred! Unable to open the file")
    
    request = build_log_analysis_prompt(file_content)

    response = ask_llm(request)
    print(response)


if __name__ == "__main__":
    main()