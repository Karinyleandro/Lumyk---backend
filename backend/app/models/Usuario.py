import uuid
from app.db.config import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    senha = db.Column(db.String(8), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,  # nao pode retornar a senha
            "data_nascimento": self.data_nascimento.isoformat()
        }
