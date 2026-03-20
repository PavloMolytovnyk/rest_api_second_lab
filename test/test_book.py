import pytest
from httpx import AsyncClient
from main import app
from uuid import uuid4

BASE_URL = "http://testserver"

@pytest.mark.asyncio
async def test_create_book():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.post(
            "/books/",
            json={
                "title": "Test Driven Development",
                "author": "Kent Beck",
                "description": "Clean code book",
                "status": "available",
                "year": 2003
            }
        )
    
    assert response.status_code == 201
    assert response.json()["title"] == "Test Driven Development"

@pytest.mark.asyncio
async def test_get_books_pagination():
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get("/books/?limit=1&offset=0")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 1

@pytest.mark.asyncio
async def test_get_non_existent_book():
    fake_id = uuid4()
    async with AsyncClient(app=app, base_url=BASE_URL) as ac:
        response = await ac.get(f"/books/{fake_id}")
    
    assert response.status_code == 404