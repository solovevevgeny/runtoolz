from fastapi.testclient import TestClient

from app.main import app 


client = TestClient(app)

def test_read_avg_pace_40():
    data = {
                "hours": 0,
                "minutes": 40,
                "seconds": 0
            }
    response = client.post('/avg_pace/?distance=10', json=data)
    assert response.status_code == 200
    assert response.json() == { "pace": "4:0" } 

def test_read_avg_pace_50():
    data = {
                "hours": 0,
                "minutes": 25,
                "seconds": 0
            }
    response = client.post('/avg_pace/?distance=5', json=data)
    assert response.status_code == 200
    assert response.json() == { "pace": "5:0" } 

