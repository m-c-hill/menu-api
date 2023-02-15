from flask import abort, jsonify, request

from cafe_menu_backend.extensions import db
from cafe_menu_backend.models import Order, OrderItem
from cafe_menu_backend.services import order as order_service


def get_order_by_id(order_id: int):
    """
    Retrieve order by id
    """
    order = Order.query.filter_by(id=order_id).one_or_none()

    if order is None:
        abort(404)

    return (
        jsonify(
            {
                "success": True,
                "order": order.to_dict(),
            }
        ),
        200,
    )


def create_order():
    """
    Create a new order
    """
    body = request.get_json()

    try:
        new_order = order_service.process_new_order(body)
        return jsonify({"success": True, "new_order": new_order.to_dict()}), 201

    except:
        abort(422)


def cancel_order(order_id: int):
    """
    Cancel an order
    """
    order = Order.query.filter_by(id=order_id).one_or_none()

    if order is None:
        abort(404)

    try:
        order.order_cancelled = True
        db.session.commit()

        return jsonify({"success": True, "cancelled_order": order.to_dict()}), 200
    except:
        abort(422)
