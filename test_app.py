import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask CI/CD Demo' in response.data

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert 'message' in data

def test_app_info(client):
    """Test app info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert data['app'] == 'Flask CI/CD Demo'
    assert data['version'] == '1.0.0'
    assert 'environment' in data

def test_users_endpoint(client):
    """Test users endpoint"""
    response = client.get('/api/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
    assert data[0]['name'] == 'Rahul'
    assert data[1]['name'] == 'Priya'
    assert data[2]['name'] == 'Amit'

def test_invalid_endpoint(client):
    """Test invalid endpoint returns 404"""
    response = client.get('/api/nonexistent')
    assert response.status_code == 404
