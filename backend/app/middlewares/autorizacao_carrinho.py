from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from backend.app.models.Carrinho import Carrinho

def autorizacao_carrinho(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id_carrinho = kwargs.get('id_carrinho') or (args[0] if args else None)

        if not id_carrinho:
            return {'mensagem': 'ID do carrinho não fornecido.'}, 400

        carrinho = Carrinho.query.get(id_carrinho)
        if not carrinho:
            return {'mensagem': 'Carrinho não encontrado.'}, 404

        usuario_id = get_jwt_identity()
        if carrinho.id_usuario != usuario_id:
            return {'mensagem': 'Você não tem permissão para acessar este carrinho.'}, 403

        return func(*args, **kwargs)

    return wrapper