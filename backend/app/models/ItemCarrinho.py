import uuid
from app.db.database import db

class ItemCarrinho(db.Model):
    __tablename__ = 'ItemCarrinho'

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