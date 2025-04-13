from app.db.database import db

class Pagamento(db.Model):
    __tablename__ = 'Pagamento'

    id = db.Column(db.Integer, primary_key=True)
    forma_pagamento = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "forma_pagamento": self.forma_pagamento
        }


