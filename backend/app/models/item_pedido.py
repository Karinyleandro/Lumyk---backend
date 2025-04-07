from app.db.database import db

class ItemPedido(db.Model):
    __tablename__ = 'item_pedido'

    id = db.Column(db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id', ondelete='CASCADE'), nullable=False)
    id_livro = db.Column(db.Integer, db.ForeignKey('livro.id', ondelete='CASCADE'), nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_embalagem = db.Column(db.Float, nullable=False)
    embalagem = db.Column(db.Boolean, nullable=False)
