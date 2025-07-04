import uuid
from backend.app.db.config import db

class ItemCarrinho(db.Model):
    __tablename__ = 'ItemCarrinho'

    # o id coloquei em string porque tô usando o uuid para gerar um id único ele é dado em: c3c42be5-ca13-4a58-89a1-80d0f3775026
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    id_carrinho = db.Column(
        db.String(36),
        db.ForeignKey('Carrinho.id', ondelete='CASCADE', name='fk_itemcarrinho_carrinho'),
        nullable=False
    )

    id_livro = db.Column(
        db.String(36),
        db.ForeignKey('Livro.id', ondelete='CASCADE', name='fk_itemcarrinho_livro'),
        nullable=False
    )
    
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    
    formato = db.Column(db.String(40), nullable=True)
    tipo = db.Column(db.String(40), nullable=True)
    
    #relacionamentos
    carrinho = db.relationship('Carrinho', backref=db.backref('itens', cascade='all, delete-orphan'))
    livro = db.relationship('Livro')

    def to_dict(self, incluir_detalhes=False):
        base = {
            "id": self.id,
            "id_carrinho": self.id_carrinho,
            "id_livro": self.id_livro,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario,
            "formato": self.formato,
            "tipo": self.tipo
        }

        if incluir_detalhes:
            base["livro"] = self.livro.to_dict() if self.livro else None
            base["carrinho"] = self.carrinho.to_dict() if self.carrinho else None

        return base