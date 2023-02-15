from datetime import datetime

from flask import abort

from cafe_menu_backend.extensions import db
from cafe_menu_backend.models import Customer, Dish, Order, OrderItem


def process_new_order(order_body: dict) -> Order:
    """
    Process a new order
    """
    customer = Customer.query.filter_by(id=order_body.get("customer_id")).one_or_none()

    if not customer:
        abort(404)

    order_items = _process_order_items(order_body.get("order_items"))
    total_price = _calculate_total_price(order_items)
    created_at = datetime.strptime(
        order_body.get("created_at"), "%a, %d %b %Y %H:%M:%S %Z"
    )

    order = Order(
        customer=customer,
        total_price=total_price,
        payment_complete=order_body.get("payment_complete"),
        created_at=created_at,
    )
    for order_item in order_items:
        order.order_items.append(order_item)

    db.session.add(order)
    db.session.add_all(order_items)
    db.session.commit()

    return order


def _process_order_items(order_items: list[dict]) -> list[OrderItem]:
    """
    Process each item in the order
    """
    return [
        OrderItem(
            dish=_get_dish(order_item.get("dish_id")),
            quantity=order_item.get("quantity"),
        )
        for order_item in order_items
    ]


def _calculate_total_price(order_items: list[OrderItem]) -> float:
    """
    Calculate the total price of the order
    """
    return sum(
        order_item.dish.price * order_item.quantity for order_item in order_items
    )


def _get_dish(dish_id: int) -> Dish:
    """
    Retrieve dish by id
    """
    dish = Dish.query.filter_by(id=dish_id).one_or_none()

    if dish is None:
        abort(404)

    return dish
