from app.db.database import db

class Assinatura(db.Model):
    __tablename__ = 'assinatura'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    tipo_assinatura = db.Column(db.String(40), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    preco_assinatura = db.Column(db.Float, nullable=False)
