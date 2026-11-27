from app.services.vehicle_service import (
    add_vehicle,
    get_vehicles,
    update_vehicle,
    delete_vehicle,
    search_vehicle
)

# CREATE
add_vehicle(
    documents=["car runs on road", "boat runs on water"],
    ids=["car", "boat"]
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