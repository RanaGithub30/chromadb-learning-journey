import chromadb;

# connect to chroma with persistent storage
client = chromadb.PersistentClient(path="./chroma_db")

# create or reuse a collection
collection = client.get_or_create_collection("vehicles")

# Print the collection name
print("Collection Stored", collection.name)

# Add a document to the "vehicles" collection
collection.add(
    documents = [
        "car runs on road",
        "bike runs on road",
        "boat runs on water",
        "plane flies in the sky",
        "bus runs on road"
    ],
    ids = [
        "car",
        "bike",
        "boat",
        "plane",
        "bus"
    ]
)

# Show data in collection
data = collection.get()
print("Data in Collection:", data)

for i, doc in zip(data['documents'], data['ids']):
    print(f"Document ID: {doc}, Document Text: {i}")
