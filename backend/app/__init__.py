from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from backend.app.db.config import db
from backend.app.routes.usuario_routes import api as usuario_ns
from backend.app.models import *
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

    api = Api(app, version='1.0', title='API do app Lumyk', 
              description='Documentação automática da API com Flask-RESTx',
              doc='/docs')  
    
    api.add_namespace(usuario_ns, path='/usuarios')

    return app
