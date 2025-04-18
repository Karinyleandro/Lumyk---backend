from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from backend.app.models.Pedido import Pedido

def autorizacao_pedido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        id_usuario_logado = get_jwt_identity()
        id_pedido = kwargs.get('id_pedido')

        pedido = Pedido.query.get(id_pedido)

        if not pedido:
            return jsonify({'mensagem': 'Pedido não encontrado.'}), 404

        if pedido.id_usuario != id_usuario_logado:
            return jsonify({'mensagem': 'Acesso negado: este pedido não pertence a você.'}), 403

        return f(*args, **kwargs)
    
    return wrapper