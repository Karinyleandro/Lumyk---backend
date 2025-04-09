from app import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero_livro.id', ondelete='CASCADE'), nullable=False)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id', ondelete='CASCADE'), nullable=False)
    foto = db.Column(db.Text, nullable=False)
    sinopse = db.Column(db.String(350), nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    formato = db.Column(db.String(40), nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
