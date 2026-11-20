import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps CI/CD Dashboard' in response.data


def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_info_endpoint(client):
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.json['backend'] == 'Flask'


def test_status_endpoint(client):
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.json['application_status'] == 'running'


def test_version_endpoint(client):
    response = client.get('/api/version')
    assert response.status_code == 200
    assert response.json['version'] == '2.0.0'