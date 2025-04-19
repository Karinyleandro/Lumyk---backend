import uuid
from backend.app.db.config import db

class ItemPedido(db.Model):
    __tablename__ = 'ItemPedido'

    # o id coloquei em string porque tô usando o uuid para gerar um id único ele é dado em: c3c42be5-ca13-4a58-89a1-80d0f3775026
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    id_pedido = db.Column(
        db.String(36),
        db.ForeignKey('Pedido.id', ondelete='CASCADE', name='fk_itempedido_pedido'),
        nullable=False
    )

    id_livro = db.Column(
        db.String(36),
        db.ForeignKey('Livro.id', ondelete='CASCADE', name='fk_itempedido_livro'),
        nullable=False
    )

    preco_unitario = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    
    # Relacionamento
    livro = db.relationship("Livro", backref="itens_pedido", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "id_pedido": self.id_pedido,
            "id_livro": self.id_livro,
            "preco_unitario": self.preco_unitario,
            "quantidade": self.quantidade,
            "pedido": self.pedido.to_dict() if self.pedido else None,
            "livro": self.livro.to_dict() if self.livro else None
        }