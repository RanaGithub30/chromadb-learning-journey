from app.config.chroma_config import collection

# the def keyword is used to define a reusable block of code called a function. Functions allow you to organize code, avoid repetition, accept input data, and return results

#CREATE

def add_vehicle(documents, ids, metadatas=None):
    collection.add(documents=documents, ids=ids, metadatas=metadatas)

# READ
def get_vehicles():
    return collection.get()

# UPDATE
def update_vehicle(vehicle_id, document):
    collection.update(ids=vehicle_id, documents=document)

# DELETE
def delete_vehicle(vehicle_id):
    collection.delete(ids=vehicle_id)

# SEARCH
def search_vehicle(query):
    return collection.query(query_texts=[query])

# VIEW METADATAS
def view_metadatas():
    return collection.get(include=["documents", "metadatas"])

# UPDATE ALL
def update_all_vehicles(documents, ids, metadatas=None):
    collection.update(documents=documents, ids=ids, metadatas=metadatas)