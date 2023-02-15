import pytest

from cafe_menu_backend.app import create_app
from cafe_menu_backend.extensions import db

from .insert_test_data import insert_test_data

# ================================
#  Mock flask app and client
# ================================


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


# ================================
#  Response fixtures
# ================================


@pytest.fixture(scope="module")
def all_dishes() -> list:
    return [
        {
            "category": "mains",
            "description": "Large margarita pizza",
            "hot_or_cold": "hot",
            "id": 1,
            "ingredients": "Dough, cheese, tomato sauce",
            "name": "Pizza",
            "price": 10.99,
        },
        {
            "category": "mains",
            "description": "1/4 lb burger in sesame bun",
            "hot_or_cold": "hot",
            "id": 2,
            "ingredients": "bread, beef, cheese, lettuce",
            "name": "Burger",
            "price": 8.99,
        },
        {
            "category": "sides",
            "description": "Oven chips served with ketchup",
            "hot_or_cold": "hot",
            "id": 3,
            "ingredients": "Potato",
            "name": "Chips",
            "price": 3.99,
        },
        {
            "category": "desserts",
            "description": "Selection of chocolate and vanilla ice cream",
            "hot_or_cold": "cold",
            "id": 4,
            "ingredients": "Ice cream, wafer, chocolate sauce",
            "name": "Ice cream",
            "price": 5.99,
        },
    ]


@pytest.fixture(scope="module")
def mains_dishes() -> list:
    return [
        {
            "category": "mains",
            "description": "Large margarita pizza",
            "hot_or_cold": "hot",
            "id": 1,
            "ingredients": "Dough, cheese, tomato sauce",
            "name": "Pizza",
            "price": 10.99,
        },
        {
            "category": "mains",
            "description": "1/4 lb burger in sesame bun",
            "hot_or_cold": "hot",
            "id": 2,
            "ingredients": "bread, beef, cheese, lettuce",
            "name": "Burger",
            "price": 8.99,
        },
    ]


@pytest.fixture(scope="module")
def pizza() -> dict:
    return {
        "category": "mains",
        "description": "Large margarita pizza",
        "hot_or_cold": "hot",
        "id": 1,
        "ingredients": "Dough, cheese, tomato sauce",
        "name": "Pizza",
        "price": 10.99,
    }


@pytest.fixture(scope="module")
def new_dish() -> dict:
    return {
        "name": "Sushi",
        "description": "Fresh salmon in rice and nori",
        "price": 11.29,
        "hot_or_cold": "cold",
        "category": "mains",
        "ingredients": "Salmon, rice, nori",
    }


@pytest.fixture(scope="module")
def new_dish_response() -> dict:
    return {
        "id": 5,
        "name": "Sushi",
        "description": "Fresh salmon in rice and nori",
        "price": 11.29,
        "hot_or_cold": "cold",
        "category": "mains",
        "ingredients": "Salmon, rice, nori",
    }


@pytest.fixture(scope="module")
def order_one() -> dict:
    return {
        "customer_id": 1,
        "created_at": "2023-01-05 23:55:59",
        "total_price": 18.97,
        "payment_complete": True,
        "order_cancelled": False,
        "order_fulfilled": False,
        "order_items": [
            {"id": 1, "quantity": 1, "dish_id": 2, "dish_name": "Burger"},
            {"id": 2, "quantity": 2, "dish_id": 3, "dish_name": "Chips"},
            {"id": 3, "quantity": 1, "dish_id": 4, "dish_name": "Ice cream"},
        ],
    }


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
