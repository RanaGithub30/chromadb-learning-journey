import chromadb

# connect to chroma with persistent storage
client = chromadb.PersistentClient(path="./chroma_db")

# create or reuse a collection
collection = client.get_or_create_collection("vehicles")
