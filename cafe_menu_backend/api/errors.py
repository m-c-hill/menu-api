from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({"success": False, "error": 404, "message": "Not found"}), 404
