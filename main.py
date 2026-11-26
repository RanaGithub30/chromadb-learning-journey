import os

import chromadb
from dotenv import load_dotenv


COLLECTION_NAME = "getting-started"
DOCUMENTS = [
    "Chroma is a vector database for AI applications.",
    "Vector search retrieves text by semantic similarity.",
    "Python is commonly used to build machine learning applications.",
]
IDS = ["doc-1", "doc-2", "doc-3"]
QUERY = "Which database can find semantically similar text?"


def main() -> None:
    load_dotenv()

    required_variables = ("CHROMA_API_KEY", "CHROMA_TENANT", "CHROMA_DATABASE")
    missing_variables = [
        variable for variable in required_variables if not os.getenv(variable)
    ]
    if missing_variables:
        raise RuntimeError(
            "Missing Chroma Cloud configuration: "
            + ", ".join(missing_variables)
            + ". Run `chroma login`, then "
            "`chroma db connect chroma-getting-started --env-file`."
        )

    client = chromadb.CloudClient(
        api_key=os.getenv("CHROMA_API_KEY"),
        tenant=os.getenv("CHROMA_TENANT"),
        database=os.getenv("CHROMA_DATABASE"),
    )
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    collection.upsert(ids=IDS, documents=DOCUMENTS)
    results = collection.query(query_texts=[QUERY], n_results=2)

    print("Ingested data:")
    for document_id, document in zip(IDS, DOCUMENTS):
        print(f"- {document_id}: {document}")

    print(f"\nQuery: {QUERY}")
    print("Results:")
    for document, distance in zip(
        results["documents"][0], results["distances"][0]
    ):
        print(f"- {document} (distance: {distance:.4f})")


if __name__ == "__main__":
    main()
