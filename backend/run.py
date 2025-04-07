from flask import Flask
from app.db.database import db
from app.routes.usuario_routes import usuario_bp  

import os

print("Caminho do banco absoluto:", os.path.abspath('app/db/database.db'))
print("Arquivo existe?", os.path.exists('app/db/database.db'))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Lumyk - PDM/backend/app/db/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registra o blueprint aqui
    app.register_blueprint(usuario_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
