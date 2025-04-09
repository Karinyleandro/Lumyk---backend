from app import db

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    id_endereco = db.Column(db.Integer, db.ForeignKey('endereco.id', ondelete='CASCADE'), nullable=False)
    id_pagamento = db.Column(db.Integer, db.ForeignKey('pagamento.id', ondelete='SET NULL'), nullable=True)
    total = db.Column(db.Float, nullable=False)
    data_compra = db.Column(db.Date, nullable=False)
    taxa_frete = db.Column(db.Float, nullable=False)
