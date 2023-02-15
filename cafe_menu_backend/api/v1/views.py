from flask import Blueprint

from cafe_menu_backend.api.v1.resources import index, dishes, orders

blueprint = Blueprint("v1", __name__, url_prefix="/v1.0")
blueprint.add_url_rule("/", "health_check", index.health_check)

# ==================
#  Dish endpoints
# ==================
blueprint.add_url_rule(
    "/dishes", "dishes", dishes.get_all_dishes, methods=["GET"]
)
blueprint.add_url_rule(
    "/dishes/category/<string:category_name>",
    "dishes_by_category",
    dishes.get_dishes_by_category,
)
blueprint.add_url_rule(
    "/dishes/<int:dish_id>",
    "dish_by_id",
    dishes.get_dish_by_id,
    methods=["GET", "POST"],
)
blueprint.add_url_rule(
    "/dishes", "dishes_create", dishes.create_new_dish, methods=["POST"]
)
blueprint.add_url_rule(
    "/dishes/<int:dish_id>", "dishes_delete", dishes.delete_dish, methods=["DELETE"]
)


# ==================
#  Order endpoints
# ==================
