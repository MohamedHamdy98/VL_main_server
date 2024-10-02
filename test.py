from fastapi.testclient import TestClient

client = TestClient(app)

def test_change_background():
    response = client.post(
        "/change_background",
        json={
            "video_url": "https://example.com/video.mp4",
            "background_url": "https://example.com/background.jpg"
        }
    )
    assert response.status_code == 202  # Adjust according to expected response
    assert "message" in response.json()  # Check if expected keys are present
