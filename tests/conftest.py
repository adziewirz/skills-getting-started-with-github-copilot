from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Provide a TestClient with activities restored after each test."""
    original_activities = deepcopy(activities)

    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(original_activities)
