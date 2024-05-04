from fastapi.testclient import TestClient
from apps.app import app




client = TestClient(app)


bookId=1

def test_create_book():
    # Test creating a book
    response = client.post(
        "/books", json={"title": "Test Book", "author": "Test Author","isbn":"264647595","year":2021}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"
    assert response.json()["author"] == "Test Author"
    global bookId
    bookId=response.json()["id"]


def test_get_books():
    # Test retrieving all books
    response = client.get("/books")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_book_by_id():
    # Test retrieving a single book by id 
    response = client.get(f"/books/{bookId}")
    assert response.status_code == 200
    assert response.json()["id"] == bookId


def test_update_book():
    # Test updating a book
    response = client.patch(f"/books/{bookId}", json={"title": "Updated Book Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Book Title"


def test_delete_book():
    # Test deleting a book
    response = client.delete(f"/books/{bookId}")
    assert response.status_code == 204
