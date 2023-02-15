import pytest

from cafe_menu_backend.app import create_app
from cafe_menu_backend.extensions import db


@pytest.fixture(scope="function")
def app():
    app = create_app("testing")

    with app.app_context():
        db.drop_all()
        db.create_all()
    yield app


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()
