from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_feedback_post():
    client = app.test_client()
    response = client.post('/feedback', json={"user": "Test", "rating": 5, "comment": "Great!"})
    assert response.status_code == 201

def test_feedback_get():
    client = app.test_client()
    response = client.get('/feedback')
    assert response.status_code == 200
