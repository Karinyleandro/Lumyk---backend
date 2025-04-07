from app.db.database import db

class Pedido(db.Model):
    __tablename__ = 'pedido'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id', ondelete='CASCADE'), nullable=False)
    id_pix = db.Column(db.Integer, db.ForeignKey('pix.id', ondelete='SET NULL'), nullable=True)
    forma_pagamento = db.Column(db.String(40), nullable=False)
    total = db.Column(db.Float, nullable=False)
    data_compra = db.Column(db.Date, nullable=False)
    taxa_frete = db.Column(db.Float, nullable=False)
