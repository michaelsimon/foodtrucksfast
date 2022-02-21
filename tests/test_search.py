
def test_search(client):
    response = client.post("/search", data={
        'search_term=Casita',
    })
    assert b"Casita Vegana" in response.data