import pytest
from httpx import AsyncClient
from api.main import app



@pytest.fixture
def test_app():
    return app


@pytest.fixture
async def client(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as ac:
        yield ac
