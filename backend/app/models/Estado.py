import uuid
from app.db.config import db

class Estado(db.Model):
    __tablename__ = 'Estado'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }