import uuid
from app.db.config import db

class ItemPedido(db.Model):
    __tablename__ = 'ItemPedido'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    id_pedido = db.Column(
        db.Integer,
        db.ForeignKey('Pedido.id', ondelete='CASCADE', name='fk_itempedido_pedido'),
        nullable=False
    )

    id_livro = db.Column(
        db.Integer,
        db.ForeignKey('Livro.id', ondelete='CASCADE', name='fk_itempedido_livro'),
        nullable=False
    )

    preco_unitario = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_pedido": self.id_pedido,
            "id_livro": self.id_livro,
            "preco_unitario": self.preco_unitario,
            "quantidade": self.quantidade
        }