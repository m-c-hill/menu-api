import pytest

from cafe_menu_backend.app import create_app
from cafe_menu_backend.extensions import db
from .insert_test_data import insert_test_data


@pytest.fixture(scope="module")
def app():
    app = create_app("testing")

    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_test_data()

    yield app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


# TODO
@pytest.fixture(scope="module")
def all_dishes() -> list:
    pass


# TODO
@pytest.fixture(scope="module")
def mains_dishes() -> list:
    pass


# TODO
@pytest.fixture(scope="module")
def pizza() -> dict:
    pass


# TODO
@pytest.fixture(scope="module")
def new_dish() -> dict:
    pass


# TODO
@pytest.fixture(scope="module")
def order_one() -> dict:
    pass


# TODO
@pytest.fixture(scope="module")
def new_order() -> dict:
    pass


# TODO
@pytest.fixture(scope="module")
def new_order_response() -> dict:
    pass


# TODO
@pytest.fixture(scope="module")
def cancelled_order_response() -> dict:
    pass
