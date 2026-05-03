import asyncio
from typing import Dict, List


# Collection of materials
materials: Dict[int, Dict[str, object]] = {
    701: {
        "id": 701,
        "title": "Mastering Python Quickly",
        "author": "Daniel Smith",
        "category": "Programming",
        "available": True
    },
    702: {
        "id": 702,
        "title": "Intro to Computer Networks",
        "author": "Linda Green",
        "category": "Networking",
        "available": True
    }
}


# Users database
users: Dict[int, Dict[str, object]] = {}

# Logs storage
logs: List[Dict[str, object]] = []


# Add a new user
async def add_user(user_id: int, name: str, email: str, membership: str) -> str:
    print(f"Adding user {name}...")

    await asyncio.sleep(5)

    users[user_id] = {
        "id": user_id,
        "name": name,
        "email": email,
        "membership": membership
    }

    return f"User added successfully! ID = {user_id}"


# Display users
async def get_users() -> List[Dict[str, object]]:
    print("Retrieving users...")

    await asyncio.sleep(3)

    return list(users.values())


# Update material details
async def update_material(material_id: int, new_title: str = None, new_author: str = None) -> str:
    print(f"Updating material {material_id}...")

    await asyncio.sleep(4)

    material = materials.get(material_id)

    if material is None:
        return "Material not found"

    if new_title:
        material["title"] = new_title

    if new_author:
        material["author"] = new_author

    return f"Material {material_id} updated successfully"


# Retrieve logs
async def get_logs() -> List[Dict[str, object]]:
    print("Loading logs...")

    await asyncio.sleep(3)

    return logs


# Run concurrent operations
async def runner() -> None:
    print("Task A initiated (Add User)")
    print("Task B initiated (Update Material)")
    print("Task C initiated (Retrieve Logs)")

    results = await asyncio.gather(
        add_user(10, "John Doe", "john@example.com", "standard"),
        update_material(701, new_title="Python Basics Guide"),
        get_logs()
    )

    print("\n=== ALL TASKS FINISHED ===")

    print("\n=== OUTPUT ===")
    for item in results:
        print(item)


asyncio.run(runner())
