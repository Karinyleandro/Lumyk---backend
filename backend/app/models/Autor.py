from app.db.database import db

class Autor(db.Model):
    __tablename__ = 'Autor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    biografia = db.Column(db.Text, nullable=False)
    foto = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "biografia": self.biografia,
            "foto": self.foto
        }
