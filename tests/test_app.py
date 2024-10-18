import pytest
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
    
    with app.test_client() as client:
        yield client
    
    with app.app_context():
        db.drop_all()

def test_create_todo(client):
    response = client.post('/todos', json={'title': 'Test Todo'})
    assert response.status_code == 201
    assert response.json['title'] == 'Test Todo'
    assert response.json['completed'] == False

def test_get_todos(client):
    client.post('/todos', json={'title': 'Todo 1'})
    client.post('/todos', json={'title': 'Todo 2'})
    response = client.get('/todos')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['title'] == 'Todo 1'
    assert response.json[1]['title'] == 'Todo 2'

def test_delete_todo(client):
    response = client.post('/todos', json={'title': 'Todo to delete'})
    todo_id = response.json['id']
    
    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 204
    
    response = client.get('/todos')
    assert len(response.json) == 0