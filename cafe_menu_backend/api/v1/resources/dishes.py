from flask import abort, jsonify, request

from cafe_menu_backend.extensions import db
from cafe_menu_backend.models import CategoryEnum, Dish


def get_all_dishes():
    """
    Retrieve all dishes on the menu
    """
    dishes = Dish.query.all()

    return (
        jsonify(
            {
                "success": True,
                "dishes": [dish.to_dict() for dish in dishes],
                "dish_count": len(dishes),
            }
        ),
        200,
    )


def get_dishes_by_category(category_name: str):
    """
    Retrieve all dishes on the menu
    """
    if category_name not in set(item.value for item in CategoryEnum):
        abort(404)

    dishes = Dish.query.filter_by(category=category_name).all()

    return (
        jsonify(
            {
                "success": True,
                "dishes": [dish.to_dict() for dish in dishes],
                "dish_count": len(dishes),
            }
        ),
        200,
    )


def get_dish_by_id(dish_id: int):
    """
    Retrieve dish by id
    """
    dish = Dish.query.filter_by(id=dish_id).one_or_none()

    if dish is None:
        abort(404)

    return (
        jsonify(
            {
                "success": True,
                "dish": dish.to_dict(),
            }
        ),
        200,
    )


def create_new_dish():
    """
    Add a new dish to the cafe menu
    """
    body = request.get_json()

    try:
        new_dish = Dish(
            name=body.get("name"),
            description=body.get("description"),
            price=body.get("price"),
            hot_or_cold=body.get("hot_or_cold"),
            category=body.get("category"),
            ingredients=body.get("ingredients"),
        )
        db.session.add(new_dish)
        db.session.commit()

        return (
            jsonify(
                {
                    "success": True,
                    "new_dish": new_dish.to_dict(),
                }
            ),
            201,
        )

    except:
        abort(422)


def delete_dish(dish_id: int):
    """
    Remove a dish from the cafe menu
    """
    dish = Dish.query.filter_by(id=dish_id).one_or_none()

    if dish is None:
        abort(404)

    try:
        db.session.delete(dish)
        db.session.commit()

        return (
            jsonify(
                {
                    "success": True,
                    "deleted": dish.id,
                }
            ),
            200,
        )

    except:
        abort(422)
