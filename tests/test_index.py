def test_index(client):
    response = client.get("/")
    assert b"View all food trucks" in response.data