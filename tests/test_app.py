def test_create_todo(client):
    response = client.post('/todos', json={'title': 'Test Todo'})
    assert response.status_code == 201
    assert response.json['title'] == 'Test Todo'
    assert response.json['completed'] is False


def test_get_todos(client):
    client.post('/todos', json={'title': 'Todo 1'})
    client.post('/todos', json={'title': 'Todo 2'})
    response = client.get('/todos')
    assert response.status_code == 200
    assert len(response.json) == 2


def test_delete_todo(client):
    response = client.post('/todos', json={'title': 'Todo to delete'})
    todo_id = response.json['id']
    
    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 204
    
    response = client.get('/todos')
    assert len(response.json) == 0