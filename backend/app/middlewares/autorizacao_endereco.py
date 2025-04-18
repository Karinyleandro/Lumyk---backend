from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from backend.app.models.Endereco import Endereco

def autorizacao_endereco(func):
    @wraps(func)
    def wrapper(id, *args, **kwargs):
        endereco = Endereco.query.get(id)
        if not endereco:
            return {'mensagem': 'Endereço não encontrado.'}, 404

        usuario_id = get_jwt_identity()
        if endereco.id_usuario != usuario_id:
            return {'mensagem': 'Você não tem permissão para acessar este endereço.'}, 403

        return func(id, *args, **kwargs)

    return wrapper
