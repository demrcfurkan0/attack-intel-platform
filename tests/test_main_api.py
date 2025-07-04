import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/")
    
    assert response.status_code == 200
    
    assert response.json() == {"message": "API is running!"}