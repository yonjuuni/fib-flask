from flask import Flask
from werkzeug.contrib.cache import SimpleCache

from config import config


cache = SimpleCache()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from api.v1 import v1
    app.register_blueprint(v1, url_prefix='/v1')

    return app
