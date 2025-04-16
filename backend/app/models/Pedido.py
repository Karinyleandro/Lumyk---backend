import uuid
from app.db.config import db

class Pedido(db.Model):
    __tablename__ = 'Pedido'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey('Usuario.id', ondelete='CASCADE', name='fk_pedido_usuario'),
        nullable=False
    )
    id_endereco = db.Column(
        db.Integer,
        db.ForeignKey('Endereco.id', ondelete='CASCADE', name='fk_pedido_endereco'),
        nullable=False
    )
    id_pagamento = db.Column(
        db.Integer,
        db.ForeignKey('Pagamento.id', ondelete='SET NULL', name='fk_pedido_pagamento'),
        nullable=True
    )

    total = db.Column(db.Float, nullable=False)
    data_compra = db.Column(db.Date, nullable=False)
    taxa_frete = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_endereco": self.id_endereco,
            "id_pagamento": self.id_pagamento,
            "total": self.total,
            "data_compra": self.data_compra.isoformat(),
            "taxa_frete": self.taxa_frete
        }