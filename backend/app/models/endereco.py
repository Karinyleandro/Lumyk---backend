from app.db.database import db

class Endereco(db.Model):
    __tablename__ = 'endereco'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id', ondelete='CASCADE'), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(40), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
