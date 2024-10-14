def test_create_category(client):
    response = client.post("/categories/", json={"name": "Banana"})
    assert response.status_code == 200
    assert response.json()["name"] == "Banana"


def test_get_categories(client):
    response = client.get("/categories/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_get_category(client):
    response = client.post("/categories/", json={"name": "Apple"})
    category_id = response.json()["id"]

    response = client.get(f"/categories/{category_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Apple"

    response = client.get("/categories/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"