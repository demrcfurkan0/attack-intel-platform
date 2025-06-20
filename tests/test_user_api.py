import pytest
from httpx import AsyncClient
from app.main import app
from app.database import get_db_dependency 

MOCK_USERS_DB = [
    {
        "_id": "60d5ec49f72e3a5a9c5e8f1a",
        "username": "testuser1",
        "email": "test1@example.com",
        "role": "Analyst",
        "status": "active"
    },
    {
        "_id": "60d5ec49f72e3a5a9c5e8f1b",
        "username": "testuser2",
        "email": "test2@example.com",
        "role": "Operator",
        "status": "inactive"
    }
]

async def override_get_db_dependency():
    class MockDb:
        def __init__(self):
            self.users = self.MockCollection()
        
        class MockCollection:
            def find(self, query={}):
                return MOCK_USERS_DB
    return MockDb()

app.dependency_overrides[get_db_dependency] = override_get_db_dependency

@pytest.mark.asyncio
async def test_get_all_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/users")
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) == 2
    assert response_data[0]["username"] == "testuser1"

def teardown_function():
    app.dependency_overrides = {}