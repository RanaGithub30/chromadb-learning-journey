from app.services.vehicle_service import (
    add_vehicle,
    get_vehicles,
    update_vehicle,
    delete_vehicle,
    search_vehicle,
    view_metadatas,
    update_all_vehicles
)

# CREATE
add_vehicle(
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
    ],
    metadatas=[
        {"type": "public_transportation", "capacity": 5, "fuel": "diesel" },
        {"type": "personal", "capacity": 2, "fuel": "petrol" },
        {"type": "water_transportation", "capacity": 10, "fuel": "diesel" },
        {"type": "air_transportation", "capacity": 100, "fuel": "gasoline" },
        {"type": "public_transportation", "capacity": 50, "fuel": "diesel" },
    ]
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
    documents=[
        "car runs on highway",
        "bike runs on road",
        "boat runs on water",
        "plane flies in the sky",
        "bus runs on road"
    ],
    ids=[
        "car",
        "bike",
        "boat",
        "plane",
        "bus"
    ],
    metadatas=[
        {"type": "public_transportation", "capacity": 5, "fuel": "diesel" },
        {"type": "personal", "capacity": 2, "fuel": "petrol" },
        {"type": "water_transportation", "capacity": 10, "fuel": "diesel" },
        {"type": "air_transportation", "capacity": 100, "fuel": "gasoline" },
        {"type": "public_transportation", "capacity": 50, "fuel": "diesel" },
    ]
)   

# VIEW METADATAS
metadatas = view_metadatas()
print("Metadatas:", metadatas)