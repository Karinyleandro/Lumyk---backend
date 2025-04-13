from app.db.database import db

class Carrinho(db.Model):
    __tablename__ = 'Carrinho'

    id = db.Column(db.Integer, primary_key=True)

    id_usuario = db.Column(
        db.Integer,
        db.ForeignKey('Usuario.id', ondelete='CASCADE', name='fk_carrinho_usuario'),
        nullable=False
    )

    data_criacao = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "data_criacao": self.data_criacao.isoformat()
        }
