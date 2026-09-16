import json
from pydantic import ValidationError
from pathlib import Path

from models import RetrievalEvaluationCase, RetrievedChunk
from retriever import retrieve

BASE_DIR = Path(__file__).resolve().parent

def load_evaluation_cases() -> list[RetrievalEvaluationCase]:
    cases_path = BASE_DIR / "retrieval_cases.json"
    
    with cases_path.open("r", encoding="utf-8") as file:
        raw_cases = json.load(file)

    return [
        RetrievalEvaluationCase.model_validate(case)
        for case in raw_cases
    ]

def recall_at_k(
    relevant_chunk_ids: list[str],
    retrieved_chunk_ids: list[str],
    k: int,
) -> float:

    if k <= 0:
        raise ValueError("k must be greater than 0.")

    if not relevant_chunk_ids:
        raise ValueError("Relevant chunk IDs must not be empty.")

    relevant = set(relevant_chunk_ids)
    retrieved_at_k = set(retrieved_chunk_ids[:k])

    relevant_retrieved = relevant & retrieved_at_k

    return len(relevant_retrieved) / len(relevant)

def precision_at_k(
    relevant_chunk_ids: list[str],
    retrieved_chunk_ids: list[str],
    k: int,
) -> float:

    if k <= 0:
        raise ValueError("k must be greater than 0.")

    if not relevant_chunk_ids:
        raise ValueError("Relevant chunk IDs must not be empty.")

    relevant = set(relevant_chunk_ids)
    retrieved_at_k = set(retrieved_chunk_ids[:k])

    if not retrieved_at_k:
        return 0.0

    relevant_retrieved = relevant & retrieved_at_k

    return len(relevant_retrieved) / len(retrieved_at_k)

def evaluate_retrieval(k) -> None:
    evaluation_cases:list[RetrievalEvaluationCase]  = load_evaluation_cases()
    retrieved_chunk: list[RetrievedChunk] = []
    sum_precision = 0 
    sum_recall = 0 
    num_cases = len(evaluation_cases)
    for case in evaluation_cases:
        relevant_chunk_ids= case.relevant_chunk_ids
        retrieved_chunks = retrieve(query = case.query, top_k= k , minimum_similarity= None)
        retrieved_chunk_ids = []
        retrieved_chunk_ids = [chunk.chunk_id for chunk in retrieved_chunks]
        case_precison = precision_at_k(relevant_chunk_ids, retrieved_chunk_ids, k)
        case_recall = recall_at_k(relevant_chunk_ids, retrieved_chunk_ids, k)
        print("Query: "+ case.query)
        print("Expected: "+ ", ".join(relevant_chunk_ids) )
        print("Retrieved: "+ ", ".join(retrieved_chunk_ids) )

        print("Recall@"+str(k)+" "+str(case_recall))
        print("Precision@"+str(k)+" "+str(case_precison))

        sum_precision += case_precison    
        sum_recall += case_recall
    print("Overall")
    print("Recall@"+str(k)+" "+str(sum_recall/num_cases))
    print("Precision@"+str(k)+" "+str(sum_precision/num_cases))

if __name__ == "__main__":
    evaluate_retrieval(3)