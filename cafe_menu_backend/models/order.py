"""
Model for orders placed using the menu. Order items hold a specified quantity of a single dish, with an order containing any number of order items.
"""

from cafe_menu_backend.extensions import db
from sqlalchemy.sql import func


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    created_at = db.Column(db.DateTime, server_default=func.now())
    total_price = db.Column(db.Float)
    payment_complete = db.Column(db.Bool)
    order_fulfilled = db.Column(db.Bool)
    order_items = db.relationship("OrderItem", backref="order")


class OrderItem(db.Model):
    __tablename__ = "order_item"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"))
