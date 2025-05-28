import pytest
import json
from app_withRESTAPI import app, db, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_create_todo_success(client):
    res = client.post('/api/todos', json={'title': 'Test task'})
    assert res.status_code == 201
    data = res.get_json()
    assert data['title'] == 'Test task'
    assert data['done'] is False

def test_create_todo_fail_no_title(client):
    res = client.post('/api/todos', json={'description': 'No title here'})
    assert res.status_code == 400
    data = res.get_json()
    assert 'error' in data

def test_get_todos_empty(client):
    res = client.get('/api/todos')
    assert res.status_code == 200
    assert res.get_json() == []

def test_get_todo_not_found(client):
    res = client.get('/api/todos/123')
    assert res.status_code == 404

def test_crud_flow(client):
    # Create
    res = client.post('/api/todos', json={'title': 'First task'})
    todo = res.get_json()
    todo_id = todo['id']

    # Read
    res = client.get(f'/api/todos/{todo_id}')
    assert res.status_code == 200
    assert res.get_json()['title'] == 'First task'

    # Update
    res = client.put(f'/api/todos/{todo_id}', json={'done': True})
    assert res.status_code == 200
    assert res.get_json()['done'] is True

    # Delete
    res = client.delete(f'/api/todos/{todo_id}')
    assert res.status_code == 200

    # Confirm deletion
    res = client.get(f'/api/todos/{todo_id}')
    assert res.status_code == 404
