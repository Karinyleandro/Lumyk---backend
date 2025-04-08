from app import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    biografia = db.Column(db.Text, nullable=False)
    foto = db.Column(db.Text, nullable=False)
