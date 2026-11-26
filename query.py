#Import the ChromaDB library for database operations

import chromadb; 

# create a client instance to connect to the ChromaDB database
client = chromadb.Client()

# create a collection named "vehicles" in the database
collection = client.create_collection(name="vehicles")

print("Collection 'vehicles' created successfully.", collection.name)

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

# Query the "vehicles" collection to retrieve all documents
results = collection.query(
    # query_texts = ["What vehicles run on the road?"],
    query_texts = ["Which vehicle helps me travel on water?"],
    n_results = 2
)

# Print the query results
print("Query Results:", results)