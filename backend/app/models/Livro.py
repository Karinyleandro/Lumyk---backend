import uuid
from backend.app.db.config import db

class Livro(db.Model):
    __tablename__ = 'Livro'

    # o id coloquei em string porque tô usando o uuid para gerar um id único ele é dado em: c3c42be5-ca13-4a58-89a1-80d0f3775026
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

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