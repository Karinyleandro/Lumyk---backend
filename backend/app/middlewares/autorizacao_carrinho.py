from functools import wraps
from flask_jwt_extended import get_jwt_identity
from backend.app.models.Carrinho import Carrinho

def autorizacao_carrinho(func):
    @wraps(func)
    def wrapper(id_carrinho, *args, **kwargs):
        carrinho = Carrinho.query.get(id_carrinho)

        if not carrinho:
            return {'mensagem': 'Carrinho não encontrado.'}, 404

        usuario_id = get_jwt_identity()
        if carrinho.id_usuario != usuario_id:
            return {'mensagem': 'Você não tem permissão para acessar este carrinho.'}, 403

        # Passa o carrinho como argumento nomeado
        return func(id_carrinho, *args, carrinho=carrinho, **kwargs)

    return wrapper