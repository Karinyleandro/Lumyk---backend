from backend.app.models.Carrinho import Carrinho
from backend.app.db.config import db
from datetime import datetime, date
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.middlewares.autorizacao_carrinho import autorizacao_carrinho
import uuid

def listar_carrinhos(id_usuario):
    carrinhos = Carrinho.query.filter_by(id_usuario=id_usuario).all()
    return [c.to_dict() for c in carrinhos], 200


@jwt_required()
@autorizacao_carrinho
def buscar_por_id(id_usuario, id_carrinho):
    carrinho = Carrinho.query.get(id_carrinho)
    if not carrinho or carrinho.id_usuario != id_usuario:
        return {'mensagem': 'Carrinho não existe ou não pertence a você'}, 404
    return carrinho.to_dict(), 200


@jwt_required()
def criar_carrinho(id_usuario, data):
    try:
        data_criacao_str = data.get('data_criacao')
        data_criacao = datetime.strptime(data_criacao_str, "%Y-%m-%d").date() if data_criacao_str else date.today()

        novo_carrinho = Carrinho(
            id=str(uuid.uuid4()),
            id_usuario=id_usuario,
            data_criacao=data_criacao
        )
        db.session.add(novo_carrinho)
        db.session.commit()
        return {'mensagem': 'Carrinho criado com sucesso!', 'carrinho': novo_carrinho.to_dict()}, 201

    except Exception as e:
        return {'mensagem': f'Erro ao criar carrinho: {str(e)}'}, 500


@jwt_required()
@autorizacao_carrinho
def atualizar_carrinho(id_carrinho, id_usuario, data):
    carrinho = Carrinho.query.get(id_carrinho)
    if not carrinho or carrinho.id_usuario != id_usuario:
        return {'mensagem': 'Carrinho não existe ou não pertence a você'}, 404

    try:
        data_criacao_str = data.get('data_criacao')
        if data_criacao_str:
            carrinho.data_criacao = datetime.strptime(data_criacao_str, "%Y-%m-%d").date()
            db.session.commit()
            return {'mensagem': 'Carrinho atualizado com sucesso!', 'carrinho': carrinho.to_dict()}, 200
        return {'mensagem': 'Nada para atualizar'}, 400

    except Exception as e:
        return {'mensagem': f'Erro ao atualizar carrinho: {str(e)}'}, 500


@jwt_required()
@autorizacao_carrinho    
def deletar_carrinho(id_carrinho, id_usuario):
    carrinho = Carrinho.query.get(id_carrinho)
    if not carrinho or carrinho.id_usuario != id_usuario:
        return {'mensagem': 'Carrinho não existe ou não pertence a você'}, 404

    db.session.delete(carrinho)
    db.session.commit()
    return {'mensagem': 'Carrinho deletado com sucesso!'}, 200