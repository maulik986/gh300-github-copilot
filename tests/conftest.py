import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def restore_participants():
    original_participants = {
        name: activity["participants"][:]
        for name, activity in activities.items()
    }

    yield

    for name, activity in activities.items():
        activity["participants"][:] = original_participants[name]