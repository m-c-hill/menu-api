from flask import Blueprint

from cafe_menu_backend.api.v1.views import blueprint as v1_blueprint

blueprint = Blueprint("api", __name__, url_prefix="/api")
blueprint.register_blueprint(v1_blueprint)
