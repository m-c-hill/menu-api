from flask import Blueprint

from cafe_menu_backend.api.v1.resources import dishes, index, orders

blueprint = Blueprint("v1", __name__, url_prefix="/v1.0")
blueprint.add_url_rule("/", "health_check", index.health_check)

# ==================
#  Dish endpoints
# ==================
blueprint.add_url_rule("/dishes", "dishes", dishes.get_all_dishes)
blueprint.add_url_rule(
    "/dishes/category/<string:category_name>",
    "dishes_by_category",
    dishes.get_dishes_by_category,
)
blueprint.add_url_rule("/dishes/<int:dish_id>", "dish_by_id", dishes.get_dish_by_id)
blueprint.add_url_rule(
    "/dishes", "create_dish", dishes.create_new_dish, methods=["POST"]
)
blueprint.add_url_rule(
    "/dishes/<int:dish_id>", "delete_dish", dishes.delete_dish, methods=["DELETE"]
)


# ==================
#  Order endpoints
# ==================
blueprint.add_url_rule("/orders/<int:order_id>", "order_by_id", orders.get_order_by_id)
blueprint.add_url_rule("/orders", "create_order", orders.create_order, methods=["POST"])
blueprint.add_url_rule(
    "/orders", "cancel_order", orders.cancel_order, methods=["PATCH"]
)
