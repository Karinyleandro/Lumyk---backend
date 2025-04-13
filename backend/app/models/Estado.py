from app.db.database import db

class Estado(db.Model):
    __tablename__ = 'Estado'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }
