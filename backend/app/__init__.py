from flask import Flask
from flask_migrate import Migrate
from .db.database import db
from .routes.usuario_routes import usuario_bp
from app.models import * 
import os

migrate = Migrate()

def create_app():
    app = Flask(__name__)  

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'db', 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(usuario_bp)

    return app