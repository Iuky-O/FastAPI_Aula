from http import HTTPStatus
from fastapi.testclient import TestClient
import pytest
from teste_poetry.app import app

@pytest.fixture()
def client():
    return TestClient(app)

def test_read_root_deve_retornar_ok(client):

    response = client.get('/testes/teste_model')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo!"}

def test_create_user(client):
    #client = TestClient(app)

    response = client.post('/user/create_user_db', 
                json={
                    'name': 'teste',
                    'age': 10,
                    'email': 'teste@gmail.com',
                    'password': '1234567'
                })
    
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
                    'id': 1,
                    'name': 'teste',
                    'age': 10,
                    'email': 'teste@gmail.com',}
    
def test_read_all_users(client):

    response = client.get('/user/get_user_db/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users':[
        {
            'id': 1,
            'name': 'teste',
            'age': 10,
            'email': 'teste@gmail.com',
        }
    ]}

