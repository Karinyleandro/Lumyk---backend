import uuid 
from backend.app.db.config import db

class Endereco(db.Model):
    __tablename__ = 'Endereco'

    # o id coloquei em string porque tô usando o uuid para gerar um id único ele é dado em: c3c42be5-ca13-4a58-89a1-80d0f3775026
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

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