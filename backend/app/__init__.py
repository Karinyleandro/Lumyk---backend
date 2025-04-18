from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager 
from backend.app.db.config import db
from backend.app.routes.usuario_routes import api as usuario
from backend.app.routes.authUsuario_routes import api as auth
from backend.app.routes.estado_routes import api as estados
from backend.app.routes.endereco_routes import api as endereco
from backend.app.routes.autor_routes import api as autor
from backend.app.routes.generoLivro_routes import api as genero
from backend.app.routes.livro_routes import api as livro
from backend.app.models import *
from dotenv import load_dotenv
import os

#jwt config .evn
load_dotenv()  

migrate = Migrate()

def create_app():
    app = Flask(__name__)  

    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'db', 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    
    app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']  
    app.config['JWT_TOKEN_LOCATION'] = ['headers']          
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app) 

    authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Insira seu token JWT com o prefixo **Bearer**'
    }
    }
    
    api = Api(
        app,
        version='1.0',
        title='API do app Lumyk',
        description='Documentação automática da API com Flask-RESTx',
        doc='/docs',
        authorizations=authorizations,
        security='Bearer Auth'
    )

    api.add_namespace(auth, path='/auth')
    api.add_namespace(usuario, path='/usuarios')
    api.add_namespace(estados, path='/estados')
    api.add_namespace(endereco, path='/enderecos')
    api.add_namespace(autor, path='/autores')
    api.add_namespace(genero, path='/generos')
    api.add_namespace(livro, path='/livros')
    
    return app
