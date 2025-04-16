import uuid
from app.db.config import db

class Pagamento(db.Model):
    __tablename__ = 'Pagamento'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    forma_pagamento = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "forma_pagamento": self.forma_pagamento
        }