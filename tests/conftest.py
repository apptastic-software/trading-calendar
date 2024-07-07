import pytest
from fastapi.testclient import TestClient
from trading_calendar.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client
