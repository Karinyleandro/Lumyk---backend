from app.db.database import db

class ItemCarrinho(db.Model):
    __tablename__ = 'item_carrinho'

    id = db.Column(db.Integer, primary_key=True)
    id_carrinho = db.Column(db.Integer, db.ForeignKey('carrinho.id', ondelete='CASCADE'), nullable=False)
    id_livro = db.Column(db.Integer, db.ForeignKey('livro.id', ondelete='CASCADE'), nullable=False)
