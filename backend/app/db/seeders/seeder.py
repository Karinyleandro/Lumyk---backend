import sys
import os
from datetime import date

# Adiciona o diretório raiz do projeto no sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from run import create_app
from app import db
from app.models.Usuario import Usuario 

def seed_usuarios():
    usuarios = [
        Usuario(
            nome="Maria Vitória",
            email="maria@gmail.com",
            senha="senha123", 
            data_nascimento=date(2000, 5, 20)
        ),
        Usuario(
            nome="João Silva",
            email="joao.silva@gmail.com",
            senha="senha456",
            data_nascimento=date(1998, 12, 10)
        )
    ]
    db.session.bulk_save_objects(usuarios)
    db.session.commit()
    print("Usuários inseridos com sucesso!")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_usuarios()
