import uuid
from backend.app.db.config import db

class ItemCarrinho(db.Model):
    __tablename__ = 'ItemCarrinho'

    # o id coloquei em string porque tô usando o uuid para gerar um id único ele é dado em: c3c42be5-ca13-4a58-89a1-80d0f3775026
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    id_carrinho = db.Column(
        db.Integer,
        db.ForeignKey('Carrinho.id', ondelete='CASCADE', name='fk_itemcarrinho_carrinho'),
        nullable=False
    )

    id_livro = db.Column(
        db.Integer,
        db.ForeignKey('Livro.id', ondelete='CASCADE', name='fk_itemcarrinho_livro'),
        nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "id_carrinho": self.id_carrinho,
            "id_livro": self.id_livro
        }