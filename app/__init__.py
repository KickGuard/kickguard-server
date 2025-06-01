from flask import Flask
from app.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from app.models import db
from app.routes.raspi import raspi_bp
from app.routes.client import client_bp
from app.routes.api_doc import api_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    app.register_blueprint(raspi_bp, url_prefix="/raspberry")
    app.register_blueprint(client_bp, url_prefix="/client")
    app.register_blueprint(api_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app
