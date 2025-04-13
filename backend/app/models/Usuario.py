from app.db.database import db

class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    senha = db.Column(db.String(8), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "data_nascimento": self.data_nascimento.isoformat()
        }
