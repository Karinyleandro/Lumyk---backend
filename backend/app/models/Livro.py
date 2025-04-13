from app.db.database import db

class Livro(db.Model):
    __tablename__ = 'Livro'

    id = db.Column(db.Integer, primary_key=True)

    id_genero = db.Column(
        db.Integer,
        db.ForeignKey('GeneroLivro.id', ondelete='CASCADE', name='fk_livro_genero'),
        nullable=False
    )

    id_autor = db.Column(
        db.Integer,
        db.ForeignKey('Autor.id', ondelete='CASCADE', name='fk_livro_autor'),
        nullable=False
    )

    foto = db.Column(db.Text, nullable=False)
    sinopse = db.Column(db.String(350), nullable=False)
    estoque = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    formato = db.Column(db.String(40), nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
    titulo = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_genero": self.id_genero,
            "id_autor": self.id_autor,
            "foto": self.foto,
            "sinopse": self.sinopse,
            "estoque": self.estoque,
            "preco": self.preco,
            "formato": self.formato,
            "tipo": self.tipo,
            "titulo": self.titulo
        }
