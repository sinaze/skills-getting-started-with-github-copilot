

from fastapi.testclient import TestClient
from src.app import app

def test_get_activities():
    # Arrange
    client = TestClient(app)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert all("description" in v and "participants" in v for v in data.values())
