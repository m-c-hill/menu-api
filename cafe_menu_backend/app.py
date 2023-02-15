import os

from flask import Flask

from cafe_menu_backend import api
from cafe_menu_backend.api.errors import register_error_handlers
from cafe_menu_backend.config import config
from cafe_menu_backend.extensions import db, migrate
from cafe_menu_backend.models import Customer, Dish, Order, OrderItem


def create_app(config_name: str = os.getenv("FLASK_CONFIG") or "default"):
    """
    Application factory to create a Flask app with the supplied configuration
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    configure_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(api.blueprint)
