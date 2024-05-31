import os

from flask import Flask
from . import models


def create_app(script_info=None):
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from server.main.views import main_blueprint

    app.register_blueprint(main_blueprint)

    app.shell_context_processor({"app": app})

    app.debug = True

    return app
