from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# instantiate db object
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
# instantiate app
    db.init_app(app)

    from .views import api
    app.register_blueprint(api)

    return app