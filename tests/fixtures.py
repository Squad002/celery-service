from microservice import create_app

import pytest
import os


@pytest.yield_fixture
def app():
    app, _ = create_app(
        config_name="testing",
    )

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

