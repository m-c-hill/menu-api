"""
Model for orders placed using the menu. Order items hold a specified quantity of a single dish, with an order
containing any number of order items.
"""

from sqlalchemy.sql import func

from cafe_menu_backend.extensions import db


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    created_at = db.Column(db.DateTime, server_default=func.now())
    total_price = db.Column(db.Float)
    payment_complete = db.Column(db.Boolean, default=False)
    order_cancelled = db.Column(db.Boolean, default=False)
    order_fulfilled = db.Column(db.Boolean, default=False)
    order_items = db.relationship("OrderItem", backref="order")

    def to_dict(self) -> dict:
        return {
            "customer_id": self.customer_id,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "total_price": self.total_price,
            "payment_complete": self.payment_complete,
            "order_cancelled": self.order_cancelled,
            "order_fulfilled": self.order_fulfilled,
            "order_items": [item.to_dict() for item in self.order_items],
        }


class OrderItem(db.Model):
    __tablename__ = "order_item"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    quantity = db.Column(db.Integer)
    dish_id = db.Column(db.Integer, db.ForeignKey("dish.id"))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "quantity": self.quantity,
            "dish_id": self.dish_id,
            "dish_name": self.dish.name,
        }
