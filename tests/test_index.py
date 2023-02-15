def test_health_check(client):
    response = client.get("api/v1.0/")

    assert response.status_code == 200
    assert response.get_json()["success"] == True
    assert response.get_json()["message"] == "API is healthy"
