from app.services.vehicle_service import (
    add_vehicle,
    get_vehicles,
    update_vehicle,
    delete_vehicle,
    search_vehicle,
    view_metadatas,
    update_all_vehicles
)

from app.data.vehicles import (
    documents, 
    ids, 
    metadatas
)

# CREATE
add_vehicle(
    documents = documents,
    ids = ids,
    metadatas = metadatas
)

# READ
data = get_vehicles()
print("All Vehicles:", data)

# UPDATE
update_vehicle(
    vehicle_id="car",
    document="car runs on highway"
)

# SEARCH
results = search_vehicle("vehicles that travel on water")
print("Search Results:", results)

# DELETE
delete_vehicle("boat")

# UPDATE ALL
update_all_vehicles(
    documents = documents,
    ids = ids,
    metadatas = metadatas
)   

# VIEW METADATAS
metadatas = view_metadatas()
print("Metadatas:", metadatas)