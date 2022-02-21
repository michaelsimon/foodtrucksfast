def test_listing(client):
    response = client.get("/list")
    assert response.status_code == 200