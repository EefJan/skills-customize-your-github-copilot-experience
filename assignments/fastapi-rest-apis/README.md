# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that exposes data through clean endpoints, validates input, and demonstrates how HTTP methods work in a modern Python web framework.

## 📝 Tasks

### 🛠️ Create the API App

#### Description
Set up a FastAPI application that serves a basic collection of items and exposes endpoints for retrieving, creating, and updating them.

#### Requirements
Completed program should:

- Import and configure a FastAPI app.
- Define a root endpoint that returns a welcome message.
- Create an endpoint to list all items.
- Create an endpoint to retrieve a single item by ID.
- Use a simple in-memory list or dictionary to store sample data.

### 🛠️ Add CRUD Endpoints

#### Description
Implement Create, Read, Update, and Delete operations for your API using standard HTTP methods.

#### Requirements
Completed program should:

- Use `GET` for retrieving items.
- Use `POST` to add a new item.
- Use `PUT` to update an existing item.
- Use `DELETE` to remove an item.
- Return JSON responses with clear field names and status codes.

### 🛠️ Validate Request Data

#### Description
Improve the API by validating incoming request data and creating a cleaner data model.

#### Requirements
Completed program should:

- Define a Pydantic model for item data.
- Require fields such as `id`, `name`, and `price` or `description`.
- Reject invalid payloads with useful validation errors.
- Example payload:

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "description": "Portable computer"
}
```

### 🛠️ Run and Test the API

#### Description
Start the FastAPI app and verify the endpoints work as expected using a local development server.

#### Requirements
Completed program should:

- Run the app with Uvicorn.
- Open the `/docs` Swagger UI page.
- Test at least three endpoints manually.
- Confirm that the API returns JSON and proper HTTP status codes.

```bash
uvicorn main:app --reload
```
