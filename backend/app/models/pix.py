from app.db.database import db

class Pix(db.Model):
    __tablename__ = 'pix'

    id = db.Column(db.Integer, primary_key=True)
    chave = db.Column(db.String(255), unique=True, nullable=False)
