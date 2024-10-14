def test_create_product(client):
    response = client.post("/categories/", json={"name": "Fruits"})
    category_id = response.json()["id"]

    response = client.post("/products/", json={
        "name": "Apple",
        "description": "Sweet Apple",
        "price": 50,
        "category_id": category_id
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Apple"
    assert response.json()["category_id"] == category_id


def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


def test_update_product(client):
    response = client.post("/categories/", json={"name": "Furniture"})
    category_id = response.json()["id"]
    response = client.post("/products/", json={
        "name": "Chair",
        "description": "A comfortable chair.",
        "price": 150,
        "category_id": category_id
    })
    product_id = response.json()["id"]

    response = client.put(f"/products/{product_id}", json={
        "name": "Office Chair",
        "description": "An ergonomic office chair.",
        "price": 200,
        "category_id": category_id
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Office Chair"


def test_delete_product(client):
    response = client.post("/categories/", json={"name": "Appliances"})
    category_id = response.json()["id"]
    response = client.post("/products/", json={
        "name": "Toaster",
        "description": "A 2-slice toaster.",
        "price": 30,
        "category_id": category_id
    })
    product_id = response.json()["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Toaster"

    response = client.get(f"/products/{product_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_filter_products(client):
    response = client.post("/categories/", json={"name": "Electronics"})
    category_id = response.json()["id"]
    client.post("/products/", json={
        "name": "Laptop",
        "description": "A powerful laptop.",
        "price": 1000,
        "category_id": category_id
    })
    client.post("/products/", json={
        "name": "Smartphone",
        "description": "A latest model smartphone.",
        "price": 700,
        "category_id": category_id
    })

    response = client.get(f"/products/?category_id={category_id}")
    assert response.status_code == 200
    for product in response.json():
        assert product["category_id"] == category_id

    response = client.get("/products/?min_price=800")
    assert response.status_code == 200
    for product in response.json():
        assert product["price"] >= 800