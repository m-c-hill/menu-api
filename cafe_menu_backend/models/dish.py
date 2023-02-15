"""
Model for dishes listed on the menu
"""

import enum

from cafe_menu_backend.extensions import db


class TemperatureEnum(enum.Enum):
    hot = "hot"
    cold = "cold"


class CategoryEnum(enum.Enum):
    starters = "starters"
    mains = "mains"
    specials = "specials"
    sides = "sides"
    desserts = "desserts"
    drinks = "drinks"


class Dish(db.Model):
    __tablename__ = "dish"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    hot_or_cold = db.Column(db.Enum(TemperatureEnum))
    category = db.Column(db.Enum(CategoryEnum))
    # TODO: convert ingredients to list, skipping for now to simplify testing
    ingredients = db.Column(db.String)
    order_items = db.relationship("OrderItem", backref="dish")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "hot_or_cold": self.hot_or_cold.value,
            "category": self.category.value,
            "ingredients": self.ingredients,
        }
