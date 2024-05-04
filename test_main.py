from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_product():
    # Test creating a product
    response = client.post("/products/", json={"title": "Test Product", "description": "Test Description", "price": 10.99})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Product"

def test_get_all_products():
    # Test retrieving all products
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product_by_id():
    # First, create a product to get its ID
    response_create = client.post("/products/", json={"title": "Test Product", "description": "Test Description", "price": 10.99})
    assert response_create.status_code == 200
    product_id = response_create.json()["id"]

    # Test retrieving product by ID
    response_get = client.get(f"/products/{product_id}")
    assert response_get.status_code == 200
    assert response_get.json()["title"] == "Test Product"

def test_update_product():
    # First, create a product to get its ID
    response_create = client.post("/products/", json={"title": "Test Product", "description": "Test Description", "price": 10.99})
    assert response_create.status_code == 200
    product_id = response_create.json()["id"]

    # Test updating the product
    response_update = client.put(f"/products/{product_id}", json={"title": "Updated Product", "description": "Updated Description", "price": 15.99})
    assert response_update.status_code == 200
    assert response_update.json()["title"] == "Updated Product"

def test_delete_product():
    # First, create a product to get its ID
    response_create = client.post("/products/", json={"title": "Test Product", "description": "Test Description", "price": 10.99})
    assert response_create.status_code == 200
    product_id = response_create.json()["id"]

    # Test deleting the product
    response_delete = client.delete(f"/products/{product_id}")
    assert response_delete.status_code == 200
    assert response_delete.json()["message"] == "Product deleted successfully"
