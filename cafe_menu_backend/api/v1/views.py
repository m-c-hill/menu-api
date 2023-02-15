from flask import Blueprint

from cafe_menu_backend.api.v1.resources import index

blueprint = Blueprint("v1", __name__, url_prefix="/v1.0")
blueprint.add_url_rule("/", "health_check", index.health_check)
