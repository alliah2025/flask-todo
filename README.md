# Flask Todo App with REST API

This project enhances a simple Flask-based Todo web application by adding a full-featured REST API. The API enables external systems to create, read, update, and delete todo items programmatically, following RESTful principles.

## 📌 Original Application

The original application is a basic Todo list manager built with Flask and SQLite. It supports:

- Viewing all tasks
- Adding new tasks
- Updating tasks (marking them as complete/incomplete)
- Deleting tasks

All actions were handled through HTML forms in the web interface.

## ✨ Enhancements Made

This version introduces a REST API layer that exposes the core functionality through JSON-based HTTP endpoints. Key improvements include:

- Added full CRUD API endpoints under `/api/todos`
- Returns proper HTTP status codes (200, 201, 400, 404, etc.)
- Includes input validation and error handling
- SQLite database for local storage
- Easy to test with Postman or similar tools
- Developed a dedicated test suite using `pytest` with 100% test coverage

## 📁 Project Structure

```
📦 flask-todo
┣ 📜 app.py
┣ 📜 app_withRESTAPI.py
┣ 📜 templates/
┃ ┗ 📜 index.html
┣ 📜 test_app.py
┗ 📜 README.md
```

> All enhancements are done inside the `feature/rest-api` branch.

---

## 📋 API Documentation

### `GET /api/todos`

Fetches all todo items.

- **Response**: `200 OK`
```json
[
  {
    "id": 1,
    "title": "Buy milk",
    "description": "2 bottles",
    "done": false
  }
]
```

### `POST /api/todos`

Creates a new todo item.

- **Request JSON**:
```json
{
  "title": "Read book",
  "description": "Chapter 4",
  "done": false
}
```
- **Response**: `201 Created` with new task JSON  
- **Error**: `400 Bad Request` if title is missing

### `PUT /api/todos/<id>`

Updates a specific todo item.

- **Request JSON**:
```json
{
  "title": "Finish report",
  "done": true
}
```
- **Response**: `200 OK` with updated task  
- **Error**: `404 Not Found` if the task does not exist

### `DELETE /api/todos/<id>`

Deletes a specific todo item.

- **Response**: `200 OK` with confirmation message  
- **Error**: `404 Not Found` if the task does not exist

---

## 🚀 How to Run the Project

### 1. Clone the repository:

```bash
git clone https://github.com/alliah2025/flask-todo.git
cd flask-todo
```

### 2. Create a virtual environment and activate it:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Unix/macOS
```

### 3. Install dependencies:

```bash
pip install Flask Flask-SQLAlchemy
```

### 4. Initialize the database:

```python
# Run this in a Python shell or a separate script
from app_withRESTAPI import db, app
with app.app_context():
    db.create_all()
    print("Database initialized.")
```

### 5. Start the Flask app:

```bash
python app_withRESTAPI.py
```

- Web interface: [http://localhost:5000](http://localhost:5000)
- API endpoint: [http://localhost:5000/api/todos](http://localhost:5000/api/todos)

You can test the API using Postman:

- `GET /api/todos` — List all todos
- `POST /api/todos` — Create a new todo
- `GET /api/todos/<id>` — Get a specific todo
- `PUT /api/todos/<id>` — Update a specific todo
- `DELETE /api/todos/<id>` — Delete a specific todo

---

## 🧪 Testing

All API endpoints have been covered by unit tests using `pytest`.

- Positive and negative test cases for all CRUD operations
- Uses an in-memory SQLite database for clean and repeatable test runs

To run tests:

```bash
pytest test_app.py --cov=.
```

---

## 🎥 Video Presentation



## 📌 Repository Links

- 🔗 Original Repository: https://github.com/patrickloeber/flask-todo.git  
- 🔗 Forked with Enhancements: https://github.com/alliah2025/flask-todo/tree/feature/rest-api