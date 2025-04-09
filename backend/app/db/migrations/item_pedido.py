from app import db

class ItemPedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id', ondelete='CASCADE'), nullable=False)
    id_livro = db.Column(db.Integer, db.ForeignKey('livro.id', ondelete='CASCADE'), nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
