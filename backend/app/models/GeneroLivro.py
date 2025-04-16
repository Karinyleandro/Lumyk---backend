import uuid
from app.db.config import db

class GeneroLivro(db.Model):
    __tablename__ = 'GeneroLivro'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(40), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }