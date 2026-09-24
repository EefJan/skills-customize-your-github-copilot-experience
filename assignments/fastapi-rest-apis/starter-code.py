from fastapi import FastAPI

app = FastAPI(title="Inventory API")

items = [
    {"id": 1, "name": "Keyboard", "price": 49.99, "description": "Mechanical keyboard"},
    {"id": 2, "name": "Mouse", "price": 24.99, "description": "Wireless mouse"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory API"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"message": "Item not found"}


# TODO: Add POST endpoint to create a new item
# TODO: Add PUT endpoint to update an existing item
# TODO: Add DELETE endpoint to remove an item
