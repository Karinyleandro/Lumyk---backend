import uuid
from app.db.database import db

class Assinatura(db.Model):
    __tablename__ = 'Assinatura'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey('Usuario.id', ondelete='CASCADE', name='fk_assinatura_usuario'),
        nullable=False
    )

    tipo_assinatura = db.Column(db.String(40), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(40), nullable=False)
    preco_assinatura = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "tipo_assinatura": self.tipo_assinatura,
            "data_inicio": self.data_inicio.isoformat(),
            "data_fim": self.data_fim.isoformat(),
            "status": self.status,
            "preco_assinatura": self.preco_assinatura
        }
