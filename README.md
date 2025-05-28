# Todo REST API Documentation

### Endpoints:

- **GET /api/todos**  
  Returns list of all todos.  
  Response: 200 OK, JSON array of tasks.

- **GET /api/todos/<id>**  
  Returns a single todo by id.  
  Response: 200 OK with task JSON, or 404 if not found.

- **POST /api/todos**  
  Creates a new todo.  
  Request JSON: { "title": "string", "description": "string (optional)", "done": bool (optional) }  
  Response: 201 Created with new todo JSON, or 400 Bad Request if missing title.

- **PUT /api/todos/<id>**  
  Updates existing todo by id.  
  Request JSON may contain any of: title, description, done  
  Response: 200 OK with updated todo JSON, or 404 if not found.

- **DELETE /api/todos/<id>**  
  Deletes todo by id.  
  Response: 200 OK with confirmation message, or 404 if not found.
