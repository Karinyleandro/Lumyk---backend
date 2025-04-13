from app.db.database import db

class Endereco(db.Model):
    __tablename__ = 'Endereco'

    id = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey('Usuario.id', ondelete='CASCADE', name='fk_endereco_usuario'),
        nullable=False
    )

    id_estado = db.Column(
        db.Integer,
        db.ForeignKey('Estado.id', ondelete='CASCADE', name='fk_endereco_estado'),
        nullable=False
    )

    numero = db.Column(db.Integer, nullable=False)
    bairro = db.Column(db.String(40), nullable=False)
    rua = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_estado": self.id_estado,
            "numero": self.numero,
            "bairro": self.bairro,
            "rua": self.rua
        }
