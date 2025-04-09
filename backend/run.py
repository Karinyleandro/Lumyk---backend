from flask import Flask
from app.db.database import db
from app.routes.usuario_routes import usuario_bp

import os

def create_app():
    app = Flask(__name__)

    # Define o caminho absoluto e seguro para o arquivo do banco
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'app', 'db', 'database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Prints de verificação
    print("Caminho do banco absoluto:", db_path)
    print("Arquivo existe?", os.path.isfile(db_path))
    print("Diretório do banco existe?", os.path.isdir(os.path.dirname(db_path)))

    # Inicializa o banco
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registra as rotas
    app.register_blueprint(usuario_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
