from app.db.database import db

class GeneroLivro(db.Model):
    __tablename__ = 'genero_livro'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True, nullable=False)
