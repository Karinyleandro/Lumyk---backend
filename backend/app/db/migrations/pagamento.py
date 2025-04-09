from app import db

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forma_pagamento = db.Column(db.String(40), nullable=False)
