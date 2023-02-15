import pytest

from cafe_menu_backend.app import create_app
from cafe_menu_backend.extensions import db
from .insert_test_data import insert_test_data


@pytest.fixture(scope="function")
def app():
    app = create_app("testing")

    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_test_data()

    yield app


@pytest.fixture(scope="function")
def client(app):
    return app.test_client()
