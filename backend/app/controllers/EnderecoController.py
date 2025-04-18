from backend.app.models.Endereco import Endereco
from backend.app.db.config import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.middlewares.autorizacao_endereco import autorizacao_endereco
import uuid

def listar_enderecos():
    enderecos = Endereco.query.all()
    return [endereco.to_dict() for endereco in enderecos], 200

@jwt_required()
def buscar_endereco_por_id(id):
    endereco = Endereco.query.get_or_404(id)
    return endereco.to_dict(), 200

@jwt_required()
def criar_endereco(data):
    usuario_id = get_jwt_identity()

    novo_endereco = Endereco(
        id=str(uuid.uuid4()),
        id_usuario=usuario_id,
        id_estado=data['id_estado'],
        numero=data['numero'],
        bairro=data['bairro'],
        rua=data['rua']
    )
    db.session.add(novo_endereco)
    db.session.commit()
    return {'mensagem': 'Endereço criado com sucesso!', 'endereco': novo_endereco.to_dict()}, 201

@jwt_required()
@autorizacao_endereco
def atualizar_endereco(id, data):
    endereco = Endereco.query.get_or_404(id)

    endereco.id_estado = data.get('id_estado', endereco.id_estado)
    endereco.numero = data.get('numero', endereco.numero)
    endereco.bairro = data.get('bairro', endereco.bairro)
    endereco.rua = data.get('rua', endereco.rua)

    db.session.commit()
    return {'mensagem': 'Endereço atualizado com sucesso!', 'endereco': endereco.to_dict()}, 200

@jwt_required()
@autorizacao_endereco
def deletar_endereco(id):
    endereco = Endereco.query.get_or_404(id)
    db.session.delete(endereco)
    db.session.commit()
    return {'mensagem': 'Endereço deletado com sucesso!'}, 200
